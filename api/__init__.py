import fastapi
from .user.route import route as route_user
from .events.route import route as route_events

main_router = fastapi.APIRouter()
main_router.include_router(route_user)
main_router.include_router(route_events)
