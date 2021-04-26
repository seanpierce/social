from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


class UsersRepository():

    @staticmethod
    def get_user_from_session_key(session_key):
        session = Session.objects.get(session_key=session_key)
        uid = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(pk=uid)
        return user