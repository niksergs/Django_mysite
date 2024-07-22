# Blog

Приложение является веб блогом, поддерживает регистрацию пользователей,
аутентификацию через социальные сети (GitHub, Google),
комментирование опубликованных записей.
Данное приложение имеет API реализованное на Django Rest Framework,
для отображения документации применены redoc и swagger.
Для отображения frontend части используется Django Template Language, Bootstrap 5 и CSS.
В качестве БД используется PostgreSQL.

## Quickstart

Run the following commands to bootstrap your environment:
    
    pip install virtualenv
    git clone https://github.com/niksergs/Django_mysite.git
    cd mysite

    python -m venv venv
    venv/Scripts/activate.bat
    pip install -r requirements.txt
    
    Необходимо создать и заполнить файл .env
    cp .env

Run the app locally:

    python manage.py runserver 0.0.0.0:8000

Run the app with gunicorn:

    pip install gunicorn
    gunicorn my_site.wsgi:application -b 0.0.0.0:8000
    