from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    password = relationship('Hash', back_polpulates='hash')
