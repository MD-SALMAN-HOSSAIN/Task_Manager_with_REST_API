
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from tasks import views
from tasks.views import TaskListCreateView, TaskRetrieveUpdateDestroyView, TaskPhotoListCreateView, \
    TaskPhotoRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.all_task, name='task_list'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('tasks/create/', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('tasks/<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('task/<int:task_id>/add_photo/', views.create_task_photo, name='add_photo'),
    path('task/<int:task_id>/delete_photo/<int:photo_id>/', views.delete_task_photo, name='delete_photo'),
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list'),
    path('api/tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('api/taskphotos/', TaskPhotoListCreateView.as_view(), name='taskphoto-list'),
    path('api/taskphotos/<int:pk>/', TaskPhotoRetrieveUpdateDestroyView.as_view(), name='taskphoto-detail'),
]

