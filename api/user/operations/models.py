import pydantic
from typing import List

class OperationResponse(pydantic.BaseModel):
    id: int
    retailPlace: str | None
    ecashTotalSum: float
    totalSum: float
    date_time: int | None
    user: str | None
