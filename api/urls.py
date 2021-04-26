from django.contrib.auth.decorators import login_required
from django.urls import path
from .authenticate import Login, Logout, CheckSession
from .posts import Create

urlpatterns = [
    path('authenticate/login', Login.as_view()),
    path('authenticate/logout', Logout.as_view()),
    path('authenticate/checksession', CheckSession.as_view()),
    path('posts/create', login_required(Create.as_view()))
]