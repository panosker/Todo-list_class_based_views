from django.shortcuts import redirect
from django.urls import reverse
from django.db import models
from rest_framework.permissions import IsAdminUser
from django.db.models.query import QuerySet
from .serializers import TodoItemSerializer , UserSerializer
from .models import TodoItem
from rest_framework import generics
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView , UpdateView , DeleteView
from django.views.generic import ListView 
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

#API views

class TodoItemListCreateView(generics.ListCreateAPIView):
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes=IsAdminUser

class TodoItemUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset= TodoItem.objects.all()
    serializer_class = TodoItemSerializer
    permission_classes=IsAdminUser

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer    


#HTML rendered views
class TodoItemListView(LoginRequiredMixin,ListView):
    model = TodoItem
    template_name = 'todo-item-list.html'
    context_object_name = 'todo'

    def get_queryset(self):
        queryset= super().get_queryset()
        queryset = queryset.filter(user =self.request.user)
        return queryset
    
class TodoItemCreateView(CreateView):
    model= TodoItem
    fields=['title','body','date','time','complete']
    template_name='create-todo-item.html'
    context_object_name = 'todo'
    success_url = reverse_lazy('todo-list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TodoItemUpdateView(UpdateView):
    model = TodoItem
    fields=['title','body','date','time','complete']
    template_name='update-todo-item.html'
    context_object_name = 'todo'
    success_url = reverse_lazy('todo-list')

    def get_queryset(self):
        queryset= super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    

class TodoItemDeleteView(DeleteView):
    model = TodoItem
    fields='__all__'
    template_name='delete-todo-item.html'
    context_object_name = 'todo'
    success_url = reverse_lazy('todo-list')

    def get_queryset(self):
        queryset= super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
    

def completed(request,todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    if todo.complete==True:
        todo.complete=False
        todo.save()
    elif todo.complete==False:
        todo.complete=True
        todo.save()
    return redirect('todo-list')

    




