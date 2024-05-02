from rest_framework import generics
from .serializers import TodoSerializer, TodoToggleCompleteSerializer
from rest_framework import generics, permissions
from todo.models import Todo
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate


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


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # RetrieveUpdateDestroyAPIView is a generic view that provides GET (retrieve), PUT (update), and DELETE method handlers.
    # RetrieveUpdateDestroyAPIView requires two mandatory attributes: serializer_class and queryset.
    serializer_class = TodoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # user can only update, delete own posts
        return Todo.objects.filter(user=user)


class TodoToggleComplete(generics.UpdateAPIView):
    # UpdateAPIView is a generic view that provides PUT method handlers.
    # UpdateAPIView requires two mandatory attributes: serializer_class and queryset.
    serializer_class = TodoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)

    def perform_update(self, serializer):
        serializer.instance.completed = not (serializer.instance.completed)
        serializer.save()


@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)  # data is a dictionary
            user = User.objects.create_user(
                data['username'], password=data['password'])
            username = data['username']
            password = data['password']
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse({'error': 'That username has already been taken. Please choose a new username'}, status=400)


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request, username=data['username'], password=data['password'])
        if user is None:
            return JsonResponse({'error': 'Could not login. Please check username and password'}, status=400)
        else: # return user token if user is authenticated
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist: # if token not in db, create a new one
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
