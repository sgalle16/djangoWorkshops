from rest_framework import generics
from .serializers import TodoSerializer

from todo.models import Todo


class TodoList(generics.ListCreateAPIView):
    # ListCreateAPIView is a generic view that provides GET (list all) and POST method handlers.
    # ListAPIView requires two mandatory attributes: serializer_class and queryset.
    serializer_class = TodoSerializer

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')
    
    def performe_create(self, serializer):
        # serializer holds a django model 
        serializer.save(user=self.request.user)