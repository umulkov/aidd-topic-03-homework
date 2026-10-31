# Шаг 3.2 — исправление дефектов

| Дефект | Файл:строка | Было → стало | Тест |
|---|---|---|---|
| URL пользователя склеивался с префиксом | `config/urls.py:7`, `user/urls.py:8`, шаблоны `dashboard/base.html:42`, `user/auth.html:3,19`, `user/registration.html:23` | `user` → `user/`; маршрут входа `auth` → `login`; ссылки на вход строятся через `{% url 'user:login' %}` | `test_user_urls_have_trailing_slash` |
| Анонимный пользователь перенаправлялся на главную | `dashboard/views.py:16-19` | `@staticmethod` и редирект на `dashboard:index` → метод экземпляра с `redirect_to_login(..., reverse_lazy("user:login"))` | `test_share_create_redirects_anonymous_user_to_login` |
| Детальная страница выбрасывала `DoesNotExist` | `dashboard/views.py:34` | `Share.objects.get(id=pk)` → `get_object_or_404(Share, id=pk)` | `test_share_page_detail_missing_returns_404` |
| API разрешал анонимные изменения | `config/settings.py:41-43`; `dashboard/tests.py:157-237` | добавлен `IsAuthenticatedOrReadOnly`; API write-тесты аутентифицируют пользователя, GET-тесты остаются анонимными | `test_share_create_requires_authentication` и CRUD-тесты |
| Настройки не читали переменные окружения | `config/settings.py:1,7-14,143`; `.env.example:1-4`; `README.md:3-8` | добавлено чтение `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`, `TINKOFF_TOKEN`; приведены пример и инструкция | проверены `manage.py check`, тесты и отдельное чтение settings с тестовыми env |
| Терялась дробная часть цены | `dashboard/services/market_data.py:11`, `dashboard/services/graph.py:20` | цена вычисляется как `units + nano / 1_000_000_000`; `Share.last_price` уже является `FloatField`, модель не менялась | `test_last_price_keeps_fractional_part`, `test_graph_keeps_fractional_candle_price`, `test_last_price_float_field_preserves_fractional_value` |
| При неизвестной предыдущей цене тренд ошибочно считался растущим | `dashboard/tasks.py:16-21` | при `last_price is None` логируется предупреждение, `is_trend_high` остаётся `None`; тренд неизвестен, поэтому не подменяется предположением | `test_price_task_skips_trend_when_previous_price_is_missing` |
| `QuerySet.update()` не обновлял `updated_at` | `dashboard/tasks.py:25-28` | в update добавлено `updated_at=timezone.now()` | `test_price_task_updates_updated_at` |
| Имя Beat не совпадало с периодом | `config/celery.py:14-16` | `add-every-5-min` → `update-last-price-every-10s`; интервал `10.0` секунд сохранён | `test_celery_schedule_name_matches_interval` |

В API-тестах изменение/создание/удаление выполняется аутентифицированным пользователем; чтение списка и деталей остаётся доступным анонимно. Решение для отсутствующей предыдущей цены — `None`, поскольку тренд нельзя достоверно определить.

## Проверки

После каждого этапа выполнялись `manage.py check` и `manage.py test -v 2 --settings=config.settings_test`; каждый завершился успешно. Число тестов росло по этапам: 11, 12, 13, 14, 14, 17, 18, 19, 20.

Финальный прогон:

- `manage.py check` — `System check identified no issues (0 silenced)`, exit code 0.
- `manage.py test -v 2 --settings=config.settings_test` — `Ran 20 tests`, `OK`, exit code 0.
- Black `--check` на изменённых Python-файлах — успешно.
- Новых миграций не требуется: `dashboard/models.py` не менялся, `last_price` уже `FloatField`.

## Что не проверено / требуется для запуска

- Реальный Tinkoff API не вызывался; нужен рабочий `TINKOFF_TOKEN`.
- Celery Worker/Beat с Redis и runserver E2E не запускались.
- Тесты прогнаны на SQLite через `config.settings_test`, не на PostgreSQL.
- Для обычного запуска требуется задать `DJANGO_SECRET_KEY`; без переменной значение остаётся пустым. `.env.example` — шаблон, Django сам файл `.env` не загружает.
- Изменение DRF намеренно требует аутентификации для API-записи; клиентам API, создающим или меняющим данные, нужно аутентифицироваться.
