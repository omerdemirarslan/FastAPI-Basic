from fastapi_basic import app, Request


@app.get("/api/v1/users/register", tags=["user register"])
def user_register(user_post_data: Request):
    """
    This method Handle User Register Requests
    :param user_post_data:
    :return:
    """
    user_converted_data = await user_post_data.json()

    return user_converted_data
