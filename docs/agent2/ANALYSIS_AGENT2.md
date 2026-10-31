# Анализ проекта Investing Demo (Agent2)

## 1. Назначение приложения и технологический стек

**Investing Demo** — веб-приложение для отслеживания акций/инструментов (тикеров): просмотр списка, карточка инструмента с историческим графиком цен и текущей ценой, CRUD-управление инструментами, автоматическое обновление последних цен и тренда через внешний API Tinkoff Invest.

**Стек:**
- Backend: Django 4.1.7 (в текущем окружении фактически установлен Django 5.2.18), Python 3.11.
- API: Django REST Framework 3.14.0 (в окружении 3.18.3), django-filter 22.1.
- Фоновые задачи: Celery 5.2.7 (в окружении 5.6.3), брокер Redis 4.5.1 (в окружении 5.2.2), Celery Beat.
- БД: PostgreSQL 2.9.5 (psycopg2-binary), по умолчанию `investing` на localhost:5432.
- Внешний API: Tinkoff Invest (`tinkoff-investments==0.2.0b50`, в окружении b117).
- UI: Django Templates, crispy-forms 2.0 + crispy-bootstrap3 2022.1, Bootstrap 3, Plotly 5.13.1.

Приложение содержит две Django-аппа: `dashboard` и `user`. Управление через `manage.py`, WSGI/ASGI, Celery-приложение в `config/celery.py`.

## 2. Структура проекта и назначение компонентов

- `config/` — настройки, urls, celery, wsgi/asgi.
- `dashboard/` — доменная аппа "акции": модели, views, urls, forms, admin, tasks, services, api, management command, tests, templates, migrations.
- `user/` — аутентификация/регистрация.
- `docs/` — логи/документация.
- `docker-compose.yml` — PostgreSQL + Redis.

## 3. Архитектура и взаимодействие компонентов
## 4. Используемые библиотеки (включая устаревшие)

Из `requirements.txt` и фактически установленные в `.venv311`:

| Библиотека | requirements | установлено | Примечание |
|---|---|---|---|
| Django | 4.1.7 | 5.2.18 | Устаревшая зафиксированная версия; окружение новее |
| djangorestframework | 3.14.0 | 3.18.3 | Расхождение версий |
| celery | 5.2.7 | 5.6.3 | Расхождение версий |
| tinkoff-investments | 0.2.0b50 | 0.2.0b117 | Beta-SDK |
| psycopg2-binary | 2.9.5 | — | Драйвер PostgreSQL |
| redis | 4.5.1 | 5.2.2 | Расхождение версий |
| plotly | 5.13.1 | — | Визуализация |
| django-crispy-forms | 2.0 | 2.3+ | UI-формы |
| crispy-bootstrap3 | 2022.1 | — | Bootstrap 3 шаблоны (устаревший UI) |
| django-filter | 22.1 | — | Фильтрация API |
| asgiref | 3.6.0 | 3.8+ | ASGI |

Вывод: проект ориентирован на стек 2022–2023 гг.; зафиксированные версии устарели, окружение новее, совместимость не гарантируется. Tinkoff SDK beta.

## 5. Модель данных

Сущность `Share` (таблица `dashboard_share`):

| Поле | Тип | Ограничения/описание |
|---|---|---|
| id | BigAutoField | PK |
| figi | CharField(255) | unique |
| isin | CharField(255) | — |
| name | CharField(255) | verbose_name "Наименование компании" |
| ticker | CharField(10) | unique, verbose_name "Тикер" |
| currency | CharField(20) | verbose_name "Валюта" |
| uid | CharField(255) | unique |
| last_price | FloatField | blank/null, verbose_name "Текущая цена" |
| is_trend_high | BooleanField | blank/null, verbose_name "Растет цена" |
| updated_at | DateTimeField | auto_now, blank/null |

Meta: verbose_name "Акция", verbose_name_plural "Акции". Связей нет. Пользователи — стандартная модель Django. Миграции 0001–0007.
## 7. Выявленные дефекты и странности

