from fastapi_basic import app


@app.get("/")
def home():
    return {"Hello": "World"}
