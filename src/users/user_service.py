""" User Base Helper File For All Helper Functions """
import logging

from src.fastapi_basic import status
from src.models.models import Users

logger = logging.getLogger(__name__)


class UserService:
    """ User Base Helper Class """

    def __init__(self, user_data: dict):
        self.request_data = user_data
        self.user_auth = {"authentication": True, "authentication_token": None}
        self.response_status = status.HTTP_200_OK
        self.message = "User Already Exist! User Info Is Here"

    def get_user_info_result(self):
        """

        """
        user_as_dict = Users.get_as_dict(email=self.request_data["email"])
        result = {
            "status": self.response_status,
            "message": self.message,
        }

        if user_as_dict["data"]:
            return result | user_as_dict
        else:
            return result | user_as_dict


    def get_or_create(self) -> dict:
        """
        This Method Get User or User Create and Return User Info Data
        :return: dict
        """
        user_detail = self.get_user_info_result()

        if not user_detail["data"]:
            try:
                user = Users.user_create(user_data=self.request_data)

                user_detail.update(
                    status=status.HTTP_201_CREATED,
                    message="User Creation Success",
                    data=Users.get_as_dict(id=user)
                )
                return user_detail
            except Exception as error:
                logger.warning(msg=error)

                self.user_auth["authentication"] = False

                self.message = "There Is An Error! Authorization Is Not Success. Please Try Again Letter"

                user_detail.update(
                    status=status.HTTP_401_UNAUTHORIZED,
                    message="There Is An Error! Authorization Is Not Success. Please Try Again Letter",
                    data="There Is No Data."
                )

                return user_detail
        else:
            return user_detail
