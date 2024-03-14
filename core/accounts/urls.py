from django.urls import path
from accounts.views import *



app_name = 'accounts'

urlpatterns = [
    path('login', Login.as_view() , name='Login'),
    path("register/", RegisterPage.as_view(), name="register"),
    path('logout',logout_views,name='logout'),
]