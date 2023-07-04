Chat app with Django and Django channels.

# Getting Started

## Project setup and run

<br />

Install [redis](https://github.com/tporadowski/redis/releases/download/v5.0.14.1/Redis-x64-5.0.14.1.msi). 
Setup the redis and open redis cli and run it backgorund for the first time

> Install dependency
```bash
pip install -r requirements.txt
```
> Migrate database and create superuser
```bash
python manage.py migrate
python manage.py createsuperuser
```
> Run the server
```bash
python manage.py runserver
```

<br />

![alt text](/static/gifs/preview.gif)
