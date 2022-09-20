import logging

from src.fastapi_basic import (
    app,
    Request,
    responses,
    status,
    Depends,
    OAuth2PasswordBearer,
)

from src.users.user_service import UserService
from src.helpers.constant_variables import (
    HTTP_400_BAD_REQUEST_REQUIRE_FIELD_MESSAGE,
    HTTP_405_METHOD_NOT_ALLOWED_MESSAGE,
    HTTP_400_BAD_REQUEST_JSON_TYPE_MESSAGE,
)


logger = logging.getLogger(__name__)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@app.get("/")
async def home():
    """
    This Method Get Home Page
    """
    return {"message": "Hello World"}


@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


@app.post("/api/v1/users/register", tags=["User Register"])
async def user_register(user_post_data: Request):
    """
    This Method Handle User Register Requests
    :param user_post_data:
    :return:
    """
    try:
        user_converted_data = await user_post_data.json()
    except Exception as error:
        logger.error(error)

        return responses.JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": HTTP_400_BAD_REQUEST_JSON_TYPE_MESSAGE},
        )

    if isinstance(user_converted_data, dict):
        if user_converted_data:
            try:
                user = UserService(user_data=user_converted_data)
                user_info = user.get_or_create()

                return responses.JSONResponse(user_info)
            except Exception as error:
                logger.error(error)

                return responses.JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={
                        "message": HTTP_400_BAD_REQUEST_REQUIRE_FIELD_MESSAGE
                    },
                )
        else:
            return responses.JSONResponse(
                status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                content={"message": HTTP_405_METHOD_NOT_ALLOWED_MESSAGE},
            )
    else:
        return responses.JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": HTTP_400_BAD_REQUEST_JSON_TYPE_MESSAGE},
        )


@app.post("/api/v1/users/login", tags=["User Login"])
async def user_login(user_post_data: Request):
    """
    This Method Handle User Login Requests
    @param user_post_data:
    @return:
    """
    try:
        user_converted_data = await user_post_data.json()
    except Exception as error:
        logger.error(error)

        return responses.JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": HTTP_400_BAD_REQUEST_JSON_TYPE_MESSAGE},
        )

    if isinstance(user_converted_data, dict):
        if user_converted_data:
            try:
                user = UserService(user_data=user_converted_data)
                user_info = user.user_login()

                return responses.JSONResponse(user_info)
            except Exception as error:
                logger.error(error)

                return responses.JSONResponse(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    content={
                        "message": HTTP_400_BAD_REQUEST_REQUIRE_FIELD_MESSAGE
                    },
                )
        else:
            return responses.JSONResponse(
                status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                content={"message": HTTP_405_METHOD_NOT_ALLOWED_MESSAGE},
            )
    else:
        return responses.JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": HTTP_400_BAD_REQUEST_JSON_TYPE_MESSAGE},
        )


@app.patch("/api/v1/users/update", tags=["user Update"])
def user_update(user_post_data: Request):
    """
    This Method Handle User Update Requests
    :param user_post_data:
    :return:
    """
    user_converted_data = user_post_data.json()

    return user_converted_data


@app.get("/api/v1/users/get", tags=["user Get"])
def user_update(user_post_data: Request):
    """
    This Method Handle User Get Requests
    :param user_post_data:
    :return:
    """
    user_converted_data = user_post_data.json()

    return user_converted_data
