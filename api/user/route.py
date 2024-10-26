import fastapi

from .auth.router import route as route_auth
from .achievements.router import route as route_achievements
from .patrol.router import route as route_patrol
from .operations.route import route as route_operations

route = fastapi.APIRouter(prefix='/user', tags=['Пользователь'])

route.include_router(route_auth)
route.include_router(route_achievements)
route.include_router(route_patrol)
route.include_router(route_operations)
