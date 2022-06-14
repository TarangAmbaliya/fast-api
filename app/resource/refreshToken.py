"""
This file implements the refresh token feature.
"""

from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials

from app.auth import auth_me
from app.auth.tokenOps import check_token, cook_token
from app.resource import router


@router.get('/token/refresh')
async def refresh_token(
        token: HTTPAuthorizationCredentials = Security(auth_me)
):
    """
    Cook a access token from the refresh token.

    :param token: A JSON web token of refresh type.
    :return: A Refreshed token of access type.
    """

    claims = check_token(in_token=token.credentials)

    if claims['scope'] == 'refresh_token':
        return {'Access Token': cook_token(identity=claims['sub'])}
    else:
        raise HTTPException(status_code=400, detail='Invalid Token.')
