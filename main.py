#!/usr/bin/python
import os

import uvicorn
from src.routers import function
from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv

load_dotenv('.env')

HOST: str = os.getenv('HOST')
PORT: int = int(os.getenv('PORT'))


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    # this code runs before the app starts
    print("* Lifespan: App started", fastapi_app)
    yield
    # this code runs after the app finishes
    print("* Lifespan: App stopped")


app = FastAPI(lifespan=lifespan)
app.include_router(function.router)


@app.get("/")
def root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    uvicorn.run(app, host=HOST, port=PORT)
