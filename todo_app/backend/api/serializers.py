from rest_framework import serializers
from todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'title', 'description', 'completed', 'created']


class TodoToggleCompleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Todo
        fields = ['title', 'description', 'created', 'completed']
