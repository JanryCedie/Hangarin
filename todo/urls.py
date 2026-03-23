from django.urls import path
from django.contrib.auth import views as auth_views
from allauth.account import views as allauth_views
from . import views
from .views import (
    DashboardView, TaskListView, TaskDetailView, 
    TaskCreateView, TaskUpdateView, TaskDeleteView, ProfileView
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/add/', TaskCreateView.as_view(), name='task-add'),
    path('tasks/<int:pk>/edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('profile/', ProfileView.as_view(), name='profile'),
    
    # Auth
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('auth/social/<str:provider>/', views.mock_social_login, name='mock-social-login'),
]
