""" User Base Helper File For All Helper Functions """
import logging

from typing import Any
from src.fastapi_basic import (
    Union,
    datetime,
    timedelta,
    status,
    JWTError,
    jwt,
    CryptContext,
)

from src.models.models import Users
from src.helpers.constant_variables import (
    HTTP_200_OK_EXIST_USER_MESSAGE,
    HTTP_200_OK_AUTHENTICATION_SUCCESS_MESSAGE,
    HTTP_201_CREATED_MESSAGE,
    HTTP_204_NO_CONTENT_MESSAGE,
    HTTP_400_BAD_REQUEST_MESSAGE,
    HTTP_401_UNAUTHORIZED_MESSAGE,
    HTTP_403_FORBIDDEN_MESSAGE,
    HTTP_404_NOT_FOUND_MESSAGE,
    NO_DATA_MESSAGE,
    JWT_SECRET_KEY,
    HASH_ALGORITHM,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

logger = logging.getLogger(__name__)


class UserService:
    """User Base Helper Class"""

    def __init__(self, user_data: dict):
        self.user_data = user_data
        self.user_email = user_data["email"]
        self.user_password = user_data["password"]
        self.user_auth = {"authentication": True, "token": "No Token"}
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def authenticate_user(email: str) -> dict:
        """
        This Method Authenticates User Info. If User Exist Return User All Data, It Is Not Returns Empty Dict Data
        @param email:
        @return:
        """
        user_as_dict = Users.get_as_dict(email=email)
        constant_values = {
            "status": status.HTTP_200_OK,
            "message": HTTP_200_OK_EXIST_USER_MESSAGE,
        }

        return constant_values | user_as_dict

    def get_or_create(self) -> dict:
        """
        This Method Get User or User Create and Return User Info Data
        :return: dict
        """
        user_detail = self.authenticate_user(email=self.user_email)

        if not user_detail["data"]:
            try:
                hashed_password = self.create_hashed_password(
                    password=self.user_password
                )
                self.user_data.update(password=hashed_password)

                new_user = Users.user_create(user_data=self.user_data)

                if new_user:
                    new_user_data = Users.get_as_dict(id=new_user)

                    if new_user_data["data"]:
                        user_detail.update(
                            status=status.HTTP_201_CREATED,
                            message=HTTP_201_CREATED_MESSAGE,
                            data=new_user_data,
                        )

                        return user_detail
                    else:
                        user_detail.update(
                            status=status.HTTP_204_NO_CONTENT,
                            message=HTTP_204_NO_CONTENT_MESSAGE,
                            data=new_user_data,
                        )

                        self.user_auth.update(authentication=False)

                        return user_detail
                else:
                    user_detail.update(
                        status=status.HTTP_403_FORBIDDEN,
                        message=HTTP_403_FORBIDDEN_MESSAGE,
                        data=new_user,
                    )

                    self.user_auth.update(authentication=False)

                    return user_detail
            except Exception as error:
                logger.warning(msg=error)

                user_detail.update(
                    status=status.HTTP_400_BAD_REQUEST,
                    message=HTTP_400_BAD_REQUEST_MESSAGE,
                    data=NO_DATA_MESSAGE,
                )

                return user_detail
        else:
            return user_detail

    def create_hashed_password(self, password: str) -> str:
        """
        This Method Creates Hashed Password By Context.
        @param password: User's Password.
        @return: Hashed Password.
        """
        return self.pwd_context.hash(secret=password)

    def verify_password(self, requested_password: str, hashed_password: str):
        """
        This Method Compare Password In The Requested Data and Database User Models.
        If Both of Them Equal It Returns True
        @param requested_password:
        @param hashed_password:
        @return:
        """
        return self.pwd_context.verify(
            secret=requested_password, hash=hashed_password
        )

    @staticmethod
    def create_access_token(subject: Union[str, Any]) -> str:
        """
        This Method Creates JWT Token.
        @param subject:
        @return: Token.
        """
        expires_token_time = datetime.utcnow() + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )

        to_encode = {"exp": expires_token_time, "sub": str(subject)}
        encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, HASH_ALGORITHM)

        return encoded_jwt

    def user_login(self) -> dict:
        """
        This Method Handle User Authentication. If User Login Success Return User Info With Token.
        @return:
        @rtype:
        """
        user_detail = self.authenticate_user(email=self.user_email)

        if not user_detail["data"]:
            user_detail.update(
                status=status.HTTP_404_NOT_FOUND,
                message=HTTP_404_NOT_FOUND_MESSAGE,
                data=NO_DATA_MESSAGE,
            )

            self.user_auth.update(authentication=False)

            return user_detail | self.user_auth

        get_hashed_password = Users.get_user_hashed_password(
            email=self.user_email
        )
        verify_password = self.verify_password(
            requested_password=self.user_password,
            hashed_password=get_hashed_password["password"],
        )

        if verify_password:
            try:
                new_token = self.create_access_token(self.user_email)

                user_detail.update(
                    status=status.HTTP_200_OK,
                    message=HTTP_200_OK_AUTHENTICATION_SUCCESS_MESSAGE,
                )

                self.user_auth.update(token=new_token)

                return user_detail | self.user_auth
            except JWTError:
                user_detail.update(
                    status=status.HTTP_401_UNAUTHORIZED,
                    message=HTTP_401_UNAUTHORIZED_MESSAGE,
                    data=NO_DATA_MESSAGE,
                )

                self.user_auth.update(authentication=False)

                return user_detail | self.user_auth
            except Exception as error:
                logger.warning(msg=str(error))

                user_detail.update(
                    status=status.HTTP_401_UNAUTHORIZED,
                    message=HTTP_401_UNAUTHORIZED_MESSAGE,
                    data=NO_DATA_MESSAGE,
                )

                self.user_auth.update(authentication=False)

                return user_detail | self.user_auth
        else:
            user_detail.update(
                status=status.HTTP_404_NOT_FOUND,
                message=HTTP_404_NOT_FOUND_MESSAGE,
                data=NO_DATA_MESSAGE,
            )

            self.user_auth.update(authentication=False)

            return user_detail | self.user_auth
