from sqlalchemy import Column, Integer, String, Float
import sqlalchemy.orm
from sqlalchemy.orm import Mapped
from .. import model


class Patrol(model.Model):
    __tablename__ = "patrol"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id: Mapped[int] = sqlalchemy.orm.mapped_column(sqlalchemy.ForeignKey("users.id"))
    headers = Column(String)
    x_pos = Column(Float)
    y_pos = Column(Float)
    radius = Column(Integer)
    answers = Column(String, default='')
