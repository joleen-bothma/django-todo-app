from django.db import models

# Get the user model to access user info
from django.contrib.auth.models import User

# Timezone utils
from django.utils import timezone

# Reverse helps us avoid hard-coding URLs
from django.urls import reverse

# Pre-set function to calculate one week from today
def one_week_from_today():
    return timezone.now() + timezone.timedelta(days=7)

# Classes are database tables
# Functions inside classes define the columns of the table

# We create 2 tables/models:
# ToDoList: These are the lists that our tasks live in
# ToDoItem: These are our task items

class ToDoList(models.Model):
    # Title of the list
    # Simple character field limited to 100chars
    # List title must be unique
    title = models.CharField(max_length=100, unique=True)

    # Get the URL of the list
    # Using 'reverse' to avoid hard-coding the URL
    def get_absolute_url(self):
        return reverse("list", args=[self.id])
    
    # String representation of the model
    # By default, return the title of the list
    def __str__(self):
        return self.title
    
class ToDoItem(models.Model):
    # User that owns the task
    # One user to many tasks
    # 'on_delete': If user is deleted then set user field to null but keep tasks
    # 'null': User field can be null (makes testing easier, change to false later)
    # 'blank': Form submission can be blank (makes testing easier, change to false later)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    # Title of the task
    # Simple character field limited to 200chars
    # Task title must be unique
    title = models.CharField(max_length=200, unique=True)

    # Description of the task
    # Text field gives us a bigger box to enter text
    # Allowed to be empty
    description = models.TextField(null=True, blank=True)

    # Checkbox showing if the task is complete
    # Simple true/false boolean field
    # By default, the field is false
    complete = models.BooleanField(default=False)

    # Date the task was created
    # DateTime field
    # Auto populate current date
    created_date = models.DateTimeField(auto_now_add=True)

    # Date the task is due
    # DateTime field
    # By default, set this to one week from today using pre-set function
    due_date = models.DateTimeField(default=one_week_from_today)

    # ToDo list that the task lives in
    # One list to many tasks
    # Connect to the ToDoList model by using a ForeignKey
    # 'on_delete': If the list is deleted, all tasks inside it are also deleted
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_aboslute_url(self):
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )
    
    # Set the string representation of the model
    # By default, return the title of the task and the due date
    def __str__(self):
        return f"{self.title}: due {self.due_date}"
    
    # Add a Meta class to control the ordering of the tasks
    # Order by complete status and then by due date
    class Meta:
        ordering = ["complete", "due_date"]
