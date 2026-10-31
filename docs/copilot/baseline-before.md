# Baseline before dependency upgrade

Environment: Python 3.11 venv `.venv311`.

## python --version

```text
STDOUT:
Python 3.11.9

STDERR:

```

Exit code: 0

## pip list --format=freeze

```text
STDOUT:
amqp==5.1.1
asgiref==3.6.0
async-timeout==4.0.2
billiard==3.6.4.0
black==23.1.0
cachetools==5.3.0
celery==5.2.7
click==8.1.3
click-didyoumean==0.3.0
click-plugins==1.1.1
click-repl==0.2.0
colorama==0.4.6
crispy-bootstrap3==2022.1
deprecation==2.1.0
Django==4.1.7
django-crispy-forms==2.0
django-filter==22.1
djangorestframework==3.14.0
grpcio==1.85.1
isort==5.12.0
kombu==5.2.4
mypy-extensions==1.0.0
packaging==23.0
pathspec==0.11.1
pip==24.0
platformdirs==3.1.1
plotly==5.13.1
prompt-toolkit==3.0.38
protobuf==4.25.9
psycopg2-binary==2.9.5
pydantic==1.10.6
python-dateutil==2.8.2
pytz==2022.7.1
redis==4.5.1
setuptools==65.5.0
six==1.16.0
sqlparse==0.4.3
tenacity==8.2.2
tinkoff-investments==0.2.0b117
tomli==2.0.1
typing_extensions==4.16.0
tzdata==2026.6
vine==5.0.0
wcwidth==0.2.6

STDERR:

[notice] A new release of pip is available: 24.0 -> 26.2.2
[notice] To update, run: C:\UwU\ai\aidd-topic-03-homework\.venv311\Scripts\python.exe -m pip install --upgrade pip
```

Exit code: 0

## python manage.py check

```text
STDOUT:
System check identified no issues (0 silenced).

STDERR:

```

Exit code: 0

## python manage.py test -v 2

