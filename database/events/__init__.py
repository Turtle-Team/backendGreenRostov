from sqlalchemy import Column, Integer, String, Float, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship

from ..model import Model

#TODO Это нихуя не работает. надо переделать и использованием зависимостей как в патруле (patrol).
# При попытка запуска с этим кодом крашится основной проект

# class Event(Model):
#     __tablename__ = "events"
#
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(String)
#     latitude = Column(Float)
#     longitude = Column(Float)
#
#     _members = relationship("UserEvent", back_populates="event")
#
#
# class UserEvent(Model):
#     __tablename__ = "user_events"
#
#     id = Column(Integer, primary_key=True, index=True)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     event_id = Column(Integer, ForeignKey('events.id'))
#
#     _user = relationship("User", back_populates="events")
#     _event = relationship("Event", back_populates="members")
#
#     __table_args__ = (UniqueConstraint('user_id', 'event_id', name='unique_user_event'),)
