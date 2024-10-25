import fastapi
from .router import route
from .. import utils

@route.get("/")
def get_achievements(current_user: str = fastapi.Depends(utils.get_current_user)):

    return {"username": ''}
