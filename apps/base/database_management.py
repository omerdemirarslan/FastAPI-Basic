""" This File Contains FastAPI Basic Database Management Process """
import logging

from os import getenv

from playhouse.migrate import PostgresqlDatabase, PostgresqlMigrator

logger = logging.getLogger(__name__)


class DatabaseManagement:

    def __init__(self):
        self.database = self.postgresql_database_connection()
        self.migrator = PostgresqlMigrator(database=self.database)

    def __enter__(self):
        """
        This Method Provides Database Connection Process Before Requests
        :return:
        """
        self.database.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        This Method Provides Database Connection Close Process After Requests
        :return:
        """
        self.database.close()


    def postgresql_database_connection(self) -> PostgresqlDatabase:
        """
        This Function Provide Connection To Platform Integration Postgresql Database.
        :return: models connection
        """
        try:
            database = PostgresqlDatabase(
                database=getenv("POSTGRES_DB"),
                user=getenv("POSTGRES_USER"),
                password=getenv("POSTGRES_PASSWORD"),
                host=getenv("POSTGRES_HOST"),
                port=getenv("POSTGRESQL_PORT")
            )

            return database
        except Exception as error:
            logger.error(msg=error)

    def postgresql_create_tables(self) -> bool:
        """
        This Method Creates Necessary Postgresql Models For Platform Integration.
        :return:
        """
        from apps.users.models import Users

        try:
            with self.database:
                self.database.create_tables(
                    [Users]
                )

                return True
        except Exception as error:
            logger.error(msg=error)

            return False

    def postgresql_migrate_tables(self) -> bool:
        """

        :return:
        """
        try:
            with self.database:
                pass
                """migrate(
                    self.migrator.add_column("account_integration_configs", "test", test)
                )"""

            return True
        except Exception as error:
            logger.error(msg=error)

            return False
