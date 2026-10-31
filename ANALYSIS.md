# Анализ исходного кода: Investing Demo

Документ описывает фактически реализованное приложение по состоянию исходного кода в репозитории. Выявленные дефекты указаны как наблюдения, а не как задуманное поведение.

---

## 1. Назначение приложения и технологический стек

### Назначение

**Investing** — веб-приложение для просмотра и администрирования справочника акций (инструментов фондового рынка). Пользователь видит список акций с тикером, названием, ISIN, последней ценой и цветовой индикацией тренда; открывает карточку инструмента с графиком дневных свечей за последние 180 дней; авторизованный пользователь может создавать, изменять и удалять записи. Данные о бумагах и котировках поступают из **Tinkoff Invest API**. Фоновая задача Celery периодически обновляет последнюю цену и флаг роста/падения.

Приложение не реализует торговлю, портфель, персональные списки наблюдения и хранение истории цен в собственной БД: история строится «на лету» запросом к Tinkoff при открытии карточки.

### Технологический стек

| Слой | Технология |
|------|------------|
| Язык | Python 3 (ориентир по зависимостям 2023 года) |
| Веб-фреймворк | Django 4.1.7 |
| HTTP API | Django REST Framework 3.14 |
| ORM / БД | Django ORM + PostgreSQL (`psycopg2-binary`) |
| Кэш / брокер очередей | Redis |
| Фоновые задачи | Celery 5.2.7 + Celery Beat |
| Рыночные данные | `tinkoff-investments` (gRPC-клиент Tinkoff Invest) |
| Графики | Plotly (серверный `plot()`, клиентский Plotly.js с CDN) |
| Формы UI | django-crispy-forms + crispy-bootstrap3 |
| Фильтрация API | django-filter |
| Контейнеры инфраструктуры | Docker Compose: PostgreSQL и Redis |
| Интерфейс | HTML-шаблоны Django, Bootstrap 3/4 (локальные CSS + CDN: jQuery, Font Awesome, Moment.js, Tempus Dominus) |

Точка входа Django: `manage.py` с `DJANGO_SETTINGS_MODULE=config.settings`. WSGI: `config.wsgi`, ASGI: `config.asgi` (стандартные заготовки без дополнительной логики).

---

## 2. Структура проекта, основные компоненты и их назначение

```
aidd-topic-03-homework/
├── manage.py                 # CLI Django
├── requirements.txt          # закреплённые зависимости
├── docker-compose.yml        # PostgreSQL и Redis
├── config/                   # проект Django (настройки, URL, Celery)
│   ├── settings.py
│   ├── urls.py
│   ├── celery.py
│   ├── wsgi.py / asgi.py
│   └── __init__.py           # импорт celery_app при старте Django
├── dashboard/                # домен «акции»: модели, UI, API, задачи
│   ├── models.py
│   ├── views.py / forms.py / urls.py / admin.py
│   ├── tasks.py
│   ├── services/             # интеграция с Tinkoff и построение графиков
│   ├── api/v1/               # REST API
│   ├── management/commands/add_shares.py
│   ├── templates/dashboard/
│   ├── static/dashboard/css/
│   ├── migrations/
│   └── tests.py              # API-тесты Share
└── user/                     # регистрация, вход, выход
    ├── views.py / forms.py / urls.py / models.py
    ├── templates/user/
    └── static/user/css/
```

### Компоненты

**`config`** — конфигурационный пакет проекта (не бизнес-приложение). Содержит настройки БД, Celery, REST Framework, логирование, корневой маршрутизатор.

**`dashboard`** — основное приложение:

- модель `Share`;
- HTML CRUD (список, детальная страница, создание, обновление, удаление);
- REST API `/api/v1/shares/`;
- сервисы `market_data` и `graph`;
- Celery-задача `update_last_price`;
- management-команда `add_shares` для первичной загрузки инструментов из Tinkoff;
- регистрация модели в Django Admin.

