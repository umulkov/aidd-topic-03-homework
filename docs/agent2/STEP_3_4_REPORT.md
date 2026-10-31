# Отчет E2E / Шаг 3.4 (Agent2)

## Окружение
- Python 3.11.9, venv `.venv311`.
- БД: SQLite (`config/settings_local.py`, файл `db.sqlite3`).
- Миграции применены успешно.
- Суперпользователь: `admin@example.com` / `admin` (username=email).

## Smoke-тесты HTTP
- GET `/` -> 200
- GET `/api/v1/shares/` -> 200
- GET `/user/login/` -> 200
- GET `/999999` -> 404
- POST `/api/v1/shares/` (анонимно) -> 403

## E2E CRUD (через сессию)
- Логин: POST `/user/login/` -> 302 (редирект на `/`), сессия установлена.
- Создание: POST `/create` -> 302, запись появилась в БД (figi=TESTFIGI123, ticker=TST).
- Деталь: GET `/1` -> 200 (график не построен из-за недоступности Tinkoff API, но страница открылась).
- Обновление: POST `/update/1` -> 302, имя изменено на "Updated Company".
- Удаление: POST `/delete/1` -> 302, запись удалена (count=0).

## Фоновые задачи
- Redis недоступен в среде, поэтому Celery worker/beat не запускались.
- Задача `update_last_price` вызвана синхронно в shell: не упала (исключение при запросе к Tinkoff API перехвачено и залогировано).
- TINKOFF_TOKEN не задан/сеть недоступна: реальный запрос к Tinkoff API не проверялся; код устойчив к ошибкам.

## Не проверено
- Реальный вызов Tinkoff Invest API (токен/сеть/SSL).
- Celery Beat/Worker с Redis.
- Конкурентная нагрузка.

## Остановка процессов
- runserver остановлен.
