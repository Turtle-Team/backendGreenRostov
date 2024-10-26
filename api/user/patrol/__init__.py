import json

import fastapi

import database
from .router import route
from .. import utils
from database.patrol import Patrol

from database.achievements.headler import Db
from database.achievements import UserAchievements
from ..achievements.models import PatrolAchievements

@route.get("/me")
def get_achievements(user: dict = fastapi.Depends(utils.get_current_user)):
    session = database.Database().get_marker()
    patrols_user: list[database.patrol.Patrol] = session.query(Patrol).filter(
        Patrol.user_id == user['id'] and Patrol.answers == ''
    ).all()
    patrols_user[0].__repr__()
    return list(map(lambda x: x.__dict__, patrols_user))


@route.post("/{id_patrol}")
def answer(answers: str, id_patrol: int, user: dict = fastapi.Depends(utils.get_current_user)):
    session = database.Database().get_marker()
    patrols_mission = session.query(Patrol).filter_by(id=id_patrol)
    patrols_mission.update({'answers': answers})

    session.commit()
    patrols_user: list[database.patrol.Patrol] = session.query(Patrol).filter(
        Patrol.user_id == user['id'] and Patrol.answers == ''
    ).all()
    patrols_user[0].__repr__()
    all_user_mission = session.query(Patrol).filter(Patrol.user_id == user['id']).filter(Patrol.answers != '').all()
    all_user_mission = len(all_user_mission)
    table_mission_achievements = {3: PatrolAchievements.BRODYAGA,
                                  5: PatrolAchievements.DRUZHINIK,
                                  8: PatrolAchievements.PATROL_MAN}

    if table_mission_achievements.get(all_user_mission):
        achievement_id: int = table_mission_achievements.get(all_user_mission).value
        if Db().is_have(user['id'], achievement_id):
            return patrols_mission.first()
        data_achievements = UserAchievements()
        data_achievements.user_id = user['id']
        data_achievements.achievement_id = achievement_id
        data_achievements.reason = 'Выполнения условий'
        Db().insert_new_ready(data_achievements)

    return patrols_mission.first()
