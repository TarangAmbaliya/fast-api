"""
User Login operations.
"""

from fastapi import HTTPException

from app.auth.passOps import verify_hash
from app.auth.tokenOps import cook_token
from app.models import session
from app.models.user import User
from app.resource import router
from app.schemas import UserLoginSchema


@router.get('/login')
async def login(data: UserLoginSchema) -> dict:
    """
    User login implementation.

    Example:
        {
             "email": "example@email.com",
            "password": "ExamplePassword"
        }

    :param data:
        Login credentials in format as shown in the example.
    :return:
        A dict containing access token & a refresh token.

    :raises HTTPException:
        Status code 401 incase of invalid credentials.
        Status code 400 if no user found.
    """
    db = session()
    query = db.query(User).filter(User.email == data.email).first()
    if query:
        if verify_hash(in_password=data.password, in_hash=query.password):
            return {
                'Access Token': cook_token(identity=query.name),
                'Refresh Token': cook_token(identity=query.name, refresh=True)
            }
        else:
            raise HTTPException(status_code=401, detail='Invalid Credentials.')
    else:
        raise HTTPException(status_code=400, detail='No User found.')
