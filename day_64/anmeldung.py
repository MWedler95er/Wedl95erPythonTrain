from fastapi import Depends, FastAPI, HTTPExeption, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import pydantic
import datetime
import jose
import passlib.context



app = FastAPI()