**`user`** — аутентификация на стандартной модели `django.contrib.auth.models.User`. Собственных моделей нет (`user/models.py` только реэкспортирует `get_user_model()`). Миграций у приложения нет.

**Инфраструктура:**

- `docker-compose.yml`: сервис `db` (образ `postgres`, БД `investing`, пользователь/пароль `postgres`, порт 5432) и `redis` (6379).
- Логи: консоль и файл `app.logs` (логгер `main`).

---

## 3. Архитектура приложения и взаимодействие компонентов

Архитектура — классический **монолит Django** с тремя каналами доступа к одним и тем же данным `Share`:

1. серверный HTML (MTV);
2. REST API (DRF ViewSet);
3. Django Admin.

Внешние системы: **PostgreSQL** (хранение), **Redis** (брокер Celery), **Tinkoff Invest API** (инструменты, last price, свечи).

```
                    ┌──────────────┐
   Браузер ────────►│ Django WSGI  │
                    │ config.urls  │
                    └──────┬───────┘
           ┌───────────────┼────────────────┐
           ▼               ▼                ▼
     dashboard.urls    user.urls      /admin/
     HTML + /api/     login/reg/logout
           │
     ┌─────┴──────┐
     ▼            ▼
  CBV views    DRF ShareViewSet
     │            │
     ▼            ▼
  ORM Share ◄── PostgreSQL
     ▲
     │  Celery Beat (каждые 10 с, имя расписания «5 min»)
     │  dashboard.tasks.update_last_price
     │         │
     │         ▼
     │   market_data.get_last_data ──► Tinkoff gRPC
     │
     └── graph.get_graph (при GET детальной страницы) ──► Tinkoff candles
```

### Потоки взаимодействия

1. **Просмотр списка.** `ShareListView` читает `Share` из БД, сортирует по `name`, пагинирует по 100 записей, отдаёт `dashboard/list.html`. Цена и тренд берутся из полей модели, которые обновляет Celery, а не из запроса к API в момент отрисовки.

2. **Карточка акции.** `ShareDetailView` загружает `Share` по `id` и вызывает `get_graph(share)`: синхронный запрос свечей Tinkoff за 180 дней, построение Plotly `Scatter`, HTML-фрагмент графика вставляется в шаблон с `{% autoescape off %}`.

3. **CRUD HTML.** Создание/изменение/удаление доступны через `IsUserAuthenticatedMixin` (проверка `request.user.is_authenticated`). Форма `ShareModelForm` с `fields = "__all__"`. После успеха — редирект на список.

4. **REST.** `DefaultRouter` регистрирует `ShareViewSet` на `shares`. Полный ModelViewSet: list/retrieve/create/update/destroy. Пагинация LimitOffset (размер страницы 100), фильтры по `name`/`ticker`, поиск по `name`, сортировка по `name`/`ticker`. Аутентификация API в настройках не задана (по умолчанию DRF: AllowAny).

5. **Первичное наполнение.** `python manage.py add_shares` вызывает `client.instruments.shares()` и `Share.objects.get_or_create(...)` по полям инструмента.

6. **Фоновое обновление цен.** Worker выполняет `update_last_price`: для каждой акции `get_last_data` (last prices по FIGI), сравнение с предыдущим `last_price`, запись `last_price` и `is_trend_high`. Время из ответа Tinkoff (`detetime`) в модель не сохраняется.

7. **Пользователи.** Регистрация создаёт Django User с `username=email` и `email=email`, сразу выполняет `login`. Вход: `authenticate` по email (приводится к нижнему регистру) и паролю. Выход: `logout` и редирект на главную.

### Наблюдения по архитектуре (не требования)

