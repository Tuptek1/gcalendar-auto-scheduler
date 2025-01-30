from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('tasks/', views.task_list, name= 'task_list'),
    path('tasks/add', views.task_add, name= 'task_add'),
    path('tasks/<str:task_id>/', views.task_detail, name= 'task_detail'),
    path('tasks/<str:task_id>/delete/', views.task_delete, name= 'task_delete'),
    path('tasks/<str:task_id>/edit/', views.task_edit, name= 'task_edit'),
]