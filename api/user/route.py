import fastapi

from .auth.router import route as route_auth
from .achievements.router import route as route_achievements
from .patrol.router import route as route_patrol

route = fastapi.APIRouter(prefix='/user', tags=['Пользователь'])

route.include_router(route_auth)
route.include_router(route_achievements)
route.include_router(route_patrol)
