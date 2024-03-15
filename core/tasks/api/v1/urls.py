from django.urls import path
from .views import *


app_name = 'api-v1'

urlpatterns = [
    path('task/',TaskList.as_view(), name='task-list'),
    path('task/<id>/',TaskDetail.as_view(), name='task-detail'),
]
