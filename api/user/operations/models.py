import typing

from pydantic import BaseModel
from typing import Optional

class OperationBillData(BaseModel):
    id: int
    operation_id: int
    nomenclature: str
    sum: float
    eco_rating: Optional[float] = None

class Operation(BaseModel):
    id: int
    retail_place: str
    ecash_sum: float
    total_sum: float
    date_time: int
    dep_name: str
    user_id: int
    request_number: int
    bill_data: typing.List[OperationBillData]
    eco_rating_sum: float = 0



