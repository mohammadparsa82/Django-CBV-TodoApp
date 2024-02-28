from django.urls import path
from accounts.views import *
from django.contrib.auth.views import LogoutView
path("logout", LogoutView.as_view(next_page="/"), name="logout"),

app_name = 'accounts'

urlpatterns = [
    path('login', Login.as_view() , name='Login'),
    path("register/", RegisterPage.as_view(), name="register"),
    path("logout", LogoutView.as_view(next_page="/"), name="logout"),
]