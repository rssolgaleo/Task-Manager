from django.urls import path
from task_manager.users import views
from task_manager.users.views import UserListView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='user_create'),
    path("", UserListView.as_view(), name="user_list"),
    path("<int:pk>/update/", UserUpdateView.as_view(), name="user_update"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="user_delete"),
]
