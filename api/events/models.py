import pydantic
from typing import List


class EventCreate(pydantic.BaseModel):
    name: str
    description: str
    latitude: float
    longitude: float
    picture: str


class RegisterEvent(pydantic.BaseModel):
    event_id: int


class Member(pydantic.BaseModel):
    first_name: str
    last_name: str
    patronymic: str

class EventMembersResponse(pydantic.BaseModel):
    event_id: int
    members: List[Member]

class EventsResponse(pydantic.BaseModel):
    id: int
    name: str
    description: str
    latitude: float
    longitude: float
    picture: str | None = None
