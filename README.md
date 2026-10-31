# investing

# Переменные окружения

Перед запуском приложения задайте `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`,
`DJANGO_ALLOWED_HOSTS` и `TINKOFF_TOKEN`. Скопируйте `.env.example` в `.env`
и замените примерные значения. Django автоматически не загружает `.env`:
переменные должны быть экспортированы средой запуска.

# PostgreSQL (Docker)
docker-compose -f docker-compose.yml up

# Tinkoff Invest API
# TINKOFF_TOKEN задаётся через окружение

# Установка основных зависимостей и SDK
python -m pip install -r requirements.txt
# SDK требует недоступный в PyPI пакет tinkoff, поэтому ставится без metadata-зависимостей
python -m pip install -r requirements-sdk.txt --no-deps

# Первоначальная загрузка списка акций
python manage.py add_shares

# Celery Beat
celery -A config beat

# Celery Worker
celery -A config worker -l info

# Celery Worker для Windows (Eventlet)
pip install eventlet cryptography
celery -A config worker -l info -P eventlet

# API
# /api/v1/shares — работа с акциями
