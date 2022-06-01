"""
Validation Schemas for pydantic
"""

from pydantic import BaseModel


class UserSchema(BaseModel):
    """
    Inherit BaseModel from pydantic and create a Schema class for User data validation.
    """
    name: str
    email: str
    password: str

    class Config:
        """
        Nested class to define that we are using ORM (sqlalchemy) for database operations.
        """
        orm_mode = True
