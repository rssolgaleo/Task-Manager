from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from task_manager.tasks.models import Task
from task_manager.tasks.forms import TaskForm
from django_filters.views import FilterView
from task_manager.tasks.filters import TaskFilter
from django.shortcuts import redirect


class TaskListView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    filterset_class = TaskFilter

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, _('Task created successfully'))
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        messages.success(self.request, _('Task updated successfully'))
        return super().form_valid(form)


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'tasks/task_confirm_delete.html'
    success_url = reverse_lazy('task_list')

    def get(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != request.user:
            messages.error(request, _('You cannot delete a task you did not create'))
            return redirect(self.success_url)
        obj.delete()
        messages.success(request, _('Task deleted successfully'))
        return redirect(self.success_url)
