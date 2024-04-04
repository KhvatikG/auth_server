from fastapi import FastAPI

from users.views import router as users_router
from api_v1.demo_auth.demo_jwt_auth import router as demo_jwt_auth_router

app = FastAPI()
app.include_router(users_router)
app.include_router(demo_jwt_auth_router)


@app.get('/')
async def hi_there():
    return {"message": "Hi There!"}
