"""
Database Model for the Users.
"""

from sqlalchemy import Column, Integer, String

from app.models import Base


class User(Base):

    """
    Inherit Base class from SQLAlchemy to create a User class defining a Database Model.
    """

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    email = Column(String, nullable=True, unique=True, index=True)
    password = Column(String, nullable=False, index=True)
