from datetime import timedelta
import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from api.user import utils
from .route import route
from database.events import Event, UserEvent
from database.user import User
import database


# Роутинг для событий
@route.post("/create")
def create_event(event: models.EventCreate, user: dict = fastapi.Depends(utils.get_current_user)):
    new_event = Event()
    new_event.name = event.name
    new_event.description = event.description
    new_event.latitude = event.latitude
    new_event.longitude = event.longitude
    db: Session = database.Database().get_marker()
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event


@route.post("/register")
def register_user_to_event(registration: models.RegisterEvent, user: dict = fastapi.Depends(utils.get_current_user)):
    db: Session = database.Database().get_marker()
    user_exists = db.query(User).filter(User.id == registration.user_id).first()
    if not user_exists:
        raise HTTPException(status_code=400, detail="User does not exist.")

    existing_registration = db.query(UserEvent).filter(
        UserEvent.user_id == registration.user_id,
        UserEvent.event_id == registration.event_id
    ).first()

    if existing_registration:
        raise HTTPException(status_code=400, detail="User is already registered for this event.")

    user_event = UserEvent(user_id=registration.user_id, event_id=registration.event_id)
    db.add(user_event)
    db.commit()
    db.refresh(user_event)

    return user_event


@route.get("/members/{event_id}", response_model=models.EventMembersResponse)
def get_event_members(event_id: int, user: dict = fastapi.Depends(utils.get_current_user)):
    db: Session = database.Database().get_marker()
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    members = db.query(User).join(UserEvent).filter(UserEvent.event_id == event_id).all()
    member_list = [models.Member(first_name=member.first_name, last_name=member.last_name, patronymic=member.patronymic) for member in members]

    return models.EventMembersResponse(event_id=event_id, members=member_list)

@route.get("/users/")
def get_users(db: Session = Depends(Event)):
    users = db.query(User).all()
    return users


# @route.get("/events/")
# def get_events(db: Session = Depends(Event)):
#     events = db.query(models.Event).all()
#     return events
