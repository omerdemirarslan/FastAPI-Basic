""" User Base Helper File For All Helper Functions """
import logging

from src.fastapi_basic import status
from .models import Users

logger = logging.getLogger(__name__)


class UserService:
    """ User Base Helper Class """

    def __init__(self):
        self.user_auth = {"authentication": True, "authentication_token": ""}
        self.response_status = status.HTTP_200_OK

    def get_or_create(self, user_data) -> dict:
        """
        This Method Get User or User Create and Return User Info Data
        :return: dict
        """
        user_info = Users.get_as_dict(email=user_data["email"])

        if not user_info:
            try:
                user = Users.user_create(user_data=user_data)

                self.response_status = status.HTTP_201_CREATED

                user_info = Users.get_as_dict(id=user)
            except Exception as e:
                logger.warning(msg=e)

                self.user_auth["authentication"] = False
                self.response_status = status.HTTP_401_UNAUTHORIZED

                user_detail = {
                    "status": self.response_status,
                    "data": {
                        "There Is No Data."
                    }
                }

                return user_detail


        user_detail = {
            "status": self.response_status,
            "data": {
                "id": user_info["id"],
                "name": user_info["name"],
                "surname": user_info["surname"],
                "email": user_info["email"],
                "gender": user_info["gender"],
                "birthday": user_info["birthday"],
                "status": user_info["status"],
                "test_user": user_info["test_user"],
            }
        }

        return user_detail

    def authentication(self, user_data: dict) -> dict:
        """
        This Method Return User Data With Authentication Information
        :return: dict
        """
        user_detail = self.get_or_create(
            user_data=user_data
        )

        if not self.user_auth["authentication"]:
            return user_detail | self.user_auth

        self.user_auth["authentication_token"] = "some key"

        return user_detail | self.user_auth
