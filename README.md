# Python-Web-App
A Web app which asks for email ,then sends an email to the entered email. Made using HTML and CSS for frontend and Python and Flask for the backend and PostgreSQL(SQLAlchemy) as the database.
# Snippt-Internship
# Installation

```sh
$ pip install -r requirements.txt
```
For Database installation,install Postgresql.

```sh
$ psql 
```

```sh
psql-> CREATE DATABASE email_1
```
Change the Database URI in script.py file
Open Python console in the project directory

```sh
python-> from script import db
python-> d.create_all()
```


# Usage

```sh
$ python script.py
```

Open http://127.0.0.1:5000/

