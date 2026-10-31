# Step 3.1 — обновление зависимостей

## 1. Diff requirements

Изменения относительно исходного `requirements.txt`:

| Пакет/строка | Было | Стало |
|---|---|---|
| Django | `Django==4.1.7` | `Django==5.2.18` |
| DRF | `djangorestframework==3.14.0` | `djangorestframework==3.18.3` |
| Celery | `celery==5.2.7` | `celery==5.6.3` |
| django-filter | `django-filter==22.1` | `django-filter==26.2` |
| django-crispy-forms | `django-crispy-forms==2.0` | `django-crispy-forms==2.7` |
| Redis client | `redis==4.5.1` | `redis==6.4.0` |
| gRPC | `grpcio==1.51.3` | `grpcio==1.85.1` |
| protobuf | `protobuf==3.20.3` | `protobuf>=4.25.1,<5.0.0` |
| SDK | `tinkoff-investments==0.2.0b50` и `tinkoff==0.1.1` | Git SDK вынесен в `requirements-sdk.txt`; `tinkoff`-пин удалён |
| SDK runtime dependency | отсутствовала | `deprecation==2.1.0` |
| Celery transitives | прямые пины `amqp==5.1.1`, `billiard==3.6.4.0`, `kombu==5.2.4`, `vine==5.0.0`, `asgiref==3.6.0` | удалены; resolver поставил совместимые версии |
| typing extensions | `typing_extensions==4.5.0` | прямой пин удалён; grpcio требует `typing-extensions~=4.12` |
| crispy-bootstrap3 | `crispy-bootstrap3==2022.1` | без изменений |

Текущая установка базовых пакетов выполняется командой `pip install -r requirements.txt`. SDK отдельно устанавливается из [requirements-sdk.txt](../../requirements-sdk.txt) командой `pip install -r requirements-sdk.txt --no-deps`. `requirements.txt` намеренно не содержит SDK: разрешить его metadata dependency `tinkoff>=0.1.1,<0.2.0` из доступных индексов не удалось. T-Bank индекс проверен, но pip получил TLS certificate verification failure для `opensource.tbank.ru`.

## 2. Чистая установка и SDK

- Python: `3.11.9`; pip: `26.2.2`.
- `pip install -r requirements.txt`: успешно в новом `.venv311`.
- SDK: GitHub `https://github.com/RussianInvestments/invest-python.git`, revision `fcf0af1`, установлен отдельно:

```powershell
python -m pip install -r requirements-sdk.txt --no-deps
```

Фактическая версия пакета — `tinkoff-investments==0.2.0b117`; фактические runtime-версии SDK — `grpcio==1.85.1`, `protobuf==4.25.9`, `deprecation==2.1.0`.

Полный `pip list --format=freeze` после чистой установки:

```text
amqp==5.4.1
asgiref==3.13.0
async-timeout==4.0.2
billiard==4.3.1
black==23.1.0
cachetools==5.3.0
celery==5.6.3
click==8.1.3
click-didyoumean==0.3.0
click-plugins==1.1.1
click-repl==0.2.0
colorama==0.4.6
crispy-bootstrap3==2022.1
deprecation==2.1.0
Django==5.2.18
django-crispy-forms==2.7
django-filter==26.2
djangorestframework==3.18.3
grpcio==1.85.1
isort==5.12.0
kombu==5.6.2
mypy-extensions==1.0.0
packaging==23.0
pathspec==0.11.1
pip==26.2.2
platformdirs==3.1.1
plotly==5.13.1
prompt-toolkit==3.0.38
protobuf==4.25.9
psycopg2-binary==2.9.5
pydantic==1.10.6
python-dateutil==2.8.2
pytz==2022.7.1
redis==6.4.0
setuptools==65.5.0
six==1.16.0
sqlparse==0.4.3
tenacity==8.2.2
tinkoff-investments==0.2.0b117
tomli==2.0.1
typing_extensions==4.16.0
tzdata==2026.6
tzlocal==5.4.5
vine==5.1.0
wcwidth==0.2.6
```

