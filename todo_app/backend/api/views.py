from rest_framework import generics
from .serializers import TodoSerializer
from rest_framework import generics, permissions
from todo.models import Todo


class TodoList(generics.ListCreateAPIView):
    # ListCreateAPIView is a generic view that provides GET (list all) and POST method handlers.
    # ListAPIView requires two mandatory attributes: serializer_class and queryset.
    serializer_class = TodoSerializer

    # permission_classes is a list of permission classes that the view requires for the request to be allowed.
    permission_classes = [permissions.IsAuthenticated]

    # queryset is a list of all the objects that the view will return.
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user).order_by('-created')

    # perform_create is a method that is called when a new object is created.
    def performe_create(self, serializer):
        # serializer holds a django model
        serializer.save(user=self.request.user)
