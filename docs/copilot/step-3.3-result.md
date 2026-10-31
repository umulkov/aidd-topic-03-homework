# Шаг 3.3 — рефакторинг

| Что | Файл:строка | Зачем |
|---|---|---|
| Логику сравнения вынесено в `compute_trend(prev_price, new_price, ticker=None)`; при отсутствии прежней цены возвращает `None` и пишет прежнее предупреждение с тикером | `dashboard/services/market_data.py:6-15`; вызов из `dashboard/tasks.py:14` | Изолировать вычисление тренда и сохранить поведение шага 3.2 |
| Обновлённые акции накапливаются и записываются через один `bulk_update`; `updated_at` выставляется явно для каждой записи | `dashboard/tasks.py:9-34` | Сократить число UPDATE-запросов, сохранив обновление времени |
| `add_shares` использует `update_or_create` по `figi`, изменяемые поля задаются через `defaults`; unique-конфликт логируется, запись пропускается | `dashboard/management/commands/add_shares.py:12-34` | Повторный запуск обновляет текущие акции; конфликт ticker/uid не останавливает импорт |
| Общий selector не вводился: HTML-список сортирует по `name`, API предоставляет отдельные filter/search и допустимую сортировку по `name`/`ticker`; общей логики фильтрации/ordering нет | `dashboard/views.py:22-28`; `dashboard/api/v1/views.py:16-22` | Не создавать абстракцию для фактически различающегося поведения |

## Проверки

После каждого из четырёх пунктов запускались Django system check и тесты; все прогоны прошли. Итог:

- `manage.py check` — `System check identified no issues (0 silenced)`, exit code 0.
- `manage.py test -v 2 --settings=config.settings_test` — `Ran 22 tests`, `OK`, exit code 0.
- `black --check` по затронутым Python-файлам — успешно.

Для `add_shares` отдельного тестового покрытия в проекте нет; согласно заданию тест на команду не добавлялся. Поведение конфликта уникальности и реальный импорт из Tinkoff API непосредственно не проверялись.
