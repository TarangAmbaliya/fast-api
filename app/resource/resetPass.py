"""
This file enables the user to reset there password using a fresh type JWT.
"""

from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials

from app.resource import router
from app.schemas import UserResetPassSchema
from app.models import session
from app.models.user import User
from app.auth import auth_me
from app.auth.passOps import generate_hash, verify_hash
from app.auth.tokenOps import check_token


@router.post('/reset')
async def pwd_reset(data: UserResetPassSchema, token: HTTPAuthorizationCredentials = Security(auth_me)) -> None:
    """
    This Function implements the password reset feature.

    Example: exapmle {
        "email": "example@mail.com",
        "old_password": "ExampleOldPassword",
        "new_password": "ExampleNewPassword"
    }

    :param token: Authorization token recieved in the request.
    :param data: Data in format as show in the example.
    :return: None
    :raises HTTPException:
        Status code 401 if the token is invalid, expired.
        Status code 400 if no user found.
    """
    in_token = token.credentials
    check_token(in_token=in_token)
    db = session()
    query = db.query(User).filter(User.email == data.email).first()
    if query:
        if verify_hash(data.old_password, query.password):
            query.password = generate_hash(data.new_password)
        else:
            raise HTTPException(status_code=401, detail='Incorrect Old Password.')
        db.commit()
    else:
        raise HTTPException(status_code=400, detail='No user found.')
