"""
Token Operations.
"""
from jose import jwt
from app.config import SECRET_KEY, ALGORITHM


def cook_access_token(identity: str) -> str:
    """
    This function is a wrapper for the jwt.encode entity.

    :param identity: String to be used in the token parameter 'sub'.
    :return: A JSON WEB TOKEN of access type.
    """
    claim = {'sub': identity}
    access_token = jwt.encode(claim, SECRET_KEY, ALGORITHM)
    return access_token


def check_token(in_token: str) -> bool:
    """
    This function is a wrapper for the jwt.decode entity.

    :param in_token: Token received in the request by user.
    :return: True if the token is authentic, else False.
    """
    decoded_in_token = jwt.decode(in_token, SECRET_KEY, ALGORITHM)

    if decoded_in_token.get('sub') is None:
        return False
    else:
        return True
