import sqlalchemy.orm
from sqlalchemy import Column, Integer, String, Date

from .. import model

class User(model.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    patronymic = Column(String)
    british_date = Column(Date)

