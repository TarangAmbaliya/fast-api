"""
Register new users and add them to the database.
"""
from pydantic import EmailStr
from pydantic.error_wrappers import ValidationError
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from app.models import session
from app.models.user import User
from app.schemas import UserSchema
from app.resource import router
from app.tasks.email import welcome_email


@router.post('/register')
async def create_user(data: UserSchema) -> dict | None:
    """
    Get Request Data and create a user with that data.

    Example:
        {
            "name": "ExampleName",
            "email": "example@email.com",
            "password": "ExamplePassword"
        }
.
    :param data:
        User data in format as shown in the example.
    :return:
        Dict with missing parameters iscase of partial input.
    :raises HTTPException:
        Status code 400 if user already exists.
        Status code 200 if successfully registered.
    """
    query = User(name=data.name, email=data.email, password=data.password)
    db = session()
    db.add(query)
    try:
        db.commit()
    except IntegrityError:
        raise HTTPException(status_code=400, detail='User already exists.')
    db.close()
    try:
        await welcome_email(to=EmailStr(str(data.email)), username=data.name)
    except ValidationError:
        raise HTTPException(status_code=400, detail='Invalid Email.')
    return
