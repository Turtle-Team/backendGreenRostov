from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint
import sqlalchemy.orm
from sqlalchemy.orm import Mapped
from ..model import Model


class Event(Model):
    __tablename__ = "events"

    id: Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True, index=True)
    name: Mapped[str] = sqlalchemy.orm.mapped_column(String, index=True)
    description: Mapped[str] = sqlalchemy.orm.mapped_column(String)
    latitude: Mapped[float] = sqlalchemy.orm.mapped_column(Float)
    longitude: Mapped[float] = sqlalchemy.orm.mapped_column(Float)


class UserEvent(Model):
    __tablename__ = "user_events"

    id: Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = sqlalchemy.orm.mapped_column(ForeignKey('users.id'))
    event_id: Mapped[int] = sqlalchemy.orm.mapped_column(ForeignKey('events.id'))

class EventsResponse(Model):
    id: int
    name: str
    description: str
    #date: datetime
    latitude: float
    longitude: float

