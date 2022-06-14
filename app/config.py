"""
Config file to manage Environment variables and configs.
"""

import os

SECRET_KEY = os.environ.get(
    'SECRET_KEY',
    '505697a4a7f652ba62cbee4d4a84e01cd30c6e366b55f784a44240082d83b372'
)
ALGORITHM = os.environ.get(
    'ALGORITHM',
    'HS256'
)

SQLALCHEMY_DATABASE_URI = os.environ.get(
    'DATABASE_URI',
    'postgresql://postgres:postgres@localhost:5432/usr'
)
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get(
    'SQLALCHEMY_TRACK_MODIFICATIONS',
    False
)
