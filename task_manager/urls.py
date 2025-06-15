from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='base'),
    path('admin/', admin.site.urls),
    path('users/', include('task_manager.task_manager_app.users.urls')),
]
