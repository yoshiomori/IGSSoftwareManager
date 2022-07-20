# IGS-Software Manager
## Introduction
An application to manage employee information, such as name, e-mail, and departament.

## Requirements
* Python 3.8 or greater

```$ pip install -r requirements.txt```

## Get started 
In order to run IGS-Software Manager, execute this commands in terminal:

```$ python manage.py migrate```

```$ python manage.py createsuperuser``` *creates a superuser account to be able to use [admin site](http://127.0.0.1:8000/admin) and update gsi.postman_collection.json with authentication data*

```$ python manage.py loaddata information``` *searches and loads the contents into database*

```$ python manage.py runserver```

Follow the postman [tutorial](https://learning.postman.com/docs/getting-started/importing-and-exporting-data/#importing-postman-data) to import gsi.postman_collection.json, use gsi.postman_collection.json as a base to do your own tests.