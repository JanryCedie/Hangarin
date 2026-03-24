from django.urls import path
from django.contrib.auth import views as auth_views
from allauth.account import views as allauth_views
from . import views
from .views import (
    DashboardView, TaskListView, TaskDetailView, 
    TaskCreateView, TaskUpdateView, TaskDeleteView, ProfileView,
    CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    PriorityListView, PriorityCreateView, PriorityUpdateView, PriorityDeleteView,
    SubTaskListView, SubTaskCreateView, SubTaskUpdateView, SubTaskDeleteView
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/add/', TaskCreateView.as_view(), name='task-add'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # Category CRUD
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category-add'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category-edit'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category-delete'),

    # Priority CRUD
    path('priorities/', PriorityListView.as_view(), name='priority-list'),
    path('priorities/add/', PriorityCreateView.as_view(), name='priority-add'),
    path('priorities/<int:pk>/edit/', PriorityUpdateView.as_view(), name='priority-edit'),
    path('priorities/<int:pk>/delete/', PriorityDeleteView.as_view(), name='priority-delete'),

    # SubTask CRUD
    path('subtasks/', SubTaskListView.as_view(), name='subtask-list'),
    path('subtasks/add/', SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtasks/<int:pk>/edit/', SubTaskUpdateView.as_view(), name='subtask-edit'),
    path('subtasks/<int:pk>/delete/', SubTaskDeleteView.as_view(), name='subtask-delete'),
    
    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('auth/social/<str:provider>/', views.mock_social_login, name='mock-social-login'),
]
