# Функциональные требования (Investing Demo) — Agent2

Документ описывает фактическое поведение приложения по исходному коду.

## 1. Просмотр списка акций

FR-1. Система должна отображать главную страницу со списком акций (Share) в виде таблицы (тикер, название, ISIN, текущая цена с валютой, цвет по тренду).
- Подтверждение: `dashboard/views.py` — `ShareListView`; `dashboard/urls.py` path("", name="index"); `dashboard/templates/dashboard/list.html`.
- Ограничения: доступно всем.

FR-2. Система должна разбивать список акций на страницы по 100 записей.
- Подтверждение: `dashboard/views.py` — `ShareListView.paginate_by = 100`.
- Ограничения: параметр `page`.

FR-3. Система должна сортировать список акций по наименованию (name) по возрастанию.
- Подтверждение: `dashboard/views.py` — `ShareListView.ordering = ["name"]`.

FR-4. Система должна показывать элементы управления (добавить/редактировать/удалить) только авторизованным пользователям.
- Подтверждение: `dashboard/templates/dashboard/list.html` — `{% if user.is_authenticated %}`.

## 2. Просмотр детальной страницы

FR-5. Система должна отображать детальную страницу акции по id: название, текущая цена, валюта, время последнего обновления.
- Подтверждение: `dashboard/views.py` — `ShareDetailView.get`; `dashboard/urls.py` path("<int:pk>"); `dashboard/templates/dashboard/detail.html`.
- Ограничения: доступно всем; при несуществующем id — ошибка (см. дефекты).

FR-6. Система должна строить график исторических цен: свечи Tinkoff Invest за 180 дней (интервал "день"), цена закрытия (units) и дата, линейный график Plotly как HTML-div (автоэкранирование отключено).
- Подтверждение: `dashboard/services/graph.py` — `get_graph`; `tinkoff.invest.Client.get_all_candles`.
- Ограничения: требует непустой TINKOFF_TOKEN; синхронный вызов внешнего API.

## 3. CRUD через HTML
## 4. REST API

FR-11. Система должна предоставлять REST API для акций по базовому пути `/api/v1/shares/` с операциями: список (GET), деталь (GET /{id}/), создание (POST), полное обновление (PUT), частичное (PATCH), удаление (DELETE).
- Подтверждение: `dashboard/api/v1/router.py` — `router.register(r"shares", ShareViewSet)`; `dashboard/api/v1/views.py` — `ShareViewSet(viewsets.ModelViewSet)`.
- Ограничения: доступно всем (права по умолчанию AllowAny).

FR-12. Сериализатор акции должен возвращать поля: id, figi, isin, name, ticker, currency, last_price, is_trend_high, updated_at.
- Подтверждение: `dashboard/api/v1/serializer.py` — `ShareSerializer.Meta.fields`.
- Ограничения: uid не включён.

FR-13. Система должна поддерживать фильтрацию API по полям name и ticker.
- Подтверждение: `dashboard/api/v1/views.py` — `ShareFilter` (fields=("name","ticker")), `filterset_class`, `DjangoFilterBackend`.

FR-14. Система должна поддерживать сортировку API по полям name и ticker.
- Подтверждение: `dashboard/api/v1/views.py` — `ordering_fields = ["name", "ticker"]`, `OrderingFilter`.

FR-15. Система должна поддерживать поиск API по полю name (префиксный/полнотекстовый в зависимости от СУБД).
- Подтверждение: `dashboard/api/v1/views.py` — `search_fields = ["$name"]`, `SearchFilter`.

FR-16. Система должна пагинировать ответы API с размером страницы 100 (LimitOffsetPagination).
- Подтверждение: `config/settings.py` — REST_FRAMEWORK DEFAULT_PAGINATION_CLASS, PAGE_SIZE 100.

FR-17. REST API акций должен быть доступен анонимным пользователям (чтение и запись).
- Подтверждение: `dashboard/api/v1/views.py` — отсутствие `permission_classes`; DRF по умолчанию AllowAny.

## 5. Регистрация и аутентификация

FR-18. Система должна предоставлять страницу регистрации по URL `/user/registration/` с формой (email, пароль, повтор пароля).
## 6. Фоновые задачи Celery

FR-23. Система должна периодически (каждые 10 секунд по beat-расписанию) запускать задачу обновления последних цен всех акций.
- Подтверждение: `config/celery.py` — beat_schedule "add-every-5-min", task "dashboard.tasks.update_last_price", schedule 10.0.
- Ограничения: требуется Redis-брокер и Celery worker/beat.