```text
STDOUT:
Found 10 test(s).

STDERR:
Creating test database for alias 'default' ('test_investing')...

C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\postgresql\base.py:336: RuntimeWarning: Normally Django will use a connection to the 'postgres' database to avoid running initialization queries against the production database when it's not needed (for example, when running tests). Django was unable to create a connection to the 'postgres' database and will use the first PostgreSQL database instead.
  warnings.warn(
Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 282, in ensure_connection
    self.connect()
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 263, in connect
    self.connection = self.get_new_connection(conn_params)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\postgresql\base.py", line 215, in get_new_connection
    connection = Database.connect(**conn_params)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\psycopg2\__init__.py", line 122, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.OperationalError: connection to server at "localhost" (::1), port 5432 failed: Permission denied (0x0000271D/10013)
	Is the server running on that host and accepting TCP/IP connections?
connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused (0x0000274D/10061)
	Is the server running on that host and accepting TCP/IP connections?


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\postgresql\base.py", line 331, in _nodb_cursor
    with super()._nodb_cursor() as cursor:
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\contextlib.py", line 137, in __enter__
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 711, in _nodb_cursor
    with conn.cursor() as cursor:
         ^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 323, in cursor
    return self._cursor()
           ^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 299, in _cursor
    self.ensure_connection()
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 281, in ensure_connection
    with self.wrap_database_errors:
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 282, in ensure_connection
    self.connect()
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 263, in connect
    self.connection = self.get_new_connection(conn_params)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\postgresql\base.py", line 215, in get_new_connection
    connection = Database.connect(**conn_params)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\psycopg2\__init__.py", line 122, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django.db.utils.OperationalError: connection to server at "localhost" (::1), port 5432 failed: Permission denied (0x0000271D/10013)
	Is the server running on that host and accepting TCP/IP connections?
connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused (0x0000274D/10061)
	Is the server running on that host and accepting TCP/IP connections?


During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 282, in ensure_connection
    self.connect()
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 263, in connect
    self.connection = self.get_new_connection(conn_params)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\postgresql\base.py", line 215, in get_new_connection
    connection = Database.connect(**conn_params)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\psycopg2\__init__.py", line 122, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
psycopg2.OperationalError: connection to server at "localhost" (::1), port 5432 failed: Permission denied (0x0000271D/10013)
	Is the server running on that host and accepting TCP/IP connections?
connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused (0x0000274D/10061)
	Is the server running on that host and accepting TCP/IP connections?


The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\manage.py", line 22, in <module>
    main()
  File "C:\UwU\ai\aidd-topic-03-homework\manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\management\__init__.py", line 446, in execute_from_command_line
    utility.execute()
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\management\__init__.py", line 440, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\management\commands\test.py", line 24, in run_from_argv
    super().run_from_argv(argv)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\management\base.py", line 402, in run_from_argv
    self.execute(*args, **cmd_options)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\management\base.py", line 448, in execute
    output = self.handle(*args, **options)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\management\commands\test.py", line 68, in handle
    failures = test_runner.run_tests(test_labels)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\runner.py", line 1050, in run_tests
    old_config = self.setup_databases(
                 ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\runner.py", line 946, in setup_databases
    return _setup_databases(
           ^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\utils.py", line 220, in setup_databases
    connection.creation.create_test_db(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\creation.py", line 62, in create_test_db
    self._create_test_db(verbosity, autoclobber, keepdb)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\creation.py", line 199, in _create_test_db
    with self._nodb_cursor() as cursor:
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\contextlib.py", line 137, in __enter__
    return next(self.gen)
           ^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\postgresql\base.py", line 357, in _nodb_cursor
    with conn.cursor() as cursor:
         ^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 323, in cursor
    return self._cursor()
           ^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 299, in _cursor
    self.ensure_connection()
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 281, in ensure_connection
    with self.wrap_database_errors:
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 282, in ensure_connection
    self.connect()
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\base\base.py", line 263, in connect
    self.connection = self.get_new_connection(conn_params)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\asyncio.py", line 26, in inner
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\db\backends\postgresql\base.py", line 215, in get_new_connection
    connection = Database.connect(**conn_params)
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\psycopg2\__init__.py", line 122, in connect
    conn = _connect(dsn, connection_factory=connection_factory, **kwasync)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
django.db.utils.OperationalError: connection to server at "localhost" (::1), port 5432 failed: Permission denied (0x0000271D/10013)
	Is the server running on that host and accepting TCP/IP connections?
connection to server at "localhost" (127.0.0.1), port 5432 failed: Connection refused (0x0000274D/10061)
	Is the server running on that host and accepting TCP/IP connections?
```

Exit code: 1

## ???????? ?????? ??????

????: SQLite in-memory ????? `config/settings_test.py`. Docker Postgres ?? ????????: ??????? `docker --version` ? `docker compose version` ?? ???????? ? ????? (`docker` ?? ?????????? ??? ???????). ????????? `psql`, `postgres` ? `pg_ctl` ????? ???????????.

Command: `.\.venv311\Scripts\python.exe manage.py test -v 2 --settings=config.settings_test`

### STDOUT

```text
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
```

### STDERR

