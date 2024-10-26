import fastapi
from .router import route
from .. import utils
from database.achievements import headler

@route.get("/")
def get_achievements(user: str = fastapi.Depends(utils.get_current_user)):
    all_achievements = headler.Db().get_all_by_user(user['id'])
    return all_achievements
