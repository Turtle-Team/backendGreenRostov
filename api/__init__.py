import fastapi
from .user.route import route as route_user
from .events.route import route as route_events
from .expert.route import route as router_expert
from .advice.route import route as route_advice
from .operations import route as route_operations

main_router = fastapi.APIRouter()
main_router.include_router(route_user)
main_router.include_router(route_events)
main_router.include_router(router_expert)
main_router.include_router(route_advice)
main_router.include_router(route_operations)
