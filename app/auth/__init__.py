"""
Initiate security and hashing utilites.
"""

from fastapi.security import HTTPBearer
from passlib.context import CryptContext

encrypt = CryptContext(schemes=['bcrypt'], deprecated='auto')
auth_me = HTTPBearer()
