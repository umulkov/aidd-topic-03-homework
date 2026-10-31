# Восстановленные функциональные требования

Документ описывает **фактически реализованное** поведение Investing Demo по исходному коду и `ANALYSIS.md`. Предполагаемые и желаемые возможности не включены. Дефекты и неоднозначности вынесены в раздел 5 и **не** являются требованиями.

Маршруты пользователей указаны так, как они собираются в `config/urls.py` (`path("user", include("user.urls"))` без `/`) и `user/urls.py`: `/userlogin/`, `/userregistration/`, `/userlogout/`.

---

## 1. Основные функциональные возможности

Приложение реализует глобальный справочник акций без персональных портфелей и без хранения истории цен в собственной БД.

1. Просмотр списка акций с пагинацией, ценой и цветовой индикацией тренда.
2. Просмотр карточки акции: реквизиты из БД и линейный график дневных цен закрытия за последние 180 дней (данные Tinkoff Invest).
3. Регистрация, вход и выход пользователя (стандартная модель Django `User`, логин = email).
4. Создание, изменение и удаление акций в HTML-интерфейсе только для аутентифицированного пользователя.
5. REST API v1 для полного CRUD коллекции акций с пагинацией, фильтрацией, поиском и сортировкой.
6. Управление акциями в Django Admin.
7. Первичная загрузка списка акций из Tinkoff Invest командой `manage.py add_shares`.
8. Периодическое фоновое обновление последней цены и флага тренда через Celery.

---

## 2. Основные сценарии взаимодействия пользователя с приложением

### С1. Гость просматривает справочник

1. Открывает `/` (`ShareListView`).
2. Видит таблицу акций (тикер, название, ISIN, цена и валюта) или текст «Акций еще нет».
3. При числе записей больше 100 переходит по страницам (`?page=`).
4. По тикеру переходит на `/<id>` (`ShareDetailView`): название, текущая цена, `updated_at`, график.

Кнопок «Добавить / Редактировать / Удалить» нет. В шапке — «Войти».

### С2. Регистрация

1. С страницы входа переходит на `/userregistration/` (`RegistrationView`).
2. Вводит email, пароль и подтверждение пароля.
3. При успехе система создаёт пользователя, выполняет вход и перенаправляет на список акций.
4. При ошибке (несовпадение паролей, занятый email и т.п.) форма показывается снова.

### С3. Вход и выход

1. Гость открывает `/userlogin/` (`AuthView`), вводит email и пароль.
2. При успехе — сессия и редирект на список; в шапке «Привет, {email}» и «Выход».
3. При неуспехе — сообщение «Неверный логин или пароль! Повторите попытку.»
4. «Выход» (`LogoutView`, GET `/userlogout/`) завершает сессию и возвращает на список.

### С4. Аутентифицированный пользователь изменяет справочник

1. На списке нажимает «Добавить», заполняет все поля формы акции, сохраняет → запись в БД, редирект на список.
2. «Редактировать» открывает ту же форму с текущими данными; сохранение обновляет запись.
3. «Удалить» показывает подтверждение с названием; POST удаляет запись и возвращает на список.
4. Неаутентифицированный запрос к create/update/delete перенаправляется на список акций.

### С5. Клиент REST API

Вызывает `/api/v1/shares/` и `/api/v1/shares/{id}/` методами GET/POST/PUT/PATCH/DELETE. Может задавать `limit`/`offset`, фильтры `name`/`ticker`, `search`, `ordering`. Проверка сессии/токена в коде API не задана.

### С6. Оператор (вне браузерного UI справочника)

1. Django Admin `/admin/` — список, поиск и редактирование `Share`.
2. `python manage.py add_shares` — загрузка инструментов Tinkoff в БД.
3. При запущенных Beat и Worker периодически обновляются `last_price` и `is_trend_high`.

---

## 3. Бизнес-правила, проверки и ограничения

### Справочник акций

