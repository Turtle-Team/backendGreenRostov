import pydantic
from typing import List

class OperationResponse(pydantic.BaseModel):
    id: int
    retailPlace: str
    ecashTotalSum: float
    items: str
    totalSum: float
    date_time: int
    user: str
