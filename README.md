# SWP-SC-web-app
Web app for students and university staff that allows to keep track of hours visited and schedule of trainings

### Web application
Folder contains sport course web application on `Django version 3.0.5`.\
To run the server use the following command: `python manage.py runserver`

### Django admin menu
login: `admin` \
password: `admin`

### Database setup (postgresql)
```
postgres=# CREATE DATABASE sport_course;
postgres=# CREATE USER sport_course_user WITH PASSWORD 'password';
postgres=# ALTER ROLE sport_course_user SET client_encoding to 'utf8';
postgres=# ALTER ROLE sport_course_user SET timezone TO 'UTC+3';
postgres=# GRANT ALL PRIVILEGES ON DATABASE sport_course TO sport_course_user;
```