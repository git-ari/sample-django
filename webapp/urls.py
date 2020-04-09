from django.urls import path, include
from rest_framework.routers import DefaultRouter
from webapp import views

router = DefaultRouter()
router.register(r'item', views.ItemViewSet)
router.register(r'todolist', views.TodoListViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api/hello', views.ApiEndpoint.as_view()),  # an example resource endpoint
]