#!/usr/bin/env python3
import bcrypt


def _hashed_password(password: str) -> bytes:
    """ Creates password hash
        Args:
            - password: user password
        Return:
            - hashed password
    """
    e_pwd = password.encode()
    return bcrypt.hashpw(e_pwd, bcrypt.gensalt())
