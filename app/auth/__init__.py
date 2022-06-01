"""
Initiate security and hashing utilites.
"""

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


encrypt = CryptContext(schemes=['bcrypt'], deprecated='auto')
auth_me = OAuth2PasswordBearer(tokenUrl='login')
