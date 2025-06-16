from django.db import models
from django.contrib.auth.models import User
from task_manager.task_manager_app.statuses.models import Status

class Task(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, related_name='tasks')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authored_tasks')
    executor = models.ForeignKey(User, on_delete=models.PROTECT, related_name='executed_tasks', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
