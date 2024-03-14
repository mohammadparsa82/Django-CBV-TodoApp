from django.urls import path
from tasks.views import *


#app_name = 'tasks'

urlpatterns = [
    path("", TaskList.as_view(), name="task_list"),
    path("create/", CreatTask.as_view(), name="create_task"),
    path("update/<int:pk>/", UpdateTask.as_view(), name="update_task"),
    path("delete/<int:pk>/", DeleteTask.as_view(), name="delete_task"),
    path("complete/<int:pk>/", TaskComplete.as_view(), name="complete_task"),
]
