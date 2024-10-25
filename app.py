

import fastapi
import api.user

app = fastapi.FastAPI()
app.include_router(api.main_router)