FR-24. Задача обновления должна для каждой акции запросить последнюю цену в Tinkoff Invest и обновить поля last_price и is_trend_high (trend: если предыдущая цена больше новой — False, иначе True; при ошибке — True).
- Подтверждение: `dashboard/tasks.py` — update_last_price; `dashboard/services/market_data.py` — get_last_data возвращает [price.units, time].
- Ограничения: при исключениях ошибка логируется, обновление пропускается.

FR-25. Система должна предоставлять команду управления `add_shares` для первичной загрузки списка акций из Tinkoff Invest (get_or_create).
- Подтверждение: `dashboard/management/commands/add_shares.py` — Command.handle; client.instruments.shares().
- Ограничения: требует непустой TINKOFF_TOKEN.

## 7. Админка и логирование

FR-26. Система должна регистрировать модель Share в Django Admin с отображением figi, isin, name, ticker, currency и поиском по этим полям.
- Подтверждение: `dashboard/admin.py` — ShareAdmin (list_display, search_fields, fields).

FR-27. Система должна логировать получение последней цены для акции (info) через логгер "main".
- Подтверждение: `dashboard/services/market_data.py` — logger.info(...); `config/settings.py` LOGGING.

---

## Выявленные дефекты реализации (НЕ являются требованиями)

- Пустой `SECRET_KEY` в `config/settings.py`.
- Пустой `TINKOFF_TOKEN`.
- REST API открыт для всех (AllowAny).
- `path("user", include(...))` без завершающего слэша.
- `ShareDetailView` использует `Share.objects.get(id=pk)` без `get_object_or_404`.
- `ShareModelForm` с `fields = "__all__"` включает служебные поля.
- Celery Beat: имя "add-every-5-min", но расписание 10 секунд.
- `tasks.update_last_price`: опечатка `detetime`, широкий `except`, проблема при `last_price is None`.
- `market_data.get_last_data` теряет дробную часть цены (units без nano), предполагает непустой список.
- `graph.get_graph` использует `close.units` (теряет точность).
- Миграция 0004 содержит ошибочные verbose_name.
- Отсутствуют исходники `settings_local`/`settings_test` (только pycache).
- Пользовательский модуль: `AuthView.post`/`RegistrationView.post` обращаются к ключам без проверки (KeyError), выход через GET.
- `IsUserAuthenticatedMixin.handle_no_permission` — нестандартная реализация.
- Отсутствие тестов для user, сервисов, Celery, HTML-вьюх.
- Админка не показывает last_price/is_trend_high/updated_at.
- Расхождение версий requirements и установленного окружения.
- `updated_at` не обновляется при `QuerySet.update()` (auto_now срабатывает только при save()).

- Подтверждение: `user/urls.py` path("registration/"); `user/views.py` RegistrationView.get; `user/forms.py` RegistrationForm; template `user/registration.html`.

FR-19. Система должна валидировать при регистрации совпадение паролей и уникальность email.
- Подтверждение: `user/forms.py` — RegistrationForm.clean.

FR-20. Система должна создавать пользователя при успешной регистрации (username=email), выполнять вход и перенаправлять на главную.
- Подтверждение: `user/forms.py` — RegistrationForm.save (User.objects.create_user); `user/views.py` RegistrationView.post (save, login, redirect).

FR-21. Система должна предоставлять страницу входа по URL `/user/login/` и аутентифицировать по email (нижний регистр) и паролю.
- Подтверждение: `user/urls.py` path("login/"); `user/views.py` AuthView.post (authenticate username=form.data["email"].lower()).

FR-22. Система должна предоставлять выход по URL `/user/logout/` (GET), завершающий сессию и перенаправляющий на главную.
- Подтверждение: `user/urls.py` path("logout/"); `user/views.py` LogoutView.get (logout, redirect).


FR-7. Система должна позволять создавать акцию через HTML-форму только авторизованным пользователям.
- Подтверждение: `dashboard/views.py` — `ShareCreateView(IsUserAuthenticatedMixin, CreateView)`, form_class=ShareModelForm, success_url=index; `dashboard/urls.py` path("create").
- Ограничения: неавторизованный перенаправляется на index.

FR-8. Система должна позволять редактировать акцию через HTML-форму только авторизованным пользователям.
- Подтверждение: `dashboard/views.py` — `ShareUpdateView`; `dashboard/urls.py` path("update/<int:pk>").

FR-9. Система должна позволять удалять акцию через HTML-страницу подтверждения только авторизованным пользователям.
- Подтверждение: `dashboard/views.py` — `ShareDeleteView`; `dashboard/urls.py` path("delete/<int:pk>"); template `dashboard/delete.html`.

FR-10. Форма акции (`ShareModelForm`) должна включать все поля модели Share (fields="__all__").
- Подтверждение: `dashboard/forms.py` — `ShareModelForm.Meta.fields = "__all__"`.
- Ограничения: включает служебные поля (см. дефекты).
