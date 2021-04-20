import json
from django.http import HttpResponse, HttpRequest
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout


@method_decorator(csrf_exempt, name='dispatch')
class Login(View):
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

        response = {
            'id': user.id,
            'username': user.username,
            'firstname': user.first_name,
            'email': user.email
        }
        
        login(request, user)
        return HttpResponse(json.dumps(response), content_type='application/json')


@method_decorator(csrf_exempt, name='dispatch')
class Logout(View):
    """
    Logs a user out.
    """
    def post(self, request, *args, **kwargs):
        logout(request)
        return HttpResponse('/login', content_type='application/json')