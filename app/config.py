import os


SECRET_KEY = os.environ.get('SECRET_KEY', '909f40337eb9dad2b9ff04b854498f66d8ce81bbb246e8425d59218db9d9d7b0')
ALGORITHM = os.environ.get('ALGORITHM', 'HS256')

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'postgresql://postgres:postgres@localhost:5432/usr')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS', False)