- Идентификатор записи — автоинкрементный `id`.
- `figi`, `ticker`, `uid` уникальны.
- `ticker` не длиннее 10 символов; `figi`/`isin`/`name`/`uid` — до 255; `currency` — до 20.
- `last_price` и `is_trend_high` необязательны (могут быть пустыми).
- `updated_at` выставляется автоматически при `save()` модели (`auto_now=True`).
- HTML-форма передаёт **все** поля модели, включая `uid`, `last_price`, `is_trend_high`, `updated_at`.
- REST-сериализатор **не** включает `uid`; обязательны как минимум `figi`, `isin`, `name`, `ticker`, `currency` (остальные поля сериализатора допускают пустые значения модели).
- Акция не привязана к пользователю: все видят один справочник.

### Доступ

- Список и карточка доступны без входа.
- HTML create/update/delete: `request.user.is_authenticated`; иначе редирект на `dashboard:index`.
- REST `ShareViewSet` не задаёт `permission_classes` / `authentication_classes` (поведение DRF по умолчанию: операции доступны без учётки).
- Admin — стандартная авторизация staff Django (не кастомизирована в проекте).

### Пользователи

- Регистрация: обязательны email, password1, password2; email — формат `EmailField`.
- Пароли должны совпадать, иначе ошибка «Введенные пароли не совпадают».
- Email не должен уже существовать в `User.email`, иначе сообщение о занятом адресе.
- Пользователь создаётся как `create_user(email, email, password)`: `username` и `email` равны введённому email.
- Вход: `authenticate(username=email.lower(), password=...)`.
- Валидаторы `AUTH_PASSWORD_VALIDATORS` в `config/settings.py` объявлены, но форма регистрации их не вызывает (см. раздел 5).

### Рыночные данные

- Последняя цена для фонового обновления: `get_last_prices` по `figi`, в БД пишется `price.units` (без `nano`).
- Тренд: если прежняя `last_price` строго больше новой — `is_trend_high = False`, иначе `True`; любое исключение при сравнении — `True`, ошибка пишется в логгер `main`.
- Ошибка запроса Tinkoff по одной акции логируется, остальные акции обрабатываются дальше.
- График: дневные свечи (`CANDLE_INTERVAL_DAY`) с `now() - 180 days` по FIGI; ось Y — `candle.close.units`.
- В шаблоне списка при истинном `is_trend_high` ячейка цены зелёная (`mediumseagreen`), иначе красная (`palevioletred`), включая случай `None` (ложно в шаблоне).

### Пагинация и выборки

- HTML-список: 100 записей на страницу, сортировка по `name`.
- API: `LimitOffsetPagination`, `PAGE_SIZE = 100`.
- API-фильтр: точное совпадение `name`, `ticker`.
- API-поиск: `search_fields = ["$name"]` (regex-поиск DRF по имени).
- API-сортировка: поля `name`, `ticker`.

### Первичная загрузка

- `get_or_create` с полями `figi`, `name`, `isin`, `ticker`, `currency`, `uid` из `client.instruments.shares()`.

### Расписание фона

- Celery Beat вызывает `dashboard.tasks.update_last_price` с `schedule: 10.0` (интервал 10 секунд).

---

## 4. Функциональные требования

Каждый пункт — наблюдаемое поведение системы с подтверждением в коде.

1. Система отображает на главной странице `/` список всех акций из БД, упорядоченный по полю `name`, с разбиением по 100 записей на страницу.  
   **Код:** `dashboard/views.py` — `ShareListView`; `dashboard/urls.py` — `path("", ..., name="index")`; `dashboard/templates/dashboard/list.html`.

2. Если акций нет, система показывает текст «Акций еще нет».  
   **Код:** `dashboard/templates/dashboard/list.html` (ветка `{% else %}`).

3. В строке списка система показывает тикер (ссылка на карточку), наименование, ISIN, последнюю цену и валюту.  
   **Код:** `dashboard/templates/dashboard/list.html`.

