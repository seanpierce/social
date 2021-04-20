from django.urls import path
from .authenticate import Login, Logout

urlpatterns = [
    path('authenticate/login', Login.as_view()),
    path('authenticate/logout', Logout.as_view())
]