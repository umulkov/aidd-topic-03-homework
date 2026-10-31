# Шаг 3.4 — E2E и smoke-проверки

## Окружение и база данных

| Компонент | Результат |
|---|---|
| Docker / Compose | Не установлены: `docker` не распознан PowerShell |
| Локальный PostgreSQL | `psql` не найден; служб с именем postgres нет |
| Redis | `redis-server` не найден; `127.0.0.1:6379` недоступен |
| Tinkoff token | Переменная `TINKOFF_TOKEN` не задана; значение секрета не выводилось |
| E2E БД | SQLite, файл `db_e2e.sqlite3`, через добавленный `config/settings_local.py` |

`manage.py migrate --settings=config.settings_local` завершился успешно, миграции применены. Локальный суперпользователь `admin@example.com` создан и проверен запросом ORM.

Порт `127.0.0.1:8000` уже слушал runserver из другого каталога (`C:\UwU\Ai-driven\...`), поэтому его процесс не останавливался и его ответы не засчитывались. Проверки приложения выполнены нашим runserver на `127.0.0.1:8001`; PID 5848 после проверки остановлен, слушатель порта закрыт.

## Smoke HTTP

| URL | Метод | Ожидание | Факт | Результат |
|---|---|---:|---|---|
| `/` | GET | 200 | 200, HTML | PASS |
| `/api/v1/shares/` | GET | 200 JSON | 200, `application/json` | PASS |
| `/user/login/` | GET | 200 | 200, HTML | PASS |
| `/user/registration/` | GET | 200 | 200, HTML | PASS |
| `/999999/` | GET | 404 | 404 | PASS |
| `/api/v1/shares/` | POST `{}` без cookies | 401/403 | 403 | PASS |
| `/user/login/` | POST неверный пароль | 200 с ошибкой HTML | 200, HTML | PASS |

Итого: 7/7 smoke-запросов прошли. Серверный лог содержит ответы этих запросов; traceback не обнаружен.

## CRUD E2E с сессией

- Вход с `admin@example.com` / локальным тестовым паролем: 302.
- POST `/create`: 302; ORM подтвердил создание акции `E2E01`, id `1`.
- Первоначальный GET `/1/`: **404**. Маршрут детали объявлен без завершающего `/`, фактический путь — `/1`.
- POST `/update/1` (существующий slashless-маршрут): 302; ORM подтвердил `name=Renamed`.
- POST `/delete/1` (существующий slashless-маршрут): 302; ORM подтвердил отсутствие записи.

Итого на момент прогона: создание, обновление и удаление подтверждены; detail URL со слэшем возвращал 404. Последующее исправление страницы при недоступности Tinkoff описано ниже.

## Последующее исправление ошибки detail-view

После этого прогона установлено, что runtime `HTTP_PROXY`/`HTTPS_PROXY` указывают на `127.0.0.1:10809`, а Tinkoff SDK возвращает `RequestError` из-за self-signed сертификата в цепочке. Даже прямая проверка TLS без прокси завершилась `CERTIFICATE_VERIFY_FAILED`; проверку сертификатов не отключали. При пустом `TINKOFF_TOKEN` живой график также недоступен.

- `dashboard/views.py` обрабатывает SDK `RequestError`, журналирует ошибку и всё равно рендерит карточку акции.
- `dashboard/templates/dashboard/detail.html` показывает безопасное сообщение о временно недоступном графике вместо debug traceback.
- Регрессионный тест `test_share_detail_renders_when_tinkoff_graph_is_unavailable` проходит.
- Реальный GET `/2` на локальном сервере после фикса вернул **200**, показал fallback-сообщение; traceback отсутствует.
- Поэтому карточка теперь открывается, но реальные исторические данные/график остаются непроверенными и недоступны, пока TLS-прокси не будет настроен с доверенным CA и не будет задан действительный `TINKOFF_TOKEN`.

## Tinkoff и Celery

- `add_shares`: **не проверен — нет `TINKOFF_TOKEN`**.
- Redis недоступен, поэтому Celery worker и Beat не запускались; задача расписания Beat не проверена.
- Вместо worker выполнен синхронный вызов `update_last_price()` с локальной БД после удаления E2E-записи. Результат: `sync ok`; пустая БД не вызывает ошибку. Это не проверяет обработку рыночных данных.

## Финальные проверки и логи

- `manage.py check --settings=config.settings_local` — без ошибок, exit code 0.
- `manage.py test -v 2 --settings=config.settings_test` — `Ran 22 tests`, `OK`, exit code 0.
- Фоновые процессы, запущенные для этой проверки, остановлены. Чужой процесс на порту 8000 не затрагивался.
- `docs/copilot/runserver.log` и `docs/copilot/runserver.err.log` — логи runserver; в stderr есть две строки `Broken pipe` после обработки клиентом redirect-ответов 302, но traceback нет.
- `docs/copilot/celery-worker.log`, `docs/copilot/celery-worker.err.log`, `docs/copilot/celery-beat.log`, `docs/copilot/celery-beat.err.log` не созданы: worker/Beat не запускались из-за отсутствия Redis.

Непроверенными остаются PostgreSQL, Redis-backed worker/Beat, `add_shares` и получение графика через реальный Tinkoff API. Маршрут detail-view остаётся slashless, например `/2`.
