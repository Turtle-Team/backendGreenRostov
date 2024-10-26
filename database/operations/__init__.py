from sqlalchemy import Integer, String, Float
from sqlalchemy.orm import Mapped
from ..model import Model
from sqlalchemy import orm
import sqlalchemy

class Operation(Model):
    __tablename__ = "operations"

    id: Mapped[int] = orm.mapped_column(primary_key=True, index=True)
    retail_place: Mapped[str] = orm.mapped_column(String)
    ecash_sum: Mapped[float] = orm.mapped_column(Float)
    totalSum: Mapped[float] = orm.mapped_column(Float)
    date_time: Mapped[int] = orm.mapped_column(Integer)
    dep_name: Mapped[str] = orm.mapped_column(String)
    user_id: Mapped[int] = orm.mapped_column(sqlalchemy.ForeignKey('users.id'))



class OperationBillData(Model):
    __tablename__ = "operation_bill_data"

    id: Mapped[int] = sqlalchemy.orm.mapped_column(primary_key=True, index=True)
    operation_id = orm.mapped_column(sqlalchemy.ForeignKey('operations.id'))
    nomenclature: Mapped[str]
    sum: Mapped[float]
    eco_rating: Mapped[float]  = orm.mapped_column(sqlalchemy.ForeignKey('operations.id'), nullable=True, default=None)