4. Если у акции `is_trend_high` истинно, ячейка цены отображается зелёным фоном, иначе красным.  
   **Код:** `dashboard/templates/dashboard/list.html` (`share.is_trend_high`).

5. Система предоставляет навигацию по страницам списка через параметр `page` (предыдущая, следующая, номера страниц).  
   **Код:** `dashboard/templates/dashboard/list.html` (`page_obj`).

6. По запросу `GET /<pk>` система загружает акцию с `id=pk` и отображает наименование, `last_price`, валюту и `updated_at`.  
   **Код:** `dashboard/views.py` — `ShareDetailView.get`; `dashboard/templates/dashboard/detail.html`.

7. На карточке акции система строит линейный график Plotly по дневным ценам закрытия за последние 180 дней, полученным из Tinkoff Invest по FIGI акции.  
   **Код:** `dashboard/services/graph.py` — `get_graph`; `dashboard/views.py` — `ShareDetailView.get`; `dashboard/templates/dashboard/detail.html`.

8. Неаутентифицированному пользователю система показывает в шапке кнопку «Войти» на маршрут `user:auth`; аутентифицированному — приветствие с `user.email` и кнопку «Выход» на `user:logout`.  
   **Код:** `dashboard/templates/dashboard/base.html`.

9. Аутентифицированному пользователю на списке система показывает кнопку «Добавить» и в каждой строке кнопки «Редактировать» и «Удалить»; гостю эти элементы не показывает.  
   **Код:** `dashboard/templates/dashboard/list.html` (`user.is_authenticated`).

10. Система принимает `GET` и `POST` `/create` для создания акции через форму со всеми полями модели `Share` и после успешного сохранения перенаправляет на список.  
    **Код:** `dashboard/views.py` — `ShareCreateView`; `dashboard/forms.py` — `ShareModelForm`; `dashboard/templates/dashboard/create.html`.

11. Система принимает `GET` и `POST` `/update/<pk>` для изменения существующей акции той же формой и после успеха перенаправляет на список.  
    **Код:** `dashboard/views.py` — `ShareUpdateView`; `dashboard/forms.py` — `ShareModelForm`.

12. Система принимает `GET` `/delete/<pk>` с подтверждением («Вы уверены…» и имя акции) и `POST` для удаления записи с последующим редиректом на список.  
    **Код:** `dashboard/views.py` — `ShareDeleteView`; `dashboard/templates/dashboard/delete.html`.

13. Если пользователь не аутентифицирован, система не выполняет create/update/delete в HTML и перенаправляет его на `dashboard:index`.  
    **Код:** `dashboard/views.py` — `IsUserAuthenticatedMixin.test_func`, `IsUserAuthenticatedMixin.handle_no_permission`.

14. Система сохраняет акцию с уникальными `figi`, `ticker` и `uid`; длина `ticker` ограничена 10 символами.  
    **Код:** `dashboard/models.py` — класс `Share`.

15. Система допускает пустые `last_price` и `is_trend_high` при сохранении модели.  
    **Код:** `dashboard/models.py` — поля `last_price`, `is_trend_high`.

16. При `save()` модели система обновляет `updated_at` текущим временем.  
    **Код:** `dashboard/models.py` — поле `updated_at` (`auto_now=True`).

17. Система отображает форму входа по `GET /userlogin/` с полями email и пароль и ссылкой на регистрацию.  
    **Код:** `user/views.py` — `AuthView.get`; `user/forms.py` — `AuthForm`; `user/templates/user/auth.html`; `user/urls.py` — `path("login/", ...)`.

18. По `POST /userlogin/` система аутентифицирует пользователя по `username`, равному email в нижнем регистре, и паролю; при успехе создаёт сессию и перенаправляет на список акций.  
    **Код:** `user/views.py` — `AuthView.post` (`authenticate`, `login`).

19. Если аутентификация неуспешна, система повторно показывает форму входа с текстом «Неверный логин или пароль! Повторите попытку.»  
    **Код:** `user/views.py` — `AuthView.post`.

