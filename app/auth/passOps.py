"""
Password Operations.
"""

from passlib.exc import UnknownHashError

from app.auth import encrypt


def generate_hash(password: str) -> str:
    """
    This function should be used whenever creating a hash throughout the app context.

    :param password:
        Password of the user.
    :return:
        A hashed version of the password.
    """
    return encrypt.hash(password)


def verify_hash(in_password: str, in_hash: str) -> bool:
    """
    This function should be used whenever verifing hash throughout the app context.

    :param in_password:
        The password entered by the user during login.
    :param in_hash:
        The hash stored in the database corresponding to that user.
    :return:
        True if hash matches, False if it dosen't.
    """
    try:
        return encrypt.verify(secret=in_password, hash=in_hash)
    except UnknownHashError:
        return False
