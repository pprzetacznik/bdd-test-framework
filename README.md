# My Application with BDD Test framework

## Installation

```
$ pip install -r requirements.txt
```

## Run

```
$ ./run.sh run
$ FLASK_DEBUG=1 ./run.sh
```

## Run automation tests

Run them with:
```
$ ./run_bdd_tests.sh
============================= test session starts =============================
platform darwin -- Python 3.11.3, pytest-7.4.0, pluggy-1.2.0 -- ...
cachedir: .pytest_cache
rootdir: ...
configfile: pytest.ini
plugins: cov-4.1.0, bdd-6.1.1
collected 1 item

...
{'msg': 'You are not logged in'}
{'msg': 'Logged successfully'}

Feature: Users
    Scenario: Check log in
        Given user opens index page
        When user logs in with credentials
        Then user successfull message is sent
    PASSED

---------- coverage: platform darwin, python 3.11.3-final-0 ----------
Name                       Stmts   Miss  Cover
----------------------------------------------
my_app/__init__.py             0      0   100%
my_app/autoapp.py              5      5     0%
my_app/server.py              22      2    91%
my_app/settings.py            12      0   100%
my_app/users/__init__.py       1      0   100%
my_app/users/views.py         14      2    86%
----------------------------------------------
TOTAL                         54      9    83%

============================== 1 passed in 0.08s ==============================
```