- Корневой include пользователей: `path("user", include("user.urls"))` **без** завершающего `/`. Именованные URL резолвятся в `/userlogin/`, `/userregistration/`, `/userlogout/`, а не в `/user/login/` и т.д.
- Mixin при отказе в доступе редиректит на `dashboard:index`, а не на страницу входа; `handle_no_permission` объявлен как `@staticmethod`.
- Расписание Beat названо `add-every-5-min`, фактически `schedule: 10.0` секунд.
- Цена из Tinkoff берётся только как `price.units` / `candle.close.units` — дробная часть (`nano`) отбрасывается.
- `QuerySet.update()` для цены **не** обновляет `auto_now`-поле `updated_at` (оно меняется при `save()` модели).
- В `docker-compose` у PostgreSQL нет явной версии образа; том `./:/app` монтирует исходники в контейнер БД и не обеспечивает именованный volume для данных Postgres.
- `SECRET_KEY` и `TINKOFF_TOKEN` в `settings.py` пустые; `DEBUG = True`, `ALLOWED_HOSTS = []`.

---

## 4. Используемые библиотеки и внешние зависимости

Источник: `requirements.txt` (версии зафиксированы pin’ами).

### Прикладные зависимости

| Пакет | Версия | Роль |
|-------|--------|------|
| Django | 4.1.7 | веб-фреймворк |
| djangorestframework | 3.14.0 | REST API |
| django-filter | 22.1 | фильтрация queryset в API |
| django-crispy-forms | 2.0 | разметка форм |
| crispy-bootstrap3 | 2022.1 | шаблоны Bootstrap 3 для crispy |
| psycopg2-binary | 2.9.5 | драйвер PostgreSQL |
| celery | 5.2.7 | очередь задач |
| redis | 4.5.1 | брокер Celery |
| kombu, amqp, billiard, vine | транзитивные | транспорт Celery |
| tinkoff-investments | 0.2.0b50 | клиент Tinkoff Invest |
| tinkoff | 0.1.1 | связанный пакет экосистемы Tinkoff |
| grpcio, protobuf | 1.51.3 / 3.20.3 | транспорт клиента Tinkoff |
| plotly | 5.13.1 | графики |
| pydantic | 1.10.6 | модели SDK Tinkoff |
| cachetools | 5.3.0 | кэш (зависимость SDK) |
| python-dateutil, pytz, six | даты/совместимость | |
| asgiref, sqlparse, tenacity, typing_extensions, async-timeout | инфраструктура Django/клиентов | |

### Инструменты разработки в том же файле

- `black==23.1.0`, `isort==5.12.0` и их зависимости (`click`, `pathspec`, `platformdirs`, `tomli`, `mypy-extensions`, `packaging`).

README дополнительно предлагает для Windows-воркера Celery пакеты `eventlet` и `cryptography` — в `requirements.txt` их нет.

### Внешние сервисы и CDN (не pip)

- Tinkoff Invest API (токен `TINKOFF_TOKEN`).
- PostgreSQL, Redis (Docker).
- CDN: Plotly.js, jQuery 3.3.1, Popper.js, Font Awesome 4.7, Moment.js, Tempus Dominus Bootstrap 4. Скрипты datetime picker в шаблонах подключены, но в формах не используются.
- Локальные статические файлы: `sticky-footer-navbar.css`, `signin.css`. Шаблоны ссылаются на `bootstrap.min.css` в `dashboard/static` и `user/static`; в репозитории этих файлов нет.

AMQP-брокер в настройках закомментирован (`amqp://guest:guest@localhost:5672`); используется Redis.

---

## 5. Модель данных: сущности, атрибуты и связи

Отдельной ER-диаграммы в проекте нет. По факту — **одна прикладная сущность** плюс стандартный пользователь Django.

### Сущность `Share` (`dashboard.models.Share`)

Справочник акций. Таблица создаётся миграциями `0001`–`0007`.