20. Система отображает форму регистрации по `GET /userregistration/` (email, пароль, повтор пароля) и ссылкой на вход.  
    **Код:** `user/views.py` — `RegistrationView.get`; `user/forms.py` — `RegistrationForm`; `user/templates/user/registration.html`.

21. При регистрации система требует заполнения email, пароля и подтверждения пароля; email должен быть корректного формата.  
    **Код:** `user/forms.py` — `RegistrationForm` (`required=True`, `EmailField`).

22. Если пароль и подтверждение не совпадают, система отклоняет регистрацию с сообщением «Введенные пароли не совпадают».  
    **Код:** `user/forms.py` — `RegistrationForm.clean`.

23. Если в БД уже есть пользователь с тем же `email`, система отклоняет регистрацию с сообщением о том, что e-mail уже зарегистрирован.  
    **Код:** `user/forms.py` — `RegistrationForm.clean` (`User.objects.filter(email=email)`).

24. При успешной регистрации система создаёт пользователя с `username` и `email`, равными введённому email, хеширует пароль, выполняет вход и перенаправляет на список акций.  
    **Код:** `user/forms.py` — `RegistrationForm.save`; `user/views.py` — `RegistrationView.post`.

25. По `GET /userlogout/` система завершает сессию и перенаправляет на список акций.  
    **Код:** `user/views.py` — `LogoutView.get`.

26. Система предоставляет REST-коллекцию акций по префиксу `/api/v1/shares/` через `DefaultRouter` и `ShareViewSet`.  
    **Код:** `dashboard/urls.py`; `dashboard/api/urls.py`; `dashboard/api/v1/urls.py`; `dashboard/api/v1/router.py` — `router.register(r"shares", ShareViewSet)`.

27. По `GET /api/v1/shares/` система возвращает список акций с пагинацией Limit/Offset и размером страницы 100.  
    **Код:** `dashboard/api/v1/views.py` — `ShareViewSet`; `config/settings.py` — `REST_FRAMEWORK`; `dashboard/tests.py` — `DashboardTests.test_share_list`.

28. По `GET /api/v1/shares/{id}/` система возвращает одну акцию; при отсутствии записи — HTTP 404.  
    **Код:** `dashboard/api/v1/views.py` — `ShareViewSet`; `dashboard/tests.py` — `test_share_detail`, `test_share_detail_invalid`.

29. По `POST /api/v1/shares/` система создаёт акцию и отвечает HTTP 201; неполный набор полей даёт HTTP 400.  
    **Код:** `dashboard/api/v1/views.py` — `ShareViewSet`; `dashboard/api/v1/serializer.py` — `ShareSerializer`; `dashboard/tests.py` — `test_share_create`, `test_share_create_invalid`.

30. По `PUT /api/v1/shares/{id}/` система полностью обновляет сериализуемые поля акции (HTTP 200); неполный PUT даёт HTTP 400.  
    **Код:** `dashboard/api/v1/views.py` — `ShareViewSet` (ModelViewSet); `dashboard/tests.py` — `test_share_update`, `test_share_update_invalid`.

31. По `DELETE /api/v1/shares/{id}/` система удаляет акцию и отвечает HTTP 204; для несуществующего id — HTTP 404.  
    **Код:** `dashboard/api/v1/views.py` — `ShareViewSet`; `dashboard/tests.py` — `test_share_delete`, `test_share_delete_invalid`.

32. В теле API система отдаёт и принимает поля `id`, `figi`, `isin`, `name`, `ticker`, `currency`, `last_price`, `is_trend_high`, `updated_at` и не включает `uid`.  
    **Код:** `dashboard/api/v1/serializer.py` — `ShareSerializer.Meta.fields`.

33. Система позволяет фильтровать список API по точному значению `name` и `ticker`.  
    **Код:** `dashboard/api/v1/views.py` — `ShareFilter`.