```text
Creating test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...

test_share_create (dashboard.tests.DashboardTests.test_share_create) ... ERROR
test_share_create_invalid (dashboard.tests.DashboardTests.test_share_create_invalid) ... ERROR
test_share_delete (dashboard.tests.DashboardTests.test_share_delete) ... ERROR
test_share_delete_invalid (dashboard.tests.DashboardTests.test_share_delete_invalid) ... ERROR
test_share_detail (dashboard.tests.DashboardTests.test_share_detail) ... ERROR
test_share_detail_invalid (dashboard.tests.DashboardTests.test_share_detail_invalid) ... ERROR
test_share_list (dashboard.tests.DashboardTests.test_share_list) ... ERROR
test_share_list_html (dashboard.tests.DashboardTests.test_share_list_html) ... ERROR
test_share_update (dashboard.tests.DashboardTests.test_share_update) ... ERROR
test_share_update_invalid (dashboard.tests.DashboardTests.test_share_update_invalid) ... ERROR

======================================================================
ERROR: test_share_create (dashboard.tests.DashboardTests.test_share_create)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 135, in __call__
    response = self.process_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\middleware.py", line 12, in process_request
    request._messages = default_storage(request)
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\__init__.py", line 12, in default_storage
    return import_string(settings.MESSAGE_STORAGE)(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 16, in __init__
    self.storages = [
                    ^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 17, in <listcomp>
    storage_class(*args, **kwargs) for storage_class in self.storage_classes
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\cookie.py", line 77, in __init__
    self.signer = signing.get_cookie_signer(salt=self.key_salt)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\signing.py", line 112, in get_cookie_signer
    key=_cookie_signer_key(settings.SECRET_KEY),
                           ^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\dashboard\tests.py", line 92, in test_share_create
    response = self.client.post(
               ^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 296, in post
    response = super().post(
               ^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 210, in post
    return self.generic('POST', path, data, content_type, **extra)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 234, in generic
    return super().generic(
           ^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 541, in generic
    return self.request(**r)
           ^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 286, in request
    return super().request(**kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 238, in request
    request = super().request(**kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 805, in request
    response = self.handler(environ)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 153, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 258, in get_response
    return super().get_response(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

======================================================================
ERROR: test_share_create_invalid (dashboard.tests.DashboardTests.test_share_create_invalid)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 135, in __call__
    response = self.process_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\middleware.py", line 12, in process_request
    request._messages = default_storage(request)
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\__init__.py", line 12, in default_storage
    return import_string(settings.MESSAGE_STORAGE)(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 16, in __init__
    self.storages = [
                    ^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 17, in <listcomp>
    storage_class(*args, **kwargs) for storage_class in self.storage_classes
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\cookie.py", line 77, in __init__
    self.signer = signing.get_cookie_signer(salt=self.key_salt)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\signing.py", line 112, in get_cookie_signer
    key=_cookie_signer_key(settings.SECRET_KEY),
                           ^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\dashboard\tests.py", line 106, in test_share_create_invalid
    response = self.client.post(
               ^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 296, in post
    response = super().post(
               ^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 210, in post
    return self.generic('POST', path, data, content_type, **extra)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 234, in generic
    return super().generic(
           ^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 541, in generic
    return self.request(**r)
           ^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 286, in request
    return super().request(**kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 238, in request
    request = super().request(**kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 805, in request
    response = self.handler(environ)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 153, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 258, in get_response
    return super().get_response(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

======================================================================
ERROR: test_share_delete (dashboard.tests.DashboardTests.test_share_delete)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 135, in __call__
    response = self.process_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\middleware.py", line 12, in process_request
    request._messages = default_storage(request)
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\__init__.py", line 12, in default_storage
    return import_string(settings.MESSAGE_STORAGE)(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 16, in __init__
    self.storages = [
                    ^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 17, in <listcomp>
    storage_class(*args, **kwargs) for storage_class in self.storage_classes
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\cookie.py", line 77, in __init__
    self.signer = signing.get_cookie_signer(salt=self.key_salt)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\signing.py", line 112, in get_cookie_signer
    key=_cookie_signer_key(settings.SECRET_KEY),
                           ^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\dashboard\tests.py", line 112, in test_share_delete
    response = self.client.get("/api/v1/shares/")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 289, in get
    response = super().get(path, data=data, **extra)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 206, in get
    return self.generic('GET', path, **r)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 234, in generic
    return super().generic(
           ^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 541, in generic
    return self.request(**r)
           ^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 286, in request
    return super().request(**kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 238, in request
    request = super().request(**kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 805, in request
    response = self.handler(environ)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 153, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 258, in get_response
    return super().get_response(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

======================================================================
ERROR: test_share_delete_invalid (dashboard.tests.DashboardTests.test_share_delete_invalid)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 135, in __call__
    response = self.process_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\middleware.py", line 12, in process_request
    request._messages = default_storage(request)
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\__init__.py", line 12, in default_storage
    return import_string(settings.MESSAGE_STORAGE)(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 16, in __init__
    self.storages = [
                    ^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 17, in <listcomp>
    storage_class(*args, **kwargs) for storage_class in self.storage_classes
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\cookie.py", line 77, in __init__
    self.signer = signing.get_cookie_signer(salt=self.key_salt)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\signing.py", line 112, in get_cookie_signer
    key=_cookie_signer_key(settings.SECRET_KEY),
                           ^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\dashboard\tests.py", line 121, in test_share_delete_invalid
    response = self.client.delete("/api/v1/shares/3/")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 320, in delete
    response = super().delete(
               ^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 222, in delete
    return self.generic('DELETE', path, data, content_type, **extra)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 234, in generic
    return super().generic(
           ^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 541, in generic
    return self.request(**r)
           ^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 286, in request
    return super().request(**kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 238, in request
    request = super().request(**kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 805, in request
    response = self.handler(environ)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 153, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 258, in get_response
    return super().get_response(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

======================================================================
ERROR: test_share_detail (dashboard.tests.DashboardTests.test_share_detail)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 135, in __call__
    response = self.process_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\middleware.py", line 12, in process_request
    request._messages = default_storage(request)
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\__init__.py", line 12, in default_storage
    return import_string(settings.MESSAGE_STORAGE)(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 16, in __init__
    self.storages = [
                    ^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 17, in <listcomp>
    storage_class(*args, **kwargs) for storage_class in self.storage_classes
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\cookie.py", line 77, in __init__
    self.signer = signing.get_cookie_signer(salt=self.key_salt)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\signing.py", line 112, in get_cookie_signer
    key=_cookie_signer_key(settings.SECRET_KEY),
                           ^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\dashboard\tests.py", line 49, in test_share_detail
    response = self.client.get("/api/v1/shares/")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 289, in get
    response = super().get(path, data=data, **extra)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 206, in get
    return self.generic('GET', path, **r)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 234, in generic
    return super().generic(
           ^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 541, in generic
    return self.request(**r)
           ^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 286, in request
    return super().request(**kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 238, in request
    request = super().request(**kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 805, in request
    response = self.handler(environ)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 153, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 258, in get_response
    return super().get_response(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

======================================================================
ERROR: test_share_detail_invalid (dashboard.tests.DashboardTests.test_share_detail_invalid)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 135, in __call__
    response = self.process_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\middleware.py", line 12, in process_request
    request._messages = default_storage(request)
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\__init__.py", line 12, in default_storage
    return import_string(settings.MESSAGE_STORAGE)(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 16, in __init__
    self.storages = [
                    ^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 17, in <listcomp>
    storage_class(*args, **kwargs) for storage_class in self.storage_classes
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\cookie.py", line 77, in __init__
    self.signer = signing.get_cookie_signer(salt=self.key_salt)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\signing.py", line 112, in get_cookie_signer
    key=_cookie_signer_key(settings.SECRET_KEY),
                           ^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\dashboard\tests.py", line 55, in test_share_detail_invalid
    response = self.client.get("/api/v1/shares/2/")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 289, in get
    response = super().get(path, data=data, **extra)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 206, in get
    return self.generic('GET', path, **r)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 234, in generic
    return super().generic(
           ^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 541, in generic
    return self.request(**r)
           ^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 286, in request
    return super().request(**kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 238, in request
    request = super().request(**kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 805, in request
    response = self.handler(environ)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 153, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 258, in get_response
    return super().get_response(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

======================================================================
ERROR: test_share_list (dashboard.tests.DashboardTests.test_share_list)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 135, in __call__
    response = self.process_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\middleware.py", line 12, in process_request
    request._messages = default_storage(request)
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\__init__.py", line 12, in default_storage
    return import_string(settings.MESSAGE_STORAGE)(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 16, in __init__
    self.storages = [
                    ^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 17, in <listcomp>
    storage_class(*args, **kwargs) for storage_class in self.storage_classes
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\cookie.py", line 77, in __init__
    self.signer = signing.get_cookie_signer(salt=self.key_salt)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\signing.py", line 112, in get_cookie_signer
    key=_cookie_signer_key(settings.SECRET_KEY),
                           ^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\dashboard\tests.py", line 37, in test_share_list
    response = self.client.get("/api/v1/shares/")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 289, in get
    response = super().get(path, data=data, **extra)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 206, in get
    return self.generic('GET', path, **r)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 234, in generic
    return super().generic(
           ^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 541, in generic
    return self.request(**r)
           ^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 286, in request
    return super().request(**kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 238, in request
    request = super().request(**kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 805, in request
    response = self.handler(environ)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 153, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 258, in get_response
    return super().get_response(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

======================================================================
ERROR: test_share_list_html (dashboard.tests.DashboardTests.test_share_list_html)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 135, in __call__
    response = self.process_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\middleware.py", line 12, in process_request
    request._messages = default_storage(request)
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\__init__.py", line 12, in default_storage
    return import_string(settings.MESSAGE_STORAGE)(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 16, in __init__
    self.storages = [
                    ^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 17, in <listcomp>
    storage_class(*args, **kwargs) for storage_class in self.storage_classes
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\cookie.py", line 77, in __init__
    self.signer = signing.get_cookie_signer(salt=self.key_salt)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\signing.py", line 112, in get_cookie_signer
    key=_cookie_signer_key(settings.SECRET_KEY),
                           ^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\dashboard\tests.py", line 33, in test_share_list_html
    response = self.client.get(reverse("dashboard:index"))
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 289, in get
    response = super().get(path, data=data, **extra)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 206, in get
    return self.generic('GET', path, **r)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 234, in generic
    return super().generic(
           ^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 541, in generic
    return self.request(**r)
           ^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 286, in request
    return super().request(**kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 238, in request
    request = super().request(**kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 805, in request
    response = self.handler(environ)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 153, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 258, in get_response
    return super().get_response(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

======================================================================
ERROR: test_share_update (dashboard.tests.DashboardTests.test_share_update)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 135, in __call__
    response = self.process_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\middleware.py", line 12, in process_request
    request._messages = default_storage(request)
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\__init__.py", line 12, in default_storage
    return import_string(settings.MESSAGE_STORAGE)(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 16, in __init__
    self.storages = [
                    ^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 17, in <listcomp>
    storage_class(*args, **kwargs) for storage_class in self.storage_classes
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\cookie.py", line 77, in __init__
    self.signer = signing.get_cookie_signer(salt=self.key_salt)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\signing.py", line 112, in get_cookie_signer
    key=_cookie_signer_key(settings.SECRET_KEY),
                           ^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\dashboard\tests.py", line 59, in test_share_update
    response = self.client.get("/api/v1/shares/")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 289, in get
    response = super().get(path, data=data, **extra)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 206, in get
    return self.generic('GET', path, **r)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 234, in generic
    return super().generic(
           ^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 541, in generic
    return self.request(**r)
           ^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 286, in request
    return super().request(**kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 238, in request
    request = super().request(**kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 805, in request
    response = self.handler(environ)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 153, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 258, in get_response
    return super().get_response(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

======================================================================
ERROR: test_share_update_invalid (dashboard.tests.DashboardTests.test_share_update_invalid)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 135, in __call__
    response = self.process_request(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\middleware.py", line 12, in process_request
    request._messages = default_storage(request)
                        ^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\__init__.py", line 12, in default_storage
    return import_string(settings.MESSAGE_STORAGE)(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 16, in __init__
    self.storages = [
                    ^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\fallback.py", line 17, in <listcomp>
    storage_class(*args, **kwargs) for storage_class in self.storage_classes
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\contrib\messages\storage\cookie.py", line 77, in __init__
    self.signer = signing.get_cookie_signer(salt=self.key_salt)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\signing.py", line 112, in get_cookie_signer
    key=_cookie_signer_key(settings.SECRET_KEY),
                           ^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 56, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\deprecation.py", line 136, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\UwU\ai\aidd-topic-03-homework\dashboard\tests.py", line 79, in test_share_update_invalid
    response = self.client.get("/api/v1/shares/")
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 289, in get
    response = super().get(path, data=data, **extra)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 206, in get
    return self.generic('GET', path, **r)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 234, in generic
    return super().generic(
           ^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 541, in generic
    return self.request(**r)
           ^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 286, in request
    return super().request(**kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 238, in request
    request = super().request(**kwargs)
              ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 805, in request
    response = self.handler(environ)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\test\client.py", line 153, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\rest_framework\test.py", line 258, in get_response
    return super().get_response(request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 58, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\core\handlers\exception.py", line 144, in response_for_exception
    log_response(
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 241, in log_response
    getattr(logger, level)(
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1518, in error
    self._log(ERROR, msg, args, **kwargs)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1634, in _log
    self.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1644, in handle
    self.callHandlers(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 1706, in callHandlers
    hdlr.handle(record)
  File "C:\Users\umulk\AppData\Local\Programs\Python\Python311\Lib\logging\__init__.py", line 978, in handle
    self.emit(record)
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\utils\log.py", line 125, in emit
    reporter.get_traceback_text(),
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 403, in get_traceback_text
    c = Context(self.get_traceback_data(), autoescape=False, use_l10n=False)
                ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 366, in get_traceback_data
    "settings": self.filter.get_safe_settings(),
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\views\debug.py", line 150, in get_safe_settings
    settings_dict[k] = self.cleanse_setting(k, getattr(settings, k))
                                               ^^^^^^^^^^^^^^^^^^^^
  File "C:\UwU\ai\aidd-topic-03-homework\.venv311\Lib\site-packages\django\conf\__init__.py", line 101, in __getattr__
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")
django.core.exceptions.ImproperlyConfigured: The SECRET_KEY setting must not be empty.

----------------------------------------------------------------------
Ran 10 tests in 1.423s

FAILED (errors=10)
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
```

