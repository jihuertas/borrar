from django.urls import path
from . import views
from .views import TaskList

urlpatterns = [
    path('tasks/', TaskList.as_view(), name='task_list'),
]