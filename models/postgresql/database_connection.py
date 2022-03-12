""" This File Content Walkerse PostgreSQL Database Connection """
from os import environ

from peewee import PostgresqlDatabase


def postgresql_database_connection() -> PostgresqlDatabase:
    """
    This Function Provide Connection To Walkerse PostgreSQL Database.
    :return:
    """
    database = PostgresqlDatabase(
        database=environ.get("POSTGRESQL_DATABASE_NAME"),
        user=environ.get("POSTGRESQL_USER"),
        password=environ.get("POSTGRESQL_PASSWORD"),
        host=environ.get("POSTGRESQL_DATABASE_HOST"),
        port=environ.get("POSTGRESQL_PORT")
    )

    return database
