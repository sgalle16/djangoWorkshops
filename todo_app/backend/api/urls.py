from django.urls import path
from . import views


app = 'api'

urlpatterns = [
    path('todos/', views.TodoList.as_view(), name='list'),
]