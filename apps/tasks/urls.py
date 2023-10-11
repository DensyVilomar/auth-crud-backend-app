from .views import *
from django.urls import path


urlpatterns = [
    path('', TaskListApiView.as_view()),
    path('<int:id>/', TaskDetailApiView.as_view()),
]
