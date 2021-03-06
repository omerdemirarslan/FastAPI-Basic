import logging

from src.fastapi_basic import app, Request, responses, status

from src.users.user_service import UserService


logger = logging.getLogger(__name__)


@app.get("/")
async def home():
    """
    This Method Get Home Page
    """
    return {"message": "Hello World"}



@app.post("/api/v1/users/register", tags=["user Register"])
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
            content={
                "message": "Sent Data Type Must Be JSON"
            }

        )

    if isinstance(user_converted_data, dict):
        try:
            user = UserService()
            user_info = user.authentication(user_data=user_converted_data)

            return responses.JSONResponse(
                user_info
            )
        except Exception as error:
            logger.error(error)

            return responses.JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={
                    "message": "There Is An Error."
                }
            )
    else:
        return responses.JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": "Sent Data Type Must Be JSON"
            }
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
