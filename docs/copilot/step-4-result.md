# Задание №4 — виртуальный инвестиционный портфель

## Модели и связи

| Модель | Поля и связи |
|---|---|
| `Portfolio` | `user` → `AUTH_USER_MODEL` (`CASCADE`), `name` (255), `created_at` (`auto_now_add`); уникальность `(user, name)`, сортировка по имени |
| `Transaction` | `portfolio` → `Portfolio` (`CASCADE`), `share` → `Share` (`PROTECT`), `operation` (`buy`/`sell`), `quantity` (positive integer), `price` (float), `executed_at` (по умолчанию `timezone.now`), `created_at` (`auto_now_add`); сортировка по `-executed_at`, затем `-id` |

Модель `Share` не изменялась. Миграция: `dashboard/migrations/0008_portfolio_transaction.py`.

## Расчёты

- По каждой акции чистое количество равно `Σ(buy quantity) - Σ(sell quantity)`.
- Позиции с количеством `<= 0` не включаются в результат.
- Средняя цена покупки — сумма `price * quantity` для покупок, делённая на купленное количество.
- `value = quantity * Share.last_price`, если `last_price` известна; иначе `None`.
- `cost = quantity * avg_buy_price`.
- `total_value` суммирует только известные значения `value`; `total_cost` суммирует себестоимость открытых позиций.
- `pnl = total_value - total_cost`; `pnl_percent = pnl / total_cost * 100`, если `total_cost > 0`, иначе `None`.

## API

Все портфельные API требуют аутентификации. Портфели и транзакции доступны только владельцу; создавать транзакцию для чужого портфеля запрещено.

| Endpoint | Назначение |
|---|---|
| `/api/v1/portfolios/` | Список своих портфелей и создание |
| `/api/v1/portfolios/<id>/` | Чтение, изменение и удаление своего портфеля |
| `/api/v1/transactions/` | Список своих транзакций и создание |
| `/api/v1/transactions/<id>/` | Чтение, изменение и удаление своей транзакции |

Поля портфеля `id`, `created_at`, `total_value`, `total_cost`, `pnl`, `pnl_percent` только для чтения; `name` доступно для записи. Транзакция принимает PK `portfolio` и `share`.

## HTML

| URL | Поведение |
|---|---|
| `/portfolio/` | Список портфелей текущего пользователя |
| `/portfolio/create/` | Создание портфеля, владелец назначается из сессии |
| `/portfolio/<id>/` | Детали, KPI, открытые позиции и транзакции; чужой портфель возвращает 404 |
| `/portfolio/<id>/transaction/add/` | Добавление транзакции только в собственный портфель |

В navbar ссылка «Портфель» отображается после входа. Анонимный пользователь перенаправляется на `user:login`. Добавлены шаблоны списка, формы портфеля, деталей и формы транзакции на Bootstrap 3.

## Ошибки и исправления

UI-тест `test_portfolio_detail_own` сначала получил 302, потому что `force_authenticate` — механизм DRF, который не создаёт Django-сессию для HTML-view. Тест исправлен: создаёт `htmluser` и входит через `self.client.login`. API-тесты продолжают использовать `force_authenticate`, как и требуется для DRF. Анонимный UI-тест списка остаётся без входа.

## Проверки и покрытие

Исходный baseline фактически **23 теста, не 22**: после шага 3.4 был добавлен регрессионный тест detail-view. Итог **33 = 23 + 4 модельных + 4 API + 2 UI** теста.

- `manage.py check` — `System check identified no issues (0 silenced)`.
- `manage.py makemigrations --check --dry-run --settings=config.settings_test` — `No changes detected`.
- `manage.py test -v 2 --settings=config.settings_test` — `Ran 33 tests`, `OK`.
- `black --check` для `dashboard/models.py`, `dashboard/views.py`, `dashboard/urls.py`, `dashboard/api/v1/serializer.py`, `dashboard/api/v1/views.py`, `dashboard/api/v1/router.py`, `dashboard/tests.py` — успешно. После форматирования `models.py` и `tests.py` полный тестовый прогон повторён.

## Отрицательное количество и непроверенное

Транзакции продажи сохраняются, даже если продажи превысили покупки; позиции с итоговым количеством `<= 0` скрываются из расчётов. Это покрыто модельным тестом.

Не выполнялись E2E через runserver для новых страниц и интеграция с живыми Tinkoff-ценами. У только что созданной акции `last_price` может быть `None`; тогда её стоимость не включается в `total_value`, но себестоимость учитывается.
