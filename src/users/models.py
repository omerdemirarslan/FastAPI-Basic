import logging

import datetime

from peewee import AutoField, CharField, SmallIntegerField, DateField, DateTimeField, BooleanField, DoesNotExist

from src.base.database_management import DatabaseManagement
from src.base.models import BaseModel

DATABASE = DatabaseManagement()

logger = logging.getLogger(__name__)


class Users(BaseModel):
    id = AutoField(primary_key=True)
    name = CharField(max_length=50)
    surname = CharField(max_length=50)
    email = CharField(max_length=80)
    password = CharField(null=False)
    gender = SmallIntegerField(null=True)
    birthday = DateField(null=True)
    updated_date = DateTimeField()
    status = SmallIntegerField()
    test_user = BooleanField(default=False)

    class Meta:
        table_name = "users"
        database = DATABASE

    @classmethod
    def update(cls, *args, **kwargs):
        """
        This Method Update updated_date When Get Option User Model
        :param args:
        :param kwargs:
        :return:
        """
        kwargs['updated_date'] = datetime.datetime.now()

        return super(Users, cls).save(*args, **kwargs)

    @classmethod
    def user_create(cls, user_data: dict) -> dict:
        """
        This Method Return User Info Data If User Exist or Return Empty Dict
        :param user_data: Expression
        :return: dict
        """
        try:
            user = Users.create(
                name=user_data["name"],
                surname=user_data["surname"],
                email=user_data["email"]
            )

            return user
        except Exception as err:
            message = err

            logger.warning(msg=message)

            return {}

    @classmethod
    def get_as_dict(cls, **expr) -> dict:
        """
        This Method Return User Info Data If User Exist or Return Empty Dict
        :param expr: Expression
        :return: dict
        """
        try:
            query = Users.select().where(*[getattr(Users, key) == value for key, value in expr.items()]).dicts()

            return query.get()
        except DoesNotExist:
            message = "User does not exist"

            logger.warning(msg=message)

            return {}
