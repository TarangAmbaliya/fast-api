from sqlalchemy.orm import Session
from app.schemas import UserSchema, PassSchema


def create_user(db: Session, user: UserSchema):
    add_user = UserSchema(name=user.name, email=user.email, password=user.password)
    db.add(add_user)
    db.commit()
