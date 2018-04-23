Django Rest Framework Challenge
----------------
This is simple implementation of Twitter API.
This platform contains restfull APIs for the client end applications.
We use $python-twitter to implement the task.

Requirements
------------

- Python 3.6.3
- Django 2.0.4
- Django Rest Framework 3.8.2
- Postgres

Installation
------------
Following are the steps to install this platform.

- Create Virtual Environment
```sh
$ git clone https://gitlab.com/MirzaBaig715/Django-REST-Challenge.git
$ cd Challenge_task
$ virtualenv venv --python=python3
$ virtualenv venv --python=python3
$ cd venv
$ source bin/activate
```
https://apps.twitter.com/

- Twitter Credentials
---------------------
Create twitter application on developer console and get the credentials.
Place them in settings.py

```sh
$CONSUMER_KEY = '################'
$CONSUMER_SECRET = '################'
$ACESS_TOKEN_KEY = '################'
$ACESS_TOKEN_SECRET = '################'
```
- Running Docker
```sh
$ docker-compose run web python manage.py migrate
$ docker-compose run web python manage.py runserver

```
- Running Tests
```sh
$ pytest twitterapp/tests.py

```
- Documentation
https://documenter.getpostman.com/view/2377788/docker-challenge/RW1XM24d