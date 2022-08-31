""" This File Contains Base Models For All Project """
import logging

import datetime

from peewee import (
    Model, AutoField, DateTimeField, CharField, SmallIntegerField, DateField, BooleanField, DoesNotExist
)

from src.base.database_management import DatabaseManagement


LOGGER = logging.getLogger(__name__)
DATABASE_OBJECT = DatabaseManagement()


class BaseModel(Model):
    id = AutoField(primary_key=True)
    created_at = DateTimeField(null=False, default=datetime.datetime.now)
    updated_date = DateTimeField(null=False, default=datetime.datetime.now)

    class Meta:
        database = DATABASE_OBJECT.postgresql_database_connection()
        table_name = "basemodel"


class Users(BaseModel):
    name = CharField(max_length=50)
    surname = CharField(max_length=50)
    email = CharField(max_length=80)
    password = CharField(null=False)
    gender = SmallIntegerField(null=True)
    birthday = DateField(null=True)
    status = SmallIntegerField(default=1)
    test_user = BooleanField(default=False)

    class Meta:
        table_name = "users"

    @classmethod
    def update(cls, __data=None, **update):
        """
        This Method Update updated_date When Get Option User Model
        :param __data:
        :param update:
        :return:
        """
        update['updated_date'] = datetime.datetime.now()

        return super(Users, cls).update(__data, **update)

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
                email=user_data["email"],
                password=user_data["password"]
            )

            return user
        except Exception as error:
            LOGGER.warning(msg=str(error))

            return {}

    @classmethod
    def get_as_dict(cls, **expr) -> dict:
        """
        This Method Return User Info Data If User Exist or Return Empty Dict
        :param expr: Expression
        :return: dict
        """
        result = {"data": None}

        try:
            query = Users.select(
                Users.id,
                Users.name,
                Users.surname,
                Users.email,
                Users.gender,
                Users.birthday,
                Users.status,
                Users.test_user
            ).where(
                *[getattr(Users, key) == value for key, value in expr.items()]
            ).dicts()

            result.update(
                data=query.get()
            )
            return result
        except DoesNotExist:
            message = "User Does Not Exist"

            LOGGER.warning(msg=message)

            return result
