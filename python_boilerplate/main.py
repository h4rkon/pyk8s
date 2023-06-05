from fastapi import FastAPI
from .routers import hello_world
from .auth import auth

app = FastAPI()
app.include_router(auth)
app.include_router(hello_world.router)
