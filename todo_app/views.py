from django.shortcuts import render
from django.views.generic import ListView
from .models import ToDoList, ToDoItem

class ToDoListView(ListView):
    models = ToDoList
    template_name = "todo_app/lists.html"

class ToDoItemView(ListView):
    models = ToDoItem
    template_name = "todo_app/tasks.html"