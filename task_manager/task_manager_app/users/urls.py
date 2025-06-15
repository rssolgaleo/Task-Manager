from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from task_manager.task_manager_app.users import views
from task_manager.task_manager_app.users.views import UserCreateView, UserListView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='user_create'),
    path('login/', LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("", UserListView.as_view(), name="user_list"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
]
