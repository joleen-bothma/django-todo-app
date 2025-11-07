from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import ToDoList, ToDoItem

class ToDoListView(ListView):
    model = ToDoList
    template_name = "todo_app/lists.html"
    context_object_name = "lists"

class ToDoItemView(ListView):
    model = ToDoItem
    template_name = "todo_app/tasks.html"
    context_object_name = "tasks"

class ToDoItemDetailView(DetailView):
    model = ToDoItem
    template_name = "todo_app/task_detail.html"
    context_object_name = "task"

class ToDoItemCreate(CreateView):
    model = ToDoItem
    template_name = "todo_app/task_form.html"
    context_object_name = "task-create"
    fields = "__all__"
    # URL redirect when task is created (lazy coz it's only called when needed)
    success_url = reverse_lazy("list")