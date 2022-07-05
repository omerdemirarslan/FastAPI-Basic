from fastapi import (
    FastAPI, Request, status
)

from dotenv import load_dotenv


load_dotenv()

app = FastAPI()
