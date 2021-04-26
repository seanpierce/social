from django.http import HttpResponse, HttpRequest
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from . import CSRFExemptView
import json
from repositories.users_repository import UsersRepository



class Login(CSRFExemptView):
    """
    Logs a user in.
    """
    def post(self, request, *args, **kwargs):
        body = json.loads(request.body.decode('utf-8'))
        username = body['username']
        password = body['password']
        user = authenticate(username=username, password=password)

        if user is None:
            return HttpResponse(False, status=401, content_type='application/json')

        login(request, user)

        response = {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
        
        return HttpResponse(json.dumps(response), content_type='application/json')


class Logout(CSRFExemptView):
    """
    Logs a user out.
    """
    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponse(True, content_type='application/json')


class CheckSession(CSRFExemptView):
    """
    Chacks to see if a session is still valid. If so, returns user data.
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
            
            return HttpResponse(json.dumps(response), content_type='application/json')
        except Exception as e:
            return HttpResponse(False, status=401, content_type='application/json')