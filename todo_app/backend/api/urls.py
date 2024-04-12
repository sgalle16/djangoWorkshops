from django.urls import path
from . import views


app = 'api'

urlpatterns = [
    path('todos/', views.TodoList.as_view(), name='todo_list'),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view(), name = 'todo_rud'),
    path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view(), name = 'todo_update'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]