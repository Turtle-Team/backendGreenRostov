import random
import typing

from sqlalchemy.orm import Session
from .route import route
from database.advice import Advice
import database
from . import models


# Роутинг для событий
@route.post("/")
def create_event() -> models.RandomAdvice:
    db: Session = database.Database().get_marker()
    all_advices = db.query(Advice).all()
    advice = random.choice(all_advices)
    advice = models.RandomAdvice(id=advice.id, name=advice.name, description=advice.description)
    return advice