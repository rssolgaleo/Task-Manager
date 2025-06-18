import django_filters
from django import forms
from .models import Task
from task_manager.task_manager_app.statuses.models import Status
from django.contrib.auth.models import User
from task_manager.task_manager_app.labels.models import Label


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all(),
        label='Status',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    executor = django_filters.ModelChoiceFilter(
        queryset=User.objects.all(),
        label='Executor',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        label='Label',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    self_tasks = django_filters.BooleanFilter(
        method='filter_self_tasks',
        label='Only my tasks',
        widget=forms.CheckboxInput()
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']

    def filter_self_tasks(self, queryset, name, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset
