import fastapi
from .user import route

main_router = fastapi.APIRouter()
main_router.include_router(route)