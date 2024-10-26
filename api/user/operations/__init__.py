import typing
import fastapi
from sqlalchemy.orm import Session
from . import models
from api.user import utils
from .route import route
from database.operations import Operation
import database

@route.get("/all")
def get_operations(user: dict = fastapi.Depends(utils.get_current_user)):
    db: Session = database.Database().get_marker()
    operations = db.query(Operation).filter(Operation.user_id == user["id"]).all()
    data = []
    for operation in operations:
        data.append(operation)
    return data
