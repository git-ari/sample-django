# sample-django

This project is a study case of [Python] on how to build an example of an API using [Django]. It was used [drf-yasg] dependency to implement [Swagger]. For now, the main goal is to develop a CRUD application of a Todo List.

## Required software

 - [Python 3](https://www.python.org/downloads/)
 - [Django](https://www.djangoproject.com/download/)


## Setting up the environment

```sh
virtualenv .env && source .env/bin/activate && pip install -r requirements.txt
```

> To exit the virtual environment at any time, just type `deactivate`. For more information see the [venv] documentation.

## Build database

```sh
python manage.py makemigrations
python manage.py migrate
```

## Run

```sh
python manage.py runserver
```

[Swagger] page is available at http://localhost:8000/swagger

> Needed this fix: https://github.com/encode/django-rest-framework/issues/6809#issuecomment-593627748Django REST Swagger

## License
MIT


### Reference material

Create a new project with [Django]
```sh
django-admin startproject sampledjango
```

Add a new application to [Django]
```sh
python manage.py startapp webapp
```

Create a new admin user for the [Django]

```sh
python manage.py createsuperuser
```

Update the dependencies of [Python]

```sh
pip freeze > requirements.txt
```


To restart database from scratch:

```sh
rm -f tmp.db db.sqlite3
rm -r my-app/migrations
python manage.py makemigrations
python manage.py migrate
```
Swagger + OAuth2 - https://github.com/Vigrond/django_oauth2_example/blob/master/settings.py

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

[Django]: <https://www.djangoproject.com/>
[drf-yasg]: <https://github.com/axnsan12/drf-yasg/>
[Swagger]: <https://swagger.io/>
[Python]: <https://www.python.org/>
[venv]: <https://docs.python.org/3/library/venv.html>