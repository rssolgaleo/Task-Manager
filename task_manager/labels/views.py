from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from task_manager.labels.models import Label
from task_manager.labels.forms import LabelForm


class LabelListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels/label_list.html'
    context_object_name = 'labels'


class LabelCreateView(LoginRequiredMixin, CreateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    success_url = reverse_lazy('label_list')

    def form_valid(self, form):
        messages.success(self.request, _('Label created successfully'))
        return super().form_valid(form)


class LabelUpdateView(LoginRequiredMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'labels/label_form.html'
    success_url = reverse_lazy('label_list')

    def form_valid(self, form):
        messages.success(self.request, _('Label updated successfully'))
        return super().form_valid(form)


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'labels/label_confirm_delete.html'
    success_url = reverse_lazy('label_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.tasks.exists():
            messages.error(
                request, _('Cannot delete label because it is in use')
            )
            return redirect(self.success_url)

        messages.success(request, _('Label deleted successfully'))
        return super().post(request, *args, **kwargs)
