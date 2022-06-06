"""
Factory file for the app. App execution starts from this file.
"""

from fastapi import FastAPI

from app.resource import createUser
from app.resource import login
from app.resource import resetPass
from app.resource import refreshToken
from app.models import Base, engine
from app.config import SECRET_KEY, ALGORITHM


app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(createUser.router)
app.include_router(login.router)
app.include_router(resetPass.router)
app.include_router(refreshToken.router)
