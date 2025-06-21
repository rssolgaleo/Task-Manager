from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(
        max_length=100,
        blank=False,
        verbose_name=_('First name'),
    )
    last_name = models.CharField(
        max_length=100,
        blank=False,
        verbose_name=_('Last name'),
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
