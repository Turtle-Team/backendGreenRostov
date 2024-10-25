from fastapi import Depends
from .route import route
from . import utils


@route.get("/me")
def read_users_me(current_user: str = Depends(utils.get_current_user)):
    return {"username": current_user}
