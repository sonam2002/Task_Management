from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import User, Task
from .forms import UserForm, TaskForm
import openpyxl
from django.http import HttpResponse

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'app/add_user.html', {'form': form})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'app/add_task.html', {'form': form})

def user_list(request):
    users = User.objects.all()
    paginator = Paginator(users, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/user_list.html', {'page_obj': page_obj})

def task_list(request):
    tasks = Task.objects.all()
    paginator = Paginator(tasks, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'app/task_list.html', {'page_obj': page_obj})

def export_excel(request):
    users = User.objects.all()
    tasks = Task.objects.all()
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=task_manager_data.xlsx'

    wb = openpyxl.Workbook()
    user_sheet = wb.active
    user_sheet.title = 'Users'
    user_sheet.append(['Name', 'Email', 'Mobile'])
    for user in users:
        user_sheet.append([user.name, user.email, user.mobile])

    task_sheet = wb.create_sheet(title='Tasks')
    task_sheet.append(['User', 'Task Detail', 'Task Type'])
    for task in tasks:
        task_sheet.append([task.user.name, task.task_detail, task.task_type])

    wb.save(response)
    return response
