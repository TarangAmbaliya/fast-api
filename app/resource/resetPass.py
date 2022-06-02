"""
This file enables the user to reset there password using a fresh type JWT.
"""

from fastapi import HTTPException
from jose import jwt

from app.resource import router
from app.schemas import UserLoginSchema
from app.models import session
from app.models.user import User


@router.post('/reset')
def pwd_reset(data: UserLoginSchema) -> None:
    """
    This Function implements the password reset feature.

    Example: exapmle {
        "email": "example@mail.com"
        "password": "ExamplePassword"
    }

    :param data: Data in format as show in the example.
    :return: None
    :raises HTTPException:
        Status code 401 if token invalid, expired or not fresh.
        Status code 400 if no user found.
    """
    db = session()
    query = db.query(User).filter(User.email == data.email).first()
    if query:
        query.password = data.password
        db.commit()
    else:
        raise HTTPException(status_code=400, detail='No user found.')
