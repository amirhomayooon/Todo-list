from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    constext = {'tasks': tasks, 'form':form}
    return render(request, 'tasks/list.html', constext)

def updatetask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    constext = {'form':form}
    return render(request, 'tasks/update_task.html',constext)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    constext = {'item':item}
    return render(request, 'tasks/delete.html',constext)