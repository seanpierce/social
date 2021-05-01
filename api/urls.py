from django.contrib.auth.decorators import login_required
from django.urls import path
from .authenticate import Login, Logout, CheckSession
from .posts import Create, GetFeed
from .profiles import GetUserProfile

urlpatterns = [
    path('authenticate/login', Login.as_view()),
    path('authenticate/logout', Logout.as_view()),
    path('authenticate/checksession', CheckSession.as_view()),
    path('posts/create', login_required(Create.as_view())),
    path('posts', login_required(GetFeed.as_view())),
    path('profile/<username>', GetUserProfile.as_view())
]