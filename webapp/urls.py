from django.urls import path
from rest_framework.routers import DefaultRouter
from webapp import views

router = DefaultRouter()
router.register(r'item', views.ItemViewSet)
router.register(r'todolist', views.TodoListViewSet)