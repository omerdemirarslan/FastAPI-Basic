# FastAPI-Basic

---

## Requirements
* Python = 3.9
* PostgreSQL Database = 13
* [Docker](https://www.docker.com/)
* .env file on the project main line
* Install Makefile plugin: **If you want to run project makefile command**


## Description

This project is built using on the basic FastAPI microframework. Apart from these, the project is dockerized with the 
docker application. When you download the project to your local, for you to deal with extra database 
operations; PostgreSQL database.

The purpose of this project include: All FastAPI-Basic Request-Response Relationship Management.

* This project name: **FastAPI-Basic**
* This project's basic folder: **fastapi-basic**

This project has three applications. These apps:
* base
* users
* error-reporting

We are use pre-commit on this project. You have to set pre-commit for before controls committed:
* pre-commit install
---


## Installation
    git clone https://github.com/omerdemirarslan/FastAPI-Basic.git
---

## Run The Project:

### Dockerfile way

```shell
$ docker build -t fastapi-basic:latest .
$ docker run -p 8000:8000 fastapi-basic
```

### Docker-compose way

#### Example .env file content:

* POSTGRES_DB=fastapi-basic
* POSTGRES_HOST=postgres
* POSTGRES_USER=fastapi
* POSTGRES_PASSWORD=007007
* POSTGRES_PORT=5432


```shell
$ docker-compose build
$ docker-compose up
```

```text
You can add the database source in your IDE database management or other database interface.

The credentials for database in the docker:
Host: 0.0.0.0 # because project runs ıt host on your local.
Port: 6432 # because Docker use 5432 default port in base postgresql but It need difference port local project.
Database: fastapi-basic
User: fastapi
Password: 007007
```

### Local Environment Way


#### Create database in your local device. Like: **fastapi-basic**

* For command line check this: [Postgresql](https://www.postgresql.org/docs/13/tutorial-createdb.html)
* The other way is PgAdmin Interface. Check this:
[PgAdmin](https://www.postgresqltutorial.com/postgresql-administration/postgresql-create-database/)

#### Example .env file content:

* POSTGRES_DB=fastapi-basic
* POSTGRES_HOST=localhost
* POSTGRES_USER=postgres
* POSTGRES_PASSWORD=**your password**
* POSTGRES_PORT=5432


#### Create virtual environment & activate it
```shell
$ python3.9 -m venv fastapi-basic
$ source fastapi-basic/bin/activate
```


#### Install the requirements
```shell
$ pip install -r src/requirements.txt
```

#### Run project with uvicorn
```shell
$ uvicorn src.main:app --host 0.0.0.0 --reload
```

#### Run project with python command
```shell
$ /usr/bin/python3 sr.main.py --debug=True --reload=True
```

---
