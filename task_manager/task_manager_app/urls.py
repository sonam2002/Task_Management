from django.urls import path
from . import views

urlpatterns = [
    path('add_user/', views.add_user, name='add_user'),
    path('add_task/', views.add_task, name='add_task'),
    path('users/', views.user_list, name='user_list'),
    path('tasks/', views.task_list, name='task_list'),
    path('exeldata_download/', views.export_excel, name='exeldata_download'),
    
]