from fastapi_basic import app, Request


from utility.helper.users import UserBaseHelper


@app.post("/api/v1/users/register", tags=["user Register"])
def user_register(user_post_data: Request):
    """
    This Method Handle User Register Requests
    :param user_post_data:
    :return:
    """
    user_converted_data = await user_post_data.json()

    user_info_data = UserBaseHelper.authentication(user_data=user_converted_data)

    return user_info_data


@app.patch("/api/v1/users/update", tags=["user Update"])
def user_update(user_post_data: Request):
    """
    This Method Handle User Update Requests
    :param user_post_data:
    :return:
    """
    user_converted_data = await user_post_data.json()

    return user_converted_data


@app.get("/api/v1/users/get", tags=["user Get"])
def user_update(user_post_data: Request):
    """
    This Method Handle User Get Requests
    :param user_post_data:
    :return:
    """
    user_converted_data = await user_post_data.json()

    return user_converted_data
