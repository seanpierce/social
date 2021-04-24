from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/', redirect_field_name=None)
def index(request):
    return render(request, 'app.html', {
        'title': 'Test'
    })

def login(request):
    return render(request, 'login.html', {
        'title': 'Login'
    })