from fastapi import Body
from fastapi.security import OAuth2PasswordBearer

from app.resource import router
from app.models.user import User
from app.models import session
from app.auth.passOps import verify_hash


@router.get('/login')
def login(email: str = Body('email'), password: str = Body('password')):
    db = session()
    query = db.query(User).filter(User.email == email).first()
    if query:
        if verify_hash(in_password=password, in_hash=query.password):
            return {'msg': 'You are now Logged in.'}
        else:
            return {'error': 'Incorrect Password.'}
    else:
        return {'error': 'No  user Found.'}
