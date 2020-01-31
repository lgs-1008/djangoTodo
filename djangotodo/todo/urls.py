from django.contrib import admin
from django.urls import path, include
from todo import views

app_name = 'todo'
urlpatterns = [
    path('', views.todoView, name = 'todoIndex'),
    path('todo/<pk>/delete/', views.todo_delete, name='todo_delete'),
]
