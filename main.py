from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

import main
from core.models import Base, db_helper
from users.views import router as users_router
from api_v1.demo_auth.demo_jwt_auth import router as demo_jwt_auth_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(users_router)
app.include_router(demo_jwt_auth_router)


@app.get('/')
async def hi_there():
    return {"message": "Hi There!"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
