# Отчёт о работе с GitHub Copilot

## Какие задачи ставились
Задания №1–4 из HOMEWORK.md. Задание №1 частично (ANALYSIS.md был предзаготовлен).

## Основные промпты
- Анализ зависимостей → привёл к плану обновления Django 4.1 → 5.2 LTS
- Baseline-тесты → выявил пустой SECRET_KEY, обошли через settings_test.py
- Обход блокировки tinkoff-investments → SDK из GitHub + requirements-sdk.txt
- 9 фиксов дефектов → каждый отдельным шагом с тестами
- Рефакторинг → compute_trend, bulk_update, идемпотентный add_shares
- E2E → SQLite local, runserver на порту 8001
- Портфель → 4 шага, 10 новых тестов

## Ошибки и проблемы
1. Галлюцинация версий: назвал DRF 3.18.3, фетчил 3.17.1 → поймали pip index versions.
2. Отказ от добавления SECRET_KEY в settings_test.py → мой промпт был слишком узким.
3. Конфликт grpcio 1.51.3 vs SDK (>=1.59.3) → разрешили явно.
4. tinkoff==0.1.1 недоступен на PyPI → SDK из GitHub.
5. force_authenticate не создаёт Django-сессию → заменили на self.client.login в UI-тесте.
6. Порт 8000 занят «чужим» runserver → перешли на 8001.

## Корректировки
- Разбил большие промпты на шаги (проверка после каждого).
- Запретил git-команды в промптах (агент лез в git status/diff без запроса).
- Явно указал, что нельзя трогать tinkoff/protobuf на этапе обновления Django.

## Проверка результатов
- manage.py check после каждого шага
- manage.py test --settings=config.settings_test: 22 → 23 → 26 → 30 → 32 → 33
- black --check
- E2E HTTP smoke через runserver
- Ручная проверка /portfolio/ в браузере (если делал)

## Время и итерации
- Шаг 3.1: ~8 итераций (Python 3.11, SDK, grpcio, requirements-sdk)
- Шаг 3.2: ~5 итераций (9 фиксов)
- Шаг 3.3: ~3 итерации
- Шаг 3.4: ~6 итераций (порт 8000, настройка БД, smoke)
- Шаг 4: ~4 итерации (force_authenticate fix)