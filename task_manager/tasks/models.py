from django.db import models
from task_manager.statuses.models import Status
from task_manager.labels.models import Label
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Task(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        verbose_name=_("Name"),
    )
    description = models.TextField(
        blank=True,
        verbose_name=_("Description"),
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT,
        related_name='tasks',
        verbose_name=_("Status")
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='authored_tasks',
        verbose_name=_("Author"),
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='executed_tasks',
        blank=True,
        null=True,
        verbose_name=_("Executor"),
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    labels = models.ManyToManyField(
        Label,
        related_name='tasks',
        blank=True,
        verbose_name=_("Labels"),
    )

    def __str__(self):
        return self.name
