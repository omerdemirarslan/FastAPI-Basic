""" User Base Helper File For All Helper Functions """
import logging

from fastapi_basic import status
from models.postgresql.models import Users

logger = logging.getLogger(__name__)


class UserBaseHelper:
    """ User Base Helper Class """

    @classmethod
    def get_or_create(cls, user_data: dict) -> dict:
        """
        This Method Get User or User Create and Return User Info Data
        :param user_data:
        :return: dict
        """
        user_email = user_data["email"]
        user_auth = {"authentication": True}
        response_status = {"status": status.HTTP_200_OK}

        user_info = Users.get_as_dict(email=user_email)

        if not user_info:

            try:
                user = Users.create(
                    name=user_data["name"],
                    surname=user_data["surname"],
                    email=user_email
                )

                response_status["status"] = status.HTTP_201_CREATED
                user_info = Users.get_as_dict(id=user)
            except Exception as e:
                logger.warning(msg=e)

                user_auth["authentication"] = False
                response_status["status"] = status.HTTP_401_UNAUTHORIZED

        user_detail = {
            "status": response_status,
            "data": {
                "user": {
                            "id": user_info["id"],
                            "name": user_info["name"],
                            "surname": user_info["surname"],
                            "email": user_info["email"],
                            "gender": user_info["gender"],
                            "birthday": user_info["birthday"],
                            "status": user_info["status"],
                            "test_user": user_info["test_user"]
                        } | user_auth
            }
        }

        return user_detail

    @classmethod
    def authentication(cls, user_data: dict) -> dict:
        """
        This Method Return User Data With Authentication Information
        :param user_data:
        :return: dict
        """
        user_detail = cls.get_or_create(
            user_data=user_data
        )

        if not user_detail["authentication"]:
            return user_detail | {"authentication_token": None}
        return user_detail | {"authentication_token": "some key"}
