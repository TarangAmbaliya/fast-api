"""
Validation Schemas for pydantic
"""

from pydantic import BaseModel


class UserSchema(BaseModel):
    """
    Inherit BaseModel from pydantic, create a Schema class for User data validation when making entry in the database.
    """
    name: str
    email: str
    password: str

    class Config:
        """
        Nested class to define that we are using ORM (sqlalchemy) for database operations.
        """
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "ExampleName",
                "email": "example@mail.com",
                "password": "ExamplePassword"
            }
        }


class UserLoginSchema(BaseModel):
    """
    Inherit BaseModel from pyantic, create a Schema class for User login data validation.
    """

    email: str
    password: str

    class Config:
        """
        Nested class to define that we are using ORM (sqlalchemy) for database operations.
        """
        orm_mode = True
        schema_extra = {
            "example": {
                "email": "example@mail.com",
                "password": "ExamplePassword"
            }
        }