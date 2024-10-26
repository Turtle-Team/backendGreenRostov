from fastapi import Depends
from .auth import utils

def get_current_user(token: str = Depends(utils.oauth2_scheme)):
    data = utils.verify_token(token)
    return data
