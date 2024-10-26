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

    _members: Mapped[list["UserEvent"]] = sqlalchemy.orm.relationship(
        "UserEvent", back_populates="_event"
    )


class UserEvent(Model):
    __tablename__ = "user_events"

    id: Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True, index=True)
    user_id: Mapped[int] = sqlalchemy.orm.mapped_column(ForeignKey('users.id'))
    event_id: Mapped[int] = sqlalchemy.orm.mapped_column(ForeignKey('events.id'))

    _user: Mapped["User"] = sqlalchemy.orm.relationship("User", back_populates="events")
    _event: Mapped["Event"] = sqlalchemy.orm.relationship("Event", back_populates="_members")

    __table_args__ = (UniqueConstraint('user_id', 'event_id', name='unique_user_event'),)
