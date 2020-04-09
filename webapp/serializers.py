from rest_framework import serializers
from . models import TodoList, Item
from django.contrib.auth.models import User

class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
    
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')