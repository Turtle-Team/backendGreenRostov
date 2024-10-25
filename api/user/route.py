import fastapi
from .auth import route as route_auth
from .achievements import route as route_achievements

route = fastapi.APIRouter(prefix='/user', tags=['Пользователь'])

route.include_router(route_auth)
route.include_router(route_achievements)
