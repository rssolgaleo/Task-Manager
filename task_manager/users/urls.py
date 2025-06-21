from django.urls import path
from task_manager.users.views import (
  UserCreateView,
  UserListView,
  UserUpdateView,
  UserDeleteView,
)

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user_create'),
    path("", UserListView.as_view(), name="user_list"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
]
