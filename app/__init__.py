from fastapi import FastAPI
from app.resource import root


app = FastAPI()

app.include_router(root.router)
