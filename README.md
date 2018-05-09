Django Default Value Trap
===========================

This project is used to demonstrate an easy-to-fall trap in django model.
Tested with python-3.6.


## Setup

First, initialize a virtualenv and install required packages:

```
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```

Connect to your PostgreSQL server and create a database named `django_default_trap`.

```
$ psql -U postgres
psql (10.3 (Ubuntu 10.3-1))
Type "help" for help.

postgres=# create database django_default_trap;
CREATE DATABASE
postgres=# \q
```

Then edit `settings.py` and change the `DATABASES` setting to use your database credential.

Then run the following command:

```
$ ./manage.py migrate
```