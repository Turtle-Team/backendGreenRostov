from datetime import timedelta, datetime

import fastapi
import jwt
from fastapi import HTTPException
from sqlalchemy.orm import Session

import database
import setting
from database.user import User
from . import utils
from .models import UserWeb, JwtToken
from .utils import create_token
from .router import route


@route.post("/refresh")
def refresh_token(refresh: str):
    try:
        payload = jwt.decode(refresh, setting.SECRET_KEY, algorithms=[setting.ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
        access_token_expires = timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_token(data={"sub": username}, expires_delta=access_token_expires)
        refresh_token_expires = timedelta(days=setting.REFRESH_TOKEN_EXPIRE_DAYS)
        refresh_token = create_token(data={"sub": username}, expires_delta=refresh_token_expires)
        refresh_data = (datetime.now() + timedelta(setting.ACCESS_TOKEN_EXPIRE_MINUTES)).isoformat()
        jwt_data = models.JwtToken(access_token=access_token, refresh_token=refresh_token, exp=refresh_data)
        return jwt_data
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Refresh token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@route.post("/register")
def register_user(user: UserWeb):
    db: Session = database.Database().get_marker()
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    new_user = User(username=user.username, password=user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"username": new_user.username, "message": "User registered successfully"}


@route.post("/login")
def login(user: UserWeb, response: fastapi.Response):
    db: Session = database.Database().get_marker()
    db_user = db.query(User).filter(User.username == user.username and User.password == user.password).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    access_token_expires = timedelta(minutes=setting.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_token(data={"sub": db_user.username}, expires_delta=access_token_expires)

    refresh_token_expires = timedelta(days=setting.REFRESH_TOKEN_EXPIRE_DAYS)
    refresh_token = create_token(data={"sub": db_user.username}, expires_delta=refresh_token_expires)
    refresh_data = (datetime.now() + timedelta(setting.ACCESS_TOKEN_EXPIRE_MINUTES)).isoformat()
    response.headers.update({'Authorization': f'Bearer {access_token}'})
    response.set_cookie(key="refresh_token", value=refresh_token, httponly=True, expires=refresh_data)
    return models.JwtToken(access_token=access_token, refresh_token=refresh_token, exp=refresh_data)
