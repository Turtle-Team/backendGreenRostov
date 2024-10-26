import pydantic
from typing import List


class EventCreate(pydantic.BaseModel):
    name: str
    description: str
    latitude: float
    longitude: float


class RegisterEvent(pydantic.BaseModel):
    user_id: int
    event_id: int


class Member(pydantic.BaseModel):
    first_name: str
    last_name: str
    patronymic: str

# Обновляем класс ответа для участников события
class EventMembersResponse(pydantic.BaseModel):
    event_id: int
    members: List[Member]
