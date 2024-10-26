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
    user_id: int
    event_id: int


class Member(pydantic.BaseModel):
    first_name: str
    last_name: str
    patronymic: str

class EventMembersResponse(pydantic.BaseModel):
    event_id: int
    members: List[Member]

class Event(pydantic.BaseModel):
    __tablename__ = "events"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    description: Mapped[str] = mapped_column(String)
    #date: Mapped[datetime] = mapped_column(DateTime)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
