import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter

# Создаем экземпляр APIRouter
router = APIRouter(prefix="/api")

# Определяем маршруты
@router.get("/items/")
async def read_items():
    return [{"name": "Foo"}, {"name": "Bar"}]

@router.get("/tovars")
async def read_users():
    return [{"username": "johndoe"}, {"username": "alice"}]

# Добавляем маршруты в приложение


app = FastAPI()
user_router = APIRouter(prefix='/test')
user_router.include_router(router)
app.include_router(user_router)

uvicorn.run(app, host="127.0.0.1", port=5001)

