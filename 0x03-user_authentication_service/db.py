#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound, InvalidRequestError
# from sqlalchemy.exc import NoResultFound, InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Creates new User instance and
            saves them to the database.
            Args:
                - email
                - hashed_password
            Return:
                - new User object
        """
        session = self._session
        new_user = User(email, hashed_password)
        session.add(new_user)
        session.commit()
        return new_user

    def find_user_by(self, **kwargs: dict):
        """ Find user by a given attribute
        """
        attr, val = tuple(kwargs.items())[0]
        if not hasattr(User, attr):
            raise InvalidRequestError

        session = self.__session
        user = session.execute(
            text(f"SELECT * FROM users WHERE {attr}=:param"),
            {"param": val}).first()
        if not user:
            raise NoResultFound
        return user