1. Пустой `SECRET_KEY` в `config/settings.py` — небезопасно.
2. Пустой `TINKOFF_TOKEN` — вызовы Tinkoff API завершатся ошибкой.
3. Отсутствие прав в API: `ShareViewSet` без `permission_classes`/`authentication_classes` → доступ всем (AllowAny).
4. Маршрутизация: `path("user", include(...))` без завершающего слэша; dashboard монтируется в корень.
5. `ShareDetailView` использует `Share.objects.get(id=pk)` без `get_object_or_404` → 500 вместо 404.
6. `ShareModelForm` с `fields = "__all__"` включает служебные поля (`id`, `uid`, `last_price`, `is_trend_high`, `updated_at`).
7. Celery Beat: имя "add-every-5-min", но `schedule: 10.0` секунд — рассинхронизация и перегрузка.
8. `tasks.update_last_price`: опечатка `detetime`, широкий `except`, тренд при `last_price is None`, `is_trend_high` может быть неопределён.
9. `services.market_data.get_last_data`: берёт только `units` (теряет `nano`); предполагает непустой `last_prices`.
10. `services.graph.get_graph`: использует `candle.close.units` (теряет точность), токен пустой.
11. Миграция 0004 содержит ошибочные verbose_name (`name` → "Валюта", `ticker` → "Ти").
12. Отсутствующие исходники `settings_local`/`settings_test` (есть только в `__pycache__`) — тесты не запускаются без внешней БД/Redis.
13. Пользовательский модуль: `AuthView.post` обращается к `form.data["email"]` без валидации (KeyError); `RegistrationView.post` обращается к `form.errors["__all__"]` (KeyError); выход через GET.
14. `IsUserAuthenticatedMixin.handle_no_permission` — статический метод, возвращающий redirect (нестандартно).
15. Отсутствие тестов для `user`, сервисов, Celery-задач, HTML-вьюх.
16. Админка: `list_display` не включает `last_price`, `is_trend_high`, `updated_at`.
17. Расхождение версий: requirements фиксирует старые версии, окружение новее; `manage.py check` проходит, 10 тестов проходят на SQLite.

## Краткое резюме

Проект — небольшое Django-приложение для мониторинга акций с интеграцией Tinkoff Invest API, PostgreSQL, Celery/Redis и DRF API. Основная сущность — `Share`. Выявлены проблемы безопасности (пустой `SECRET_KEY`, открытый API), конфигурации (пустой токен, отсутствие тестовых настроек), ошибки в бизнес-логике и миграциях, устаревший стек. Текущие 10 API-тестов проходят на SQLite (Django 5.2). Код на данном этапе не изменялся.


## 6. Механизмы обработки запросов и работы с БД

- ORM Django, QuerySet `all/get/filter/update/get_or_create`.
- HTML: CBV (ListView пагинация 100, сортировка по name; DetailView; Create/Update/Delete с UserPassesTestMixin).
- API: DRF ModelViewSet, LimitOffsetPagination (PAGE_SIZE 100), DjangoFilterBackend, OrderingFilter, SearchFilter.
- Формы: ModelForm с `fields = "__all__"`.
- БД по умолчанию PostgreSQL; для тестов использована временная SQLite (10 тестов: OK).
- Фон: Celery, beat 10 сек. Логирование: логгер `main`, консоль + `app.logs`.


Потоки данных:
1. Браузер → Django (HTML): `config/urls` → `dashboard.urls`/`user.urls`; ListView/DetailView/CRUD; DetailView вызывает `services.graph.get_graph` → Tinkoff API → Plotly.
2. Клиент → REST API: `/api/v1/shares/` → `ShareViewSet` → `ShareSerializer` → ORM → БД.
3. Фон: Celery Beat (10 сек) → `tasks.update_last_price` → `services.market_data.get_last_data` → Tinkoff API → обновление `Share`.
4. Инициализация: `manage.py add_shares` → Tinkoff `instruments.shares()` → `Share.objects.get_or_create`.
5. Админка: `/admin/` для `Share`.

Внешние зависимости: Tinkoff Invest API (токен из settings), PostgreSQL, Redis.
