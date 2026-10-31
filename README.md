# investing

# PostgreSQL (Docker)
docker-compose -f docker-compose.yml up

# Tinkoff Invest API
# TINKOFF_TOKEN указывается в config/settings.py

# Первоначальная загрузка списка акций

# Установка Tinkoff SDK (сломанные метаданные на PyPI)
pip install -r requirements-sdk.txt --no-deps

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
