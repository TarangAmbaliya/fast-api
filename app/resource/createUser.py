"""
Register new users and add them to the database.
"""

from sqlalchemy.exc import IntegrityError
from fastapi import Response, status

from app.models import session
from app.models.user import User
from app.schemas import UserSchema
from app.resource import router
from app.auth.passOps import generate_hash


@router.post('/register')
async def create_user(response: Response, user: UserSchema) -> dict or None:
    """
    Get Request Data and create a user with that data.

    Example:
        {
            "name": "ExampleName",
            "email": "example@email.com",
            "password": "ExamplePassword"
        }

    :param response: Used internally by the app to produce HTTP response codes.
    :param user: User data in format as shown in the example.
    :return: Response code 200 upon successfull data validation.
        Returns None with response code 400 if user already exists.
        Returns a response code 400 and a dict with missing parameters iscase of partial input.
    """
    query = User(name=user.name, email=user.email, password=generate_hash(user.password))
    db = session()
    db.add(query)
    try:
        db.commit()
    except IntegrityError:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return
    db.close()
    response.status_code = status.HTTP_200_OK
    return
