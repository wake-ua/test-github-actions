#!/usr/bin/python

from src.routers import function
from fastapi import FastAPI

app = FastAPI()


app.include_router(function.router)


@app.get("/")
def read_root():
    return {"message": "Hello World"}
