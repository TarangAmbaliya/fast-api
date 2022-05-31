from fastapi import FastAPI

from app.resource import createUser
from app.resource import login
from app.models import Base, engine
from app.config import SECRET_KEY, ALGORITHM


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(createUser.router)
app.include_router(login.router)
