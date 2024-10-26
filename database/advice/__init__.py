from sqlalchemy import orm
from .. import model
import sqlalchemy

class Advice(model.Model):
    __tablename__ = "advice"

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True, index=True)
    name: orm.Mapped[str] = orm.mapped_column(sqlalchemy.String, index=True)
    description: orm.Mapped[str] = orm.mapped_column(sqlalchemy.String)



