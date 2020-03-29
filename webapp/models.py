from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.name


class Item(models.Model):
    todoListId = models.ForeignKey(TodoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=100)
    checked = models.BooleanField()
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text