34. Система позволяет искать акции в API по полю `name` в режиме regex-поиска DRF (`$name`) и сортировать по `name` и `ticker`.  
    **Код:** `dashboard/api/v1/views.py` — `ShareViewSet.search_fields`, `ShareViewSet.ordering_fields`.

35. HTML-список по `GET /` доступен без аутентификации и возвращает HTTP 200.  
    **Код:** `dashboard/views.py` — `ShareListView` (без mixin доступа); `dashboard/tests.py` — `test_share_list_html`.

36. В Django Admin система регистрирует модель `Share` со списком колонок figi/isin/name/ticker/currency, поиском по этим полям и формой, включающей `uid`, `last_price`, `is_trend_high`.  
    **Код:** `dashboard/admin.py` — `ShareAdmin`; `config/urls.py` — `path("admin/", ...)`.

37. Команда `python manage.py add_shares` запрашивает список акций Tinkoff (`instruments.shares`) и создаёт записи `Share` через `get_or_create` с полями figi, name, isin, ticker, currency, uid.  
    **Код:** `dashboard/management/commands/add_shares.py` — `Command.handle`.

38. Задача `update_last_price` для каждой акции запрашивает последнюю цену Tinkoff по FIGI и записывает в БД `last_price` равным `price.units`.  
    **Код:** `dashboard/tasks.py` — `update_last_price`; `dashboard/services/market_data.py` — `get_last_data`.

39. При обновлении цены система выставляет `is_trend_high=False`, если сохранённая цена строго больше новой, иначе `True`; при исключении сравнения выставляет `True` и пишет ошибку в лог.  
    **Код:** `dashboard/tasks.py` — `update_last_price`.

40. Если запрос цены по одной акции завершается исключением, система логирует ошибку и продолжает обработку остальных акций.  
    **Код:** `dashboard/tasks.py` — внешний `try/except` в цикле.

41. Планировщик Celery Beat запускает `dashboard.tasks.update_last_price` каждые 10 секунд.  
    **Код:** `config/celery.py` — `app.conf.beat_schedule["add-every-5-min"]` (`schedule: 10.0`).

---

## 5. Неоднозначности, противоречия и возможные дефекты реализации

Нижеследующее **не** является функциональными требованиями.

### Особенности реализации (не требования)

1. **Вставка HTML графика без экранирования.** `get_graph` возвращает HTML-фрагмент Plotly; шаблон карточки выводит его через `{% autoescape off %}`. Это способ отрисовки виджета, а не отдельное пользовательское поведение. Сырой HTML на странице увеличивает риск XSS, если фрагмент окажется скомпрометирован.  
   **Код:** `dashboard/templates/dashboard/detail.html`; `dashboard/services/graph.py` — `get_graph`.

2. **CSRF-токены.** Мутирующие HTML-формы содержат `{% csrf_token %}`; в `MIDDLEWARE` включён `CsrfViewMiddleware`. Это механизм защиты запросов, а не функциональная возможность справочника.  
   **Код:** `config/settings.py` — `MIDDLEWARE`; `dashboard/templates/dashboard/create.html`, `delete.html`; `user/templates/user/auth.html`, `registration.html`.

### Неоднозначности

1. **Интервал обновления цен.** Ключ расписания назван `add-every-5-min`, фактически `schedule: 10.0` секунд (`config/celery.py`). Намерение (5 минут vs 10 секунд) по коду однозначно не восстанавливается; реализован интервал 10 секунд (требование 41).

2. **Смысл `updated_at` на карточке.** Поле с `auto_now=True` обновляется при `save()` модели, но фоновая задача пишет цену через `QuerySet.update()`, которое `auto_now` не триггерит. На карточке подпись «Время последнего обновления» может не совпадать со временем последней котировки. Какое время задумано — не зафиксировано.

3. **Политика доступа к REST API.** `ShareViewSet` не задаёт права. Это фактическое открытое CRUD-API (требования 26–31), но намерение (публичный API vs забытая авторизация) из кода не следует.

