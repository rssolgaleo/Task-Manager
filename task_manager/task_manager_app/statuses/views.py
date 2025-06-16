from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from .models import Status
from .forms import StatusForm

class StatusListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses/status_list.html'
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixin, CreateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_form.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        messages.success(self.request, _("Status created successfully"))
        return super().form_valid(form)


class StatusUpdateView(LoginRequiredMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/status_form.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        messages.success(self.request, _("Status updated successfully"))
        return super().form_valid(form)


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'statuses/status_confirm_delete.html'
    success_url = reverse_lazy('status_list')

    def form_valid(self, form):
        messages.success(self.request, _("Status deleted successfully"))
        return super().form_valid(form)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            return super().delete(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, _("Cannot delete status because it is in use"))
            return redirect('status_list')
