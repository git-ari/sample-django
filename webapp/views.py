from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf.urls import url
from webapp.models import TodoList, Item
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from webapp.serializers import TodoListSerializer, ItemSerializer
from oauth2_provider.views.generic import ProtectedResourceView
from django.http import HttpResponse
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import action


class TodoListViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents todo lists.
    """
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer
    
class ItemViewSet(viewsets.ModelViewSet):
    """
    This endpoint presents code items of todo lists.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class ApiEndpoint(ProtectedResourceView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, OAuth2!')