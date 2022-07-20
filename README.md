# IGS-Software Manager
## Introduction
An application to manage employee information, such as name, e-mail, and departament.

## Requirements
* Python 3.8 or greater

```$ pip install -r requirements.txt```

## Get started 
In order to run IGS-Software Manager, execute this commands in terminal:

```$ python manage.py migrate```

```$ python manage.py createsuperuser``` *creates a superuser account to be able to use [admin site](http://127.0.0.1/admin)*

```$ python manage.py loaddata information``` *searches and loads the contents into database*

```$ python manage.py runserver```