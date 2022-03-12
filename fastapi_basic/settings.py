""" This File Content All Setting For FastAPI-Basic Project """
from os import environ

from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_POSTGRES_DATABASE_URL = "postgresql://{user}:{password}@{postgres_server}/{data_base}".format(
    user=environ.get("POSTGRESQL_USER"),
    password=environ.get("POSTGRESQL_PASSWORD"),
    postgres_server=environ.get("POSTGRESQL_DATABASE_HOST"),
    data_base=environ.get("POSTGRESQL_DATABASE_NAME")
)

ENGINE = create_engine(
    SQLALCHEMY_POSTGRES_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=ENGINE)

Base = declarative_base()
