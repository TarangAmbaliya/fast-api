"""
Database Model for the Users.
"""

from sqlalchemy import Column, Integer, String, Boolean

from app.models import Base
from app.auth.passOps import generate_hash


class User(Base):

    """
    Inherit Base class from SQLAlchemy to create a User class defining a Database Model.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String, nullable=False, index=True)
    is_active = Column(Boolean, index=True)
    is_verified = Column(Boolean, index=True)

    def __init__(self, name, email, password, is_active=True, is_verified=False):
        self.name = name
        self.email = email
        self.password = generate_hash(password)
        self.is_active = is_active
        self.is_verified = is_verified
