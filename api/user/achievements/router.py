import fastapi
from .. import route as router_user

route = fastapi.APIRouter(prefix='/achivments', tags=['Достижения пользователей'])