Exit code: 1

Earlier SQLite attempt: `Ran 10 tests`; `FAILED (errors=10)` because `SECRET_KEY` was empty in `config/settings.py` line 6. This was a configuration failure, not an SQLite backend failure. The later test-only settings add a dummy secret key.

Earlier baseline status: tests had not passed. Docker and PostgreSQL were unavailable, and the test override at that time changed only `DATABASES`.


## Green baseline on SQLite (test-only settings)

- Test path: SQLite in-memory through `config/settings_test.py`; Docker/PostgreSQL was not used.
- `config/settings_test.py` adds the test-only docstring, `SECRET_KEY = "test-only-not-for-production"`, `DEBUG = False`, `ALLOWED_HOSTS = ["testserver", "localhost", "127.0.0.1"]`, and `PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]`; `DATABASES` remains SQLite `:memory:`.
- `config/settings.py` was not changed.
- `dashboard/tests.py` was not changed; detail-view tests passed without an external API call.
- This successful run supersedes the earlier failing baseline run.

### Full test output

???????: ` .\.venv311\Scripts\python.exe manage.py test -v 2 --settings=config.settings_test`

#### STDOUT

```text
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
```

#### STDERR

```text
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
Ran 10 tests in 0.114s

OK
Destroying test database for alias 'default' ('file:memorydb_default?mode=memory&cache=shared')...
```

Exit code: 0

**Status: tests green — Ran 10, OK.**

## Green SQLite baseline — verified summary

- Test-only settings: `SECRET_KEY="test-only-not-for-production"`, `DEBUG=False`, `ALLOWED_HOSTS=["testserver", "localhost", "127.0.0.1"]`, `PASSWORD_HASHERS=["django.contrib.auth.hashers.MD5PasswordHasher"]`, plus SQLite in-memory `DATABASES`.
- `config/settings.py` was not changed.
- `dashboard/tests.py` was not changed; the detail-view tests passed without patching.
- Test command: `.\.venv311\Scripts\python.exe manage.py test -v 2 --settings=config.settings_test`
- Full test output is in the STDOUT and STDERR blocks immediately above.
- Result: `Ran 10 tests in 0.114s`, `OK`; exit code `0`.
- This successful run supersedes the earlier failing SQLite run with empty `SECRET_KEY`.
