from sqlalchemy.exc import IntegrityError

from app.models import session
from app.models.user import User
from app.schemas import UserSchema
from app.resource import router
from app.auth.passOps import generate_hash


@router.post('/register')
def create_user(user: UserSchema):
    query = User(name=user.name, email=user.email, password=generate_hash(user.password))
    db = session()
    db.add(query)
    try:
        db.commit()
    except IntegrityError:
        return {'error': 'Name or Email already exist.'}
    db.refresh(query)
    db.close()
    return query
