from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from ..model import Model


class Event(Model):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    members = relationship("UserEvent", back_populates="event")


class UserEvent(Model):
    __tablename__ = "user_events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    event_id = Column(Integer, ForeignKey('events.id'))

    user = relationship("User", back_populates="events")
    event = relationship("Event", back_populates="members")

    __table_args__ = (UniqueConstraint('user_id', 'event_id', name='unique_user_event'),)
