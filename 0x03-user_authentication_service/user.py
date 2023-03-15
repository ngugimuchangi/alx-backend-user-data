#!/usr/bin/env python3
"""
Users model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """ Represents user object/table
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250))
    reset_token = Column(String(250))

    def __init__(self, email: str, hashed_password: str,
                 session_id: str = None, reset_token: str = None,
                 **kwargs: dict) -> None:
        """ Create new User instance
        """
        self.email = email
        self.hashed_password = hashed_password
        if session_id:
            self.session_id = session_id
        if reset_token:
            self.reset_token = reset_token

        if not kwargs:
            return
        for attr, val in kwargs.items():
            if hasattr(User, attr) and attr != 'id':
                setattr(self, attr, val)
