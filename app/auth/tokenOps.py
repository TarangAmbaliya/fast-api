"""
Token Operations.
"""

from fastapi import HTTPException
from datetime import timedelta, datetime
from jose import jwt

from app.config import SECRET_KEY, ALGORITHM


def cook_token(identity: str,
               expire_at: datetime = datetime.utcnow() + timedelta(hours=10),
               refresh: bool = False) -> str:
    """
    This function is a wrapper for the jwt.encode entity.

    :param identity:
        String to be used in the token parameter 'sub'.
    :param expire_at:
        Amount of time after which the token will expire.
    :param refresh:
        True if the token type is to be refresh.
    :return:
        A dict of JSON WEB TOKEN of access type and a refresh type.
    """
    if refresh:
        scope = 'refresh_token'
        expire_at = datetime.utcnow() + timedelta(days=10)
    else:
        scope = 'access_token'
    claim = {
        'exp': expire_at,
        'sub': identity,
        'scope': scope
    }
    token = jwt.encode(claim, SECRET_KEY, ALGORITHM)
    return token


def check_token(in_token: str) -> dict:
    """
    This function is a wrapper for the jwt.decode entity.

    :param in_token:
        Token received in the request by user.
    :return:
        Token claims.
    :raises HTTPException:
        Status code 401 if Token expired.
        Status code 400 if Token invalid, or type mismatch.
    """
    try:
        claim = jwt.decode(in_token, SECRET_KEY, ALGORITHM)
        return claim
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token expired.')
    except jwt.JWTError:
        raise HTTPException(400, detail='Invalid token.')
