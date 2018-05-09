Django Default Value Trap
===========================

This project is used to demonstrate an easy-to-fall trap in django model.
Tested with python-3.6.

When setting a dict as default value to a django model field,
don't use `{}` or any other pre-defined dictionary.
Instead, a function that "generates" the dictionary should be passed as default value.

- Incorrect: `detail = JSONField(default={})`
- Correct: `detail = JSONField(default=dict)`


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

## Run the Test

Run the test through following command:

```
$ ./manage.py default_test
book1.detail.author = None
book1.detail.author = Steven
book1 saved.
book2.detail.author = Steven
```

You will see that `book2.detail.author` took a default value of `Steven` which was never set to `book2.detail`.
This value was changed by the assignment to `book1.detail'author']`, incorrectly.

