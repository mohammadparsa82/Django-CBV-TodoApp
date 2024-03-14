from django.shortcuts import render,redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.edit import (
    CreateView,UpdateView,DeleteView,)
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.forms import TaskForm

# Create your views here.



class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "task/list_task.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)

class CreatTask(CreateView,LoginRequiredMixin):
    model= Task
    fields = ['title','complete']
    success_url = '/tasks/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class UpdateTask(UpdateView, LoginRequiredMixin):
    model = Task
    success_url = '/tasks/'
    form_class = TaskForm
    template_name = 'tasks/update_task.html'

class DeleteTask(DeleteView, LoginRequiredMixin):
    model = Task
    context_object_name = "task"
    success_url = '/tasks/'

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)
    
class TaskComplete(LoginRequiredMixin, View):
    model = Task
    success_url = reverse_lazy("task_list")

    def get(self, request, *args, **kwargs):
        object = Task.objects.get(id=kwargs.get("pk"))
        object.complete = True
        object.save()
        return redirect(self.success_url)