## 3. `pip check`

```text
tinkoff-investments 0.2.0b117 requires tinkoff, which is not installed.
```

Exit code: `1`. Это оставшийся metadata-конфликт SDK: его importable module входит в установленный Git SDK и импорты проходят, однако требуемый distribution `tinkoff` не опубликован в доступных индексах. Не маскировал конфликт установкой фиктивного пакета.

## 4. Django system check

Команда: `python manage.py check`

```text
STDOUT:
System check identified no issues (0 silenced).

STDERR:

Exit code: 0
```

## 5. Проверка миграций

Команда: `python manage.py makemigrations --check --dry-run`

```text
STDOUT:
No changes detected

STDERR:
RuntimeWarning: Django не смог проверить историю миграций в базе default: PostgreSQL localhost:5432 недоступен (IPv6: Permission denied; IPv4: Connection refused).

Exit code: 0
```

Новых миграций нет; ничего не создавалось.

## 6. Тесты

Команда: `python manage.py test -v 2 --settings=config.settings_test`

```text
STDOUT:
Found 10 test(s).
Operations to perform:
  Synchronize unmigrated apps: crispy_bootstrap3, crispy_forms, django_filters, messages, rest_framework, staticfiles
  Apply all migrations: admin, auth, contenttypes, dashboard, sessions
Synchronizing apps without migrations:
  Creating tables...
    Running deferred SQL...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying dashboard.0001_add_share... OK
  Applying dashboard.0002_update_share... OK
  Applying dashboard.0003_add_uuid... OK
  Applying dashboard.0004_add_last_price... OK
  Applying dashboard.0005_add_verbose_name... OK
  Applying dashboard.0006_add_verbose_name... OK
  Applying dashboard.0007_add_updated_at... OK
  Applying sessions.0001_initial... OK
System check identified no issues (0 silenced).

STDERR:
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...

test_share_create (dashboard.tests.DashboardTests.test_share_create) ... ok
test_share_create_invalid (dashboard.tests.DashboardTests.test_share_create_invalid) ... ok
test_share_delete (dashboard.tests.DashboardTests.test_share_delete) ... ok
test_share_delete_invalid (dashboard.tests.DashboardTests.test_share_delete_invalid) ... ok
test_share_detail (dashboard.tests.DashboardTests.test_share_detail) ... ok
test_share_detail_invalid (dashboard.tests.DashboardTests.test_share_detail_invalid) ... ok
test_share_list (dashboard.tests.DashboardTests.test_share_list) ... ok
test_share_list_html (dashboard.tests.DashboardTests.test_share_list_html) ... ok
test_share_update (dashboard.tests.DashboardTests.test_share_update) ... ok
test_share_update_invalid (dashboard.tests.DashboardTests.test_share_update_invalid) ... ok

----------------------------------------------------------------------
Ran 10 tests in 0.072s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...

Exit code: 0
```

## 7. Crispy template pack

Оставлен `crispy-bootstrap3==2022.1`: обновлённый набор тестов прошёл, поэтому замену template pack по условию шага 4 не запускал. Отдельный рендеринг формы/браузерный визуальный тест не выполнялся, поэтому совместимость внешнего template pack отдельно не подтверждена.

## 8. Импорт SDK и сервиса

Команда:

```text
python -c "from tinkoff.invest import Client; from dashboard.services.market_data import get_last_data; print('imports OK')"
```

```text
STDOUT: imports OK
STDERR:
Exit code: 0
```

## 9. Не проверено

- Живой запрос к Tinkoff API: токен не предоставлен.
- Celery worker/Beat с Redis.
- End-to-end через `runserver`.
- PostgreSQL миграционная история: PostgreSQL в среде недоступен; тесты использовали SQLite test-only settings.
