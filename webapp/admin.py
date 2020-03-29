from django.contrib import admin
from . models import Item, TodoList

admin.site.register(Item)
admin.site.register(TodoList)