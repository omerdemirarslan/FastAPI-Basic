from src.fastapi_basic import app, Request


from src.users.user_service import UserService


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
    user_converted_data = await user_post_data.json()

    new_user_data = UserService()
    new_user_data.authentication(user_data=user_converted_data)

    return new_user_data


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
