from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('users/', include('task_manager.task_manager_app.users.urls')),
    path('statuses/', include('task_manager.task_manager_app.statuses.urls')),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tasks/', include('task_manager.task_manager_app.tasks.urls')),
    path('labels/', include('task_manager.task_manager_app.labels.urls')),
]
