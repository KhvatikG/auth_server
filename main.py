from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hi_there():
    return {"message": "Hi There!"}
