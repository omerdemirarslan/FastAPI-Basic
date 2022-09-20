import secrets

from typing import Union
from datetime import datetime, timedelta

from fastapi import FastAPI, Request, HTTPException, status, responses, Depends

from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from dotenv import load_dotenv


load_dotenv()

app = FastAPI()
