from fastapi import (
    FastAPI, Request, status, responses
)

from dotenv import load_dotenv


load_dotenv()

app = FastAPI()
