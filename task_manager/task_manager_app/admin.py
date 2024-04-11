from django.contrib import admin
from .models import User, Task
@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ['id','name','email','mobile']

@admin.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_display = ['user','task_detail','task_type']


