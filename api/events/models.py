import pydantic
from typing import List
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Column, String, Float, DateTime


class EventCreate(pydantic.BaseModel):
    name: str
    description: str
    latitude: float
    longitude: float


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
