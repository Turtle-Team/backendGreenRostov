import json

import fastapi

import database
from .router import route
from .. import utils
from database.patrol import Patrol

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
    return patrols_mission.first()
