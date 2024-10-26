import datetime

import pydantic


class UserWeb(pydantic.BaseModel):
    username: str
    password: str
    first_name: str = pydantic.Field(None)
    last_name: str = pydantic.Field(None)
    patronymic: str = pydantic.Field(None)
    british_date: datetime.datetime = pydantic.Field(None)

class UserAuth(pydantic.BaseModel):
    username: str
    password: str

class JwtToken(pydantic.BaseModel):
    token_type: str = pydantic.Field(default='Bearer')
    access_token: str = pydantic.Field()
    refresh_token: str = pydantic.Field()
    exp: str = pydantic.Field(default=None)
