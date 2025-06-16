from django import forms
from .models import Task
from task_manager.task_manager_app.statuses.models import Status
from django.contrib.auth.models import User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor']
