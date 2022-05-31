from passlib.context import CryptContext


encrypt = CryptContext(schemes=['bcrypt'], deprecated='auto')
