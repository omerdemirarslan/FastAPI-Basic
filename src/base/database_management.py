""" This File Contains FastAPI Basic Database Management Process """
import logging

from os import getenv, path

from peewee import PostgresqlDatabase
from peewee_migrate import Router

logger = logging.getLogger(__name__)


MIGRATION_FOLDER_PATH = path.abspath(
    path.join(path.dirname(__file__), "..", "migrations")
)


class DatabaseManagement:
    def __init__(self):
        self.database = self.postgresql_database_connection()
        self.router = Router(
            database=self.database,
            ignore=["basemodel"],
            migrate_dir=MIGRATION_FOLDER_PATH,
        )

    @classmethod
    def postgresql_database_connection(cls) -> PostgresqlDatabase:
        """
        This Function Provide Connection To FastAPI Basic Postgresql Database.
        :return: models connection
        """
        try:
            database = PostgresqlDatabase(
                database=getenv("POSTGRES_DB"),
                user=getenv("POSTGRES_USER"),
                password=getenv("POSTGRES_PASSWORD"),
                host=getenv("POSTGRES_HOST"),
                port=getenv("POSTGRESQL_PORT"),
            )

            return database
        except Exception as error:
            logger.error(msg=error)

    def postgresql_create_tables(self) -> bool:
        """
        This Method Creates Necessary Postgresql Models For FastAPI Basic
        :return:
        """
        from src.models.models import Users

        try:
            with self.database:
                self.database.create_tables([Users])

                return True
        except Exception as error:
            logger.error(msg=error)

            return False

    def postgresql_migrate_tables(self) -> bool:
        """
        This Method Creates Necessary Migration Auto For All Models.
        :return:
        """
        try:
            with self.database:
                self.router.create(auto=True)
                self.router.run()

                return True
        except Exception as error:
            logger.error(msg=error)

            return False
