from sqlalchemy import Column, Integer, String, Float
import sqlalchemy.orm
from sqlalchemy.orm import Mapped
from ..model import Model

class Operation(Model):
    __tablename__ = "operations"

    id: Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True, index=True)
    retailPlace: Mapped[str] = sqlalchemy.orm.mapped_column(String)
    ecashTotalSum: Mapped[float] = sqlalchemy.orm.mapped_column(Float)
    items: Mapped[str] = sqlalchemy.orm.mapped_column(String)
    totalSum: Mapped[float] = sqlalchemy.orm.mapped_column(Float)
    date_time: Mapped[int] = sqlalchemy.orm.mapped_column(Integer)
    user: Mapped[str] = sqlalchemy.orm.mapped_column(String)
