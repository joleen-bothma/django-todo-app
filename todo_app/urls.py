from django.urls import path
from .views import ToDoListView, ToDoItemView, ToDoItemDetailView, ToDoItemCreate

urlpatterns = [
    path("", ToDoListView.as_view(), name="lists"),
    path("list/<int:list_id>/", ToDoItemView.as_view(), name="list"),
    path("task/<int:pk>/", ToDoItemDetailView.as_view(), name="task"),
    path("task-create/", ToDoItemCreate.as_view(), name="task-create"),
]