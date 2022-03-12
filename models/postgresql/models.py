import logging

from datetime import datetime

from models.postgresql.database_connection import postgresql_database_connection

from sqlalchemy import Column, Integer, VARCHAR, Text, SmallInteger, Date, DateTime, Boolean

DATABASE = postgresql_database_connection()

logger = logging.getLogger(__name__)


class Users(DATABASE):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(VARCHAR)
    surname = Column(VARCHAR)
    email = Column(VARCHAR)
    password = Column(Text, nullable=True)
    gender = Column(SmallInteger, nullable=True)
    birthday = Column(Date, nullable=True)
    created_date = Column(DateTime, default=datetime.now())
    updated_date = Column(DateTime)
    status = Column(SmallInteger)
    test_user = Column(Boolean, default=False)

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
            logger.warning(msg=err)

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
        except Exception as err:
            print(err)
            message = "User does not exist"

            logger.warning(msg=message)

            return {}
