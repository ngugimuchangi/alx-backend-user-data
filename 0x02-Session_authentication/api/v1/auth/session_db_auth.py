#!/usr/bin/env python3
"""
Session storage module
"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from datetime import datetime, timedelta
from models.user_session import UserSession
from models.user import User
from typing import TypeVar
from os import getenv


class SessionDBAuth(SessionExpAuth):
    """ Session class for storable and persistent
        sessions
    """
    def create_session(self, user_id: str = None) -> str:
        """ Creates session object
            Return:
                - id of session object
        """
        if user_id and type(user_id) is str:
            session = UserSession(**{"user_id": user_id})
            session.save()
            return session.id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Get user by session id
        """
        if not session_id or type(session_id) is not str:
            return None
        try:
            session = UserSession.get(session_id)
        except KeyError:
            return None
        if not session:
            return None

        # Session with infinity lifespan
        if self.session_duration <= 0:
            return session.user_id

        # Check for expired session
        expiry_date = session.updated_at \
            + timedelta(seconds=self.session_duration)
        if datetime.utcnow() < expiry_date:
            return session.user_id
        session.remove()
        return None
        

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get current user
            Return:
                - User object for user instance whose user id is
                  linked to given session id
        """
        if not request:
            return None
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        try:
            return User.get(user_id)
        except KeyError:
            return None

    def destroy_session(self, request=None) -> bool:
        """ Destroy session object based on session id
        """
        if not request:
            return False
        session_id = self.session_cookie(request)
        try:
            session = UserSession.get(session_id)
        except KeyError:
            return False
        else:
            if session:
                session.remove()
                return True
        return False
