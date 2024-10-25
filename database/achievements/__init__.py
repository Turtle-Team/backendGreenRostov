from sqlalchemy import Column, Integer, String
import sqlalchemy.orm
from sqlalchemy.orm import Mapped
from .. import model
from .. import user


class Achievements(model.Model):
    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    experience = Column(Integer)
    level = Column(Integer)
    picture = Column(String)



class UserAchievements(model.Model):
    __tablename__ = "user_achievements"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = sqlalchemy.orm.mapped_column(sqlalchemy.ForeignKey("users.id"))
    achievement_id: Mapped[int] = sqlalchemy.orm.mapped_column(sqlalchemy.ForeignKey("achievements.id"))
    reason: Mapped[str] = Column(String)

