#!/usr/bin/python
import os

import uvicorn
from src.routers import function
from fastapi import FastAPI
from contextlib import asynccontextmanager
from dotenv import load_dotenv


# Check if the file exists
if os.path.exists('.env'):
    print("Loading .env file")
    load_dotenv('.env')
else:
    print("No .env file defined")

HOST: str = os.getenv('HOST')
PORT: int = None
if os.getenv('PORT'):
    PORT = int(os.getenv('PORT'))


@asynccontextmanager
async def lifespan(fastapi_app: FastAPI):
    # this code runs before the app starts
    print("* Lifespan: App started", fastapi_app)
    print("\t - HOST =", HOST)
    print("\t - PORT =", PORT)
    yield
    # this code runs after the app finishes
    print("* Lifespan: App stopped")


app = FastAPI(lifespan=lifespan)
app.include_router(function.router)


@app.get("/")
def root():
    return {"message": "Hello, World!"}


if __name__ == "__main__":
    print("\t - HOST =", HOST)
    print("\t - PORT =", PORT)
    uvicorn.run(app, host=HOST, port=PORT)
