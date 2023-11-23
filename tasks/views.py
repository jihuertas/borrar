from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.views import View

# Create your views here.

def task_list(request):
    tasks = Task.objects.all()

    if request.method == 'POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form= TaskForm()
    return render(request,'tasks/task_list.html',{'tasks':tasks,'form':form})


class TaskList(View):
    tasks = Task.objects.all()
    nombre_template = 'tasks/task_list.html'

    def actualizaTask(self):
        self.tasks = Task.objects.all()
        return self.tasks

    def get(self, request):
        form= TaskForm()
        return render(request,self.nombre_template,{'tasks':self.actualizaTask(),'form':form})
    
    def post(self, request):
        form=TaskForm(request.POST)
        if form.is_valid():

            titulo = form.cleaned_data['title']
            description = form.cleaned_data['description']
            completed = form.cleaned_data['completed']

            Task.objects.create(title=titulo, description=description, completed=completed)
            #form.save()
            return redirect('task_list')
        return render(request,self.nombre_template,{'tasks':self.actualizaTask(),'form':form})



    
