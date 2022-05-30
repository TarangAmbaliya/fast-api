from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.models import Base


class Hash(Base):
    __tableaname__ = 'hashes'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    hash_password = Column(String, nullable=False)
    hash = relationship('User', back_populates='password')