| Атрибут | Тип | Ограничения | Назначение |
|---------|-----|-------------|------------|
| `id` | BigAutoField | PK | внутренний идентификатор |
| `figi` | CharField(255) | unique | FIGI инструмента Tinkoff |
| `isin` | CharField(255) | — | ISIN |
| `name` | CharField(255) | verbose_name «Наименование компании» | название |
| `ticker` | CharField(10) | unique | биржевой тикер |
| `currency` | CharField(20) | — | валюта котировки |
| `uid` | CharField(255) | unique | UID инструмента в Tinkoff |
| `last_price` | FloatField | blank/null | последняя цена (целая часть units) |
| `is_trend_high` | BooleanField | blank/null | True, если новая цена ≥ предыдущей (при ошибке сравнения тоже True) |
| `updated_at` | DateTimeField | auto_now, blank/null | время последнего `save()` модели |

Связей ForeignKey/M2M у `Share` нет. История котировок **не** моделируется: свечи не сохраняются.

`ShareSerializer` отдаёт: `id`, `figi`, `isin`, `name`, `ticker`, `currency`, `last_price`, `is_trend_high`, `updated_at`. Поле `uid` в API не сериализуется, хотя есть в модели и в HTML-форме (`fields = "__all__"`).

### Сущность `User` (встроенная Django)

Кастомная модель пользователя не задана (`AUTH_USER_MODEL` не переопределён).

Регистрация: `User.objects.create_user(email, email, password)` → `username` = email, `email` = email, пароль хешируется стандартными валидаторами из `AUTH_PASSWORD_VALIDATORS`.

Связи User ↔ Share **нет**: акции глобальные, не принадлежат пользователю. Авторизация влияет только на видимость кнопок CRUD и доступ к CBV создания/изменения/удаления.

### Админка

`ShareAdmin`: список `figi`, `isin`, `name`, `ticker`, `currency`; поиск по тем же полям; в форме редактирования также `uid`, `last_price`, `is_trend_high` (без `updated_at`).

---

## 6. Механизмы обработки пользовательских запросов и взаимодействия с БД

### Маршрутизация HTTP

Корневой `config/urls.py`:

| Префикс | Приложение |
|---------|------------|
| `/admin/` | Django Admin |
| `/` | `dashboard.urls` |
| `user` | `user.urls` (без слэша) |

`dashboard/urls.py` (`app_name = "dashboard"`):

| Метод / путь | Представление | БД |
|--------------|---------------|-----|
| GET `/` | `ShareListView` | `SELECT` Share, ordering `name`, paginate 100 |
| GET `/<int:pk>` | `ShareDetailView` | `Share.objects.get(id=pk)` + внешний API Tinkoff |
| GET/POST `/create` | `ShareCreateView` | `INSERT` через ModelForm |
| GET/POST `/update/<int:pk>` | `ShareUpdateView` | `UPDATE` через ModelForm |
| GET/POST `/delete/<int:pk>` | `ShareDeleteView` | `DELETE` |
| `/api/` → `/api/v1/` | DRF router | см. ниже |

`user/urls.py` (`app_name = "user"`):

| Путь (как в include) | Представление | БД |
|----------------------|---------------|-----|
| `login/` | `AuthView` | `authenticate` / сессия |
| `registration/` | `RegistrationView` | `create_user` + `login` |
| `logout/` | `LogoutView` | сброс сессии |

Сессии и CSRF — стандартный middleware Django. HTML-формы передают `{% csrf_token %}`.

### Обработка запросов UI

- **Список/CRUD:** class-based views (`ListView`, `CreateView`, `UpdateView`, `DeleteView`, кастомный `View` для детали). Доступ к изменению данных: `UserPassesTestMixin` + `is_authenticated`. Неаутентифицированный пользователь видит список и карточку, кнопки «Добавить / Редактировать / Удалить» скрыты шаблоном.
- **Авторизация:** `AuthView.post` не вызывает `form.is_valid()`; берёт `form.data["email"]` / `password`. При неуспехе шаблон получает `error`.
- **Регистрация:** `RegistrationForm.clean` сравнивает пароли и проверяет уникальность `email`. Сообщение об ошибке в view читается как `form.errors["__all__"].data[0].message` (только non-field errors).
- **Детальная страница:** при отсутствии записи `get()` даст `DoesNotExist` (нет обработки 404). Каждый GET ходит в Tinkoff за свечами.

