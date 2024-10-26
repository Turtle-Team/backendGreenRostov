import typing
import fastapi
from sqlalchemy.orm import Session
from . import models
from api.user import utils
from .route import route
from database.operations import Operation
import database

@route.get("/all", response_model=typing.List[models.OperationResponse])
def get_operations(user: dict = fastapi.Depends(utils.get_current_user)) -> typing.List[models.OperationResponse]:
    db: Session = database.Database().get_marker()
    operations = db.query(Operation).filter_by(user=user["id"]).all()
    data = []
    for operation in operations:
        op = models.OperationResponse(
            id=operation.id,
            retailPlace=operation.retailPlace,
            ecashTotalSum=operation.ecashTotalSum,
            totalSum=operation.totalSum,
            date_time=operation.date_time,
            user=operation.user
        )
        data.append(op)
    return data
