from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models
from .database import SessionLocal, engine
from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)

app = FastAPI()



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/event/create")
def create_event(event: EventCreate, db: Session = Depends(get_db)):
    new_event = models.Event(**event.dict())
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event


@app.post("/event/register")
def register_user_to_event(registration: RegisterEvent, db: Session = Depends(get_db)):
    user_exists = db.query(models.User).filter(models.User.id == registration.user_id).first()
    if not user_exists:
        raise HTTPException(status_code=400, detail="User does not exist.")

    existing_registration = db.query(models.UserEvent).filter(
        models.UserEvent.user_id == registration.user_id,
        models.UserEvent.event_id == registration.event_id
    ).first()

    if existing_registration:
        raise HTTPException(status_code=400, detail="User is already registered for this event.")

    user_event = models.UserEvent(user_id=registration.user_id, event_id=registration.event_id)
    db.add(user_event)
    db.commit()
    db.refresh(user_event)

    return user_event


@app.get("/event/members/{event_id}", response_model=EventMembersResponse)
def get_event_members(event_id: int, db: Session = Depends(get_db)):
    event = db.query(models.Event).filter(models.Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    members = db.query(models.User).join(models.UserEvent).filter(models.UserEvent.event_id == event_id).all()
    return EventMembersResponse(event_id=event_id, members=[member.name for member in members])
@app.get("/users/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.get("/events/")
def get_events(db: Session = Depends(get_db)):
    events = db.query(models.Event).all()
    return events