### REST API

Базовый URL: `/api/v1/shares/` (trailing slash по правилам DRF).

`ShareViewSet(ModelViewSet)`:

- queryset: `Share.objects.all()`;
- serializer: `ShareSerializer`;
- filter backends: `OrderingFilter`, `DjangoFilterBackend`, `SearchFilter`;
- `ShareFilter`: точное совпадение `name`, `ticker`;
- `search_fields = ["$name"]` (regex-поиск DRF);
- `ordering_fields = ["name", "ticker"]`.

Создание/изменение/удаление через API **не** требуют логина. Тесты в `dashboard/tests.py` покрывают list/detail/create/update/delete HTML-списка (только 200) и API, включая невалидные PUT/POST и 404.

### Взаимодействие с БД

- Движок: `django.db.backends.postgresql`, БД `investing` на `localhost:5432`. SQLite в settings закомментирован.
- Все выборки и изменения акций идут через ORM. Сырого SQL нет.
- `add_shares`: `get_or_create` с набором полей FIGI/name/ISIN/ticker/currency/uid. Повторный запуск с изменившимися атрибутами при том же FIGI может не обновить запись либо создать конфликт по unique `ticker`/`uid` — логика идемпотентности ограничена.
- Обновление цен: `Share.objects.filter(id=share.id).update(last_price=..., is_trend_high=...)` — один UPDATE на акцию в цикле (N запросов), без bulk_update. Исключения логируются, задача не падает целиком.
- Сравнение тренда: если `share.last_price` is `None`, сравнение вызывает исключение, тренд принудительно `True`.

### Фоновые процессы и внешние вызовы

Запуск (из README):

1. `docker-compose -f docker-compose.yml up` — Postgres и Redis;
2. `python manage.py add_shares` — загрузка справочника;
3. `celery -A config beat` и `celery -A config worker`;
4. Django runserver в README не указан явно, но это стандартный способ отдать HTTP.

Клиент Tinkoff: `with Client(TINKOFF_TOKEN) as client`. Пустой токен означает, что интеграция неработоспособна до ручной подстановки ключа в `config/settings.py`.

---

## Краткая схема маршрутов и компонентов

```
GET  /                         ShareListView          → Share (read)
GET  /<id>                     ShareDetailView        → Share (read) + Tinkoff candles
POST /create                   ShareCreateView        → Share (insert), auth
POST /update/<id>              ShareUpdateView        → Share (update), auth
POST /delete/<id>              ShareDeleteView        → Share (delete), auth
*    /api/v1/shares[/id/]      ShareViewSet           → Share CRUD, без auth
POST /userlogin/               AuthView               → auth.User (session)
POST /userregistration/        RegistrationView       → auth.User (insert)
GET  /userlogout/              LogoutView             → session clear
     /admin/                   ShareAdmin + User admin
Celery update_last_price       → Share.update + Tinkoff last_prices
manage.py add_shares           → Share.get_or_create + Tinkoff instruments
```

---

## Источники в коде

Анализ опирается на: `config/settings.py`, `config/urls.py`, `config/celery.py`, `dashboard/models.py`, `dashboard/views.py`, `dashboard/urls.py`, `dashboard/forms.py`, `dashboard/tasks.py`, `dashboard/services/*`, `dashboard/api/v1/*`, `dashboard/management/commands/add_shares.py`, `dashboard/admin.py`, `dashboard/tests.py`, `user/views.py`, `user/forms.py`, `user/urls.py`, `user/models.py`, шаблоны `dashboard/` и `user/`, `requirements.txt`, `docker-compose.yml`, `README.md`, миграции `dashboard/migrations/`.
