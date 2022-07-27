""" This File Contains Base Models For All Project """
import datetime

from peewee import Model, DateTimeField

from .database_management import DatabaseManagement


database_object = DatabaseManagement()


class BaseModel(Model):
    created_at = DateTimeField(null=False, default=datetime.datetime.now)

    class Meta:
        database = database_object.postgresql_database_connection()
        table_name = "basemodel"
