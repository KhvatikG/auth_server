from fastapi import FastAPI

from users.views import router as users_router

app = FastAPI()
app.include_router(users_router)

@app.get('/')
async def hi_there():
    return {"message": "Hi There!"}