4. **Политика паролей.** В settings заданы стандартные `AUTH_PASSWORD_VALIDATORS`, но `RegistrationForm` их не использует. Неясно, должны ли пароли проверяться на длину/простоту при регистрации.

5. **Идемпотентность `add_shares`.** `get_or_create` передаёт все поля как критерии поиска. Повторный запуск при изменении name/ticker у того же FIGI может создать конфликт уникальности или дубликат логики. Ожидаемое поведение повторного запуска однозначно не специфицировано.

6. **Частичное обновление API.** ModelViewSet поддерживает PATCH, но тесты покрывают только PUT. Поведение PATCH следует из DRF, отдельных правил в проекте нет.

7. **Маршруты `/userlogin/` и т.д.** Склейка `path("user", ...)` без `/` выглядит как ошибка, но это и есть фактические URL именованных маршрутов. Было ли задумано `/user/login/` — неоднозначность.

### Противоречия

1. Комментарий/имя Beat «каждые 5 минут» противоречит `schedule: 10.0`.
2. HTML-форма и админка работают с `uid`; REST-сериализатор `uid` не отдаёт и не принимает — разные контракты одной сущности.
3. Вход приводит email к `.lower()`, регистрация сохраняет email как введён. Учётные записи с заглавными буквами в email могут не входить.
4. Заголовок шаблона `create.html` всегда «Добавить инструмент», хотя тот же шаблон используется `ShareUpdateView`.
5. Docstring `ShareDeleteView` — «Удаление задачи», фактически удаляется акция.

### Возможные дефекты реализации

1. `AuthView.post` не вызывает `form.is_valid()` и читает `form.data["email"]` / `["password"]`: отсутствие полей даёт исключение, а не сообщение валидации (`user/views.py`).
2. `RegistrationView.post` при ошибках без `__all__` обращается к `form.errors["__all__"].data[0].message` — риск `KeyError` на ошибках полей (`user/views.py`).
3. `RegistrationForm.clean` читает `self.cleaned_data["email"]` без `.get()`: при невалидном email возможен `KeyError` (`user/forms.py`).
4. `ShareDetailView.get` использует `Share.objects.get(id=pk)` без обработки `DoesNotExist` — необработанное исключение вместо 404 (`dashboard/views.py`).
5. `IsUserAuthenticatedMixin.handle_no_permission` объявлен как `@staticmethod` и уводит на главную, а не на форму входа (`dashboard/views.py`).
6. В `last_price` и в график попадает только целая часть котировки Tinkoff (`units`), дробная `nano` отбрасывается (`market_data.py`, `graph.py`).
7. Сравнение тренда падает, если `last_price` is `None`; тогда тренд всегда `True` (`tasks.py`).
8. `SECRET_KEY` и `TINKOFF_TOKEN` пустые: без ручной настройки вход Django и вызовы Tinkoff неработоспособны (`config/settings.py`).
9. Шаблоны ссылаются на `bootstrap.min.css` в static-каталогах приложений; в репозитории этих файлов нет — вёрстка может отображаться без Bootstrap.
10. В `docker-compose.yml` том `./:/app` монтируется в контейнер Postgres и не выделен volume данных БД; версия образа `postgres` не зафиксирована.
11. `RegistrationForm.save` вызывает `authenticate` сразу после `create_user` и может вернуть `None`, после чего `login(request, user)` в view получит не-пользователя (краевой случай).
12. Длина тикера в тесте создания API (`TESTTEST`, 8 символов) укладывается в `max_length=10`; более длинные тикеры из Tinkoff при `add_shares` могут нарушить ограничение модели.

---

## Источники

Исходный код: `config/settings.py`, `config/urls.py`, `config/celery.py`, `dashboard/*`, `user/*`, `dashboard/tests.py`, шаблоны приложений. Контекст: `ANALYSIS.md`. Исходный код и `ANALYSIS.md` при подготовке документа не изменялись.
