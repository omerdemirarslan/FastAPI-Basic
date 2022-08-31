""" User Base Helper File For All Helper Functions """
import logging

from src.fastapi_basic import status
from src.models.models import Users

logger = logging.getLogger(__name__)


class UserService:
    """ User Base Helper Class """

    def __init__(self):
        self.user_auth = {"authentication": True, "authentication_token": ""}
        self.response_status = status.HTTP_200_OK
        self.message = "User Already Exist! User Info Is Here"

    def get_or_create(self, user_data) -> dict:
        """
        This Method Get User or User Create and Return User Info Data
        :return: dict
        """
        get_user = Users.get_as_dict(email=user_data["email"])

        if not get_user:
            try:
                user = Users.user_create(user_data=user_data)

                self.response_status = status.HTTP_201_CREATED

                get_user = Users.get_as_dict(id=user)
                self.message = "User Creation Success"
            except Exception as error:
                logger.warning(msg=error)

                self.user_auth["authentication"] = False
                self.response_status = status.HTTP_401_UNAUTHORIZED
                self.message = "There Is An Error! Authorization Is Not Success. Please Try Again Letter"

                user_detail = {
                    "status": self.response_status,
                    "message": self.message,
                    "data": {
                        "There Is No Data."
                    }
                }

                return user_detail

        user_detail = {
            "status": self.response_status,
            "message": self.message,
            "data": {
                "id": get_user["id"],
                "name": get_user["name"],
                "surname": get_user["surname"],
                "email": get_user["email"],
                "gender": get_user["gender"],
                "birthday": get_user["birthday"],
                "status": get_user["status"],
                "test_user": get_user["test_user"],
            }
        }

        return user_detail

    def user_register(self, user_data: dict) -> dict:
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
