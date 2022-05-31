from fastapi.security import OAuth2PasswordBearer

from app.auth import encrypt


def generate_hash(password: str):
    return encrypt.hash(password)


def verify_hash(in_password: str, in_hash: str):
    return encrypt.verify(secret=in_password, hash=in_hash)
