import database
from . import Achievements, UserAchievements
from .models import AllAchievements
from . import models
from sqlalchemy import func
from database.user import User

class Db(database.Database):
    def insert_new_ready(self, data: UserAchievements):
        marker = self.get_marker()
        marker.add(data)
        marker.commit()

    def is_have(self, user_id: int, achievements_id: int):
        achv = self.get_marker().query(UserAchievements).filter(
            UserAchievements.user_id == user_id
        ).filter(UserAchievements.achievement_id == achievements_id).first()
        if achv is not None:
            return True
        return False

    def get_all_achievements(self):
        return self.get_marker().query(Achievements).all()

    def get_leaders(self):
        leaders =(self.get_marker().query(
            UserAchievements.user_id,
            func.sum(Achievements.experience).label("total_experience"),
        ).join(Achievements, UserAchievements.achievement_id == Achievements.id)
                  .group_by(UserAchievements.user_id)
                  .order_by(func.sum(Achievements.experience).desc()).limit(5)
                  .all())
        user_ids = list(map(lambda x: x[0], leaders))
        users = self.get_marker().query(User).filter(User.id.in_(user_ids)).all()
        result = []
        for i in leaders:
            r = list(filter(lambda x: x.id == i[0], users))
            result.append(models.Leaders(name=r[-1].username, exp=i[1]))

        return result

    def get_all_by_user(self, user_id):
        all_achievements: list[Achievements] = self.get_all_achievements()
        user_achievements: list[UserAchievements] = self.get_marker().query(UserAchievements).filter(
            UserAchievements.user_id == user_id).all()

        data = []
        for ach in all_achievements:
            data_ach = AllAchievements(achievements_id=ach.id,
                                       header=ach.name,
                                       text=ach.description,
                                       exp=ach.experience,
                                       image=ach.picture,
                                       user_id=user_id)
            data.append(data_ach)

        for ach in data:
            for user_ach in user_achievements:
                if user_ach.achievement_id == ach.achievements_id:
                    ach.complete = True

        return data
