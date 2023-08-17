from django.urls import path
from .views import TodoItemListCreateView , TodoItemUpdateDestroyView , UserRegistrationView , TodoItemListView ,TodoItemCreateView, TodoItemUpdateView,TodoItemDeleteView
from . import views

urlpatterns=[
    path('api/register/', UserRegistrationView.as_view(), name='register-api'), 
    path('api/todo/',TodoItemListCreateView.as_view(),name='todo-list-create-api'),
    path('api/todo/<int:todo_id>/',TodoItemUpdateDestroyView.as_view(), name='todo-list-details-api'),
    path('todo/',TodoItemListView.as_view(), name='todo-list'),
    path('add-todo/', TodoItemCreateView.as_view(),name='add-todo'),
    path('edit-todo/<int:pk>/', TodoItemUpdateView.as_view(), name='edit-todo'),
    path('delete-todo/<int:pk>/',TodoItemDeleteView.as_view(),name='delete-todo'),
    path('complete/<int:todo_id>/', views.completed, name='complete-todo'),
    ]