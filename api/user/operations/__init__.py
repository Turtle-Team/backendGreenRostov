import typing
import fastapi
from sqlalchemy.orm import Session
from . import models
from api.user import utils
from .route import route
from database.operations import Operation, OperationBillData
import database

@route.get("/all")
def get_operations(user: dict = fastapi.Depends(utils.get_current_user)) -> typing.List[models.Operation]:
    db: Session = database.Database().get_marker()
    operations = db.query(Operation).filter(Operation.user_id == user["id"]).all()
    op_ids = list(map(lambda x: x.id, operations))
    operations_bill = db.query(OperationBillData).filter(OperationBillData.operation_id.in_(op_ids)).all()

    bills_by_operation = {}
    for bill in operations_bill:
        if bill.operation_id not in bills_by_operation:
            bills_by_operation[bill.operation_id] = []
        bills_by_operation[bill.operation_id].append(models.OperationBillData(**bill.__dict__))

    result = []
    for operation in operations:
        bill_data = bills_by_operation.get(operation.id, [])
        eco_sum = 0.0
        for bill in bill_data:
            if bill.eco_rating:
                eco_sum += bill.eco_rating

        operation_dict = operation.__dict__
        # del operation_dict['_sa_instance_state']
        operation_dict["bill_data"] = bill_data
        operation_dict['eco_rating_sum'] = eco_sum
        result.append(models.Operation(**operation_dict))
    return result
