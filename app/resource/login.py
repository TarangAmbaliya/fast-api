"""
User Login operations.
"""

from fastapi import Body, Response, status

from app.resource import router
from app.models.user import User
from app.models import session
from app.auth.passOps import verify_hash
from app.auth.tokenOps import cook_access_token


@router.get('/login')
async def login(response: Response, email: str = Body('email'), password: str = Body('password')) -> dict or None:
    """
    User login implementation.

    Example:
        {
             "email": "example@email.com",
            "password": "ExamplePassword"
        }

    :param response: Used internally by the app to produce HTTP response codes.
    :param email: User email.
    :param password: User password.
    :return: Returns a response code 200 with a dict containing access token if user present in database.
        Returns None with response code 400 if no entry found in the database.
        Returns None with respose code 401 if password is incorrect.
    """
    db = session()
    query = db.query(User).filter(User.email == email).first()
    if query:
        response.status_code = status.HTTP_400_BAD_REQUEST
        if verify_hash(in_password=password, in_hash=query.password):
            response.status_code = status.HTTP_200_OK
            token = cook_access_token(query.name)
            return {'Access Token': token}
        else:
            response.status_code = status.HTTP_401_UNAUTHORIZED
            return
    else:
        return
