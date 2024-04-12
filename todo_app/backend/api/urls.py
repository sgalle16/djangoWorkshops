from django.urls import path
from . import views


app = 'api'

urlpatterns = [
    path('todos/', views.TodoList.as_view(), name='list'),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view()),
]