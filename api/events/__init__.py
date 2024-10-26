from datetime import timedelta
import fastapi
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from api.user import utils
from .route import route
from database.events import Event, UserEvent
import database


# Роутинг для событий
@route.post("/event/create")
def create_event(event: models.EventCreate, user: dict = fastapi.Depends(utils.get_current_user)):
    new_event = models.Event(**event.dict())
    user.add(new_event)
    user.commit()
    user.refresh(new_event)
    return new_event


@route.post("/event/register")
def register_user_to_event(registration: models.RegisterEvent, user: dict = fastapi.Depends(utils.get_current_user)):
    user_exists = user.query(models.User).filter(models.User.id == registration.user_id).first()
    if not user_exists:
        raise HTTPException(status_code=400, detail="User does not exist.")

    existing_registration = user.query(models.UserEvent).filter(
        models.UserEvent.user_id == registration.user_id,
        models.UserEvent.event_id == registration.event_id
    ).first()

    if existing_registration:
        raise HTTPException(status_code=400, detail="User is already registered for this event.")

    user_event = models.UserEvent(user_id=registration.user_id, event_id=registration.event_id)
    user.add(user_event)
    user.commit()
    user.refresh(user_event)

    return user_event


@route.get("/event/members/{event_id}", response_model=models.EventMembersResponse)
def get_event_members(event_id: int, user: dict = fastapi.Depends(utils.get_current_user)):
    event = user.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    members = user.query(models.User).join(models.UserEvent).filter(models.UserEvent.event_id == event_id).all()
    return models.EventMembersResponse(event_id=event_id, members=[member.name for member in members])


@route.get("/users/")
def get_users(db: Session = Depends(Event)):
    users = db.query(models.User).all()
    return users


@route.get("/events/")
def get_events(db: Session = Depends(Event)):
    events = db.query(models.Event).all()
    return events
