from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str
    email: str
    password: list[Hash] = []

    class Config:
        orm_mode = True


class PassSchema(BaseModel):
    id: int
    user_id: int
    hash_password: str
    hash: str

    class Conifg:
        orm_mode = True
