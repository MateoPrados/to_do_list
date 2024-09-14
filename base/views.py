from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy #to redirect 

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Task


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True #redirect to the tasks page if the user is already authenticated
    
    def get_success_url(self):
        return reverse_lazy('tasks')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks') #redirect to the tasks page after creating a task
    
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks') 
    
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    #template_name = 'base/task_delete.html' #use a custom template to delete a task
    
    