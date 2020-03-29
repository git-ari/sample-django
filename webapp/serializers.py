from rest_framework import serializers
from . models import TodoList, Item


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
