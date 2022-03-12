import logging
import peewee

from datetime import datetime

from models.postgresql.database_connection import postgresql_database_connection

DATABASE = postgresql_database_connection()

logger = logging.getLogger(__name__)


class Users(peewee.Model):
    id = peewee.AutoField(primary_key=True)
    name = peewee.CharField(max_length=50)
    surname = peewee.CharField(max_length=50)
    email = peewee.CharField(max_length=80)
    password = peewee.CharField(null=False)
    gender = peewee.SmallIntegerField(null=True)
    birthday = peewee.DateField(null=True)
    created_date = peewee.DateTimeField(default=datetime.now())
    updated_date = peewee.DateTimeField()
    status = peewee.SmallIntegerField()
    test_user = peewee.BooleanField(default=False)

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
        kwargs['updated_date'] = datetime.now()

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
        except peewee.DoesNotExist:
            message = "User does not exist"

            logger.warning(msg=message)

            return {}
