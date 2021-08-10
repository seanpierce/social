import json
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from . import APIView
from repositories.users import UsersRepository



class Login(APIView):
    """
    Logs a user in.
    """
    def post(self, request, *args, **kwargs):
        payload = self.GetPayload(request, ['username', 'password'])
        user = authenticate(username=payload['username'], password=payload['password'])

        if user is None:
            return self.Response(False, 401)

        login(request, user)

        response = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        
        return self.Response(response)


class Logout(APIView):
    """
    Logs a user out.
    """
    def post(self, request, *args, **kwargs):
        logout(request)
        return self.Response(True)


class CheckSession(APIView):
    """
    Checks to see if a session is still valid. If so, returns user data.
    """
    def post(self, request, *args, **kwargs):
        session_key = request.session.session_key

        try:
            user = UsersRepository.get_user_from_session_key(session_key)

            response = {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
            
            return self.Response(response)
        except Exception as e:
            return self.Response(False, 401)