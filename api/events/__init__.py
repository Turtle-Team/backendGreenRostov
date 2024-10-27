import typing

import fastapi
from fastapi import HTTPException
from sqlalchemy.orm import Session

import database
from api.events.models import EventsResponse
from api.user import utils
from database.events import Event, UserEvent
from database.user import User
from . import models
from .route import route


# Роутинг для событий
@route.post("/create")
def create_event(event: models.EventCreate, user: dict = fastapi.Depends(utils.get_current_user)):
    new_event = Event()
    new_event.name = event.name
    new_event.description = event.description
    new_event.latitude = event.latitude
    new_event.longitude = event.longitude
    new_event.picture = event.picture
    db: Session = database.Database().get_marker()
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event


@route.post("/register")
def register_user_to_event(registration: models.RegisterEvent, user: dict = fastapi.Depends(utils.get_current_user)):
    db: Session = database.Database().get_marker()
    user_exists = db.query(User).filter(User.id == user['id']).first()
    if not user_exists:
        raise HTTPException(status_code=400, detail="User does not exist.")

    existing_registration = db.query(UserEvent).filter(UserEvent.user_id == user['id'],
                                                       UserEvent.event_id == registration.event_id).first()

    if existing_registration:
        raise HTTPException(status_code=400, detail="User is already registered for this event.")

    user_event = UserEvent(user_id=user['id'], event_id=registration.event_id)
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
    # member_list = [models.Member(first_name=member.first_name, last_name=member.last_name, patronymic=member.patronymic) for member in members]
    member_list = [models.Member(first_name=member.username, last_name=member.username, patronymic=member.username) for
                   member in members]

    return models.EventMembersResponse(event_id=event_id, members=member_list)


@route.get("/my")
def get_event_members(user: dict = fastapi.Depends(utils.get_current_user)):
    db: Session = database.Database().get_marker()
    event = db.query(UserEvent).filter(UserEvent.user_id == user['id']).all()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    events_ids = list(map(lambda x: x.event_id, event))
    events = db.query(Event).filter(Event.id.in_(events_ids)).all()
    return events


@route.get("/all")
def get_events(user: dict = fastapi.Depends(utils.get_current_user)) -> typing.List[EventsResponse]:
    db: Session = database.Database().get_marker()
    events = db.query(Event).all()
    data = []
    for event in events:
        e = EventsResponse(id=event.id, name=event.name, description=event.description, latitude=event.latitude,
                           longitude=event.longitude, picture=event.picture)
        data.append(e)
    return data
