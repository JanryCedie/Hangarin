from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .models import Task, Category, Priority

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'todo/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        tasks = Task.objects.all()
        
        context['total_tasks'] = tasks.count()
        context['completed_tasks'] = tasks.filter(status='Completed').count()
        context['pending_tasks'] = tasks.filter(status='Pending').count()
        context['tasks_this_year'] = tasks.filter(deadline__year=now.year).count()
        
        # Recent tasks for dashboard
        context['recent_tasks'] = tasks.order_by('-created_at')[:5]
        return context

def mock_social_login(request, provider):
    # Mock social login: find or create a user and log them in
    username = f"{provider}_user"
    user, created = User.objects.get_or_create(username=username)
    if created:
        user.set_unusable_password()
        user.save()
    login(request, user)
    return redirect('dashboard')

def custom_logout(request):
    # Check if user is coming from admin
    referrer = request.META.get('HTTP_REFERER', '')
    is_admin = '/admin/' in referrer
    logout(request)
    if is_admin:
        return redirect('admin:login')
    return redirect('login')

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'todo/task_list.html'
    context_object_name = 'tasks'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search')
        category_id = self.request.GET.get('category')
        sort_by = self.request.GET.get('sort', '-created_at')

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(category__name__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        # Valid sort fields
        valid_sorts = ['title', 'created_at', 'deadline', 'status', '-title', '-created_at', '-deadline', '-status']
        if sort_by in valid_sorts:
            queryset = queryset.order_by(sort_by)
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['current_sort'] = self.request.GET.get('sort', '-created_at')
        context['current_search'] = self.request.GET.get('search', '')
        return context

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'todo/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'todo/task_form.html'
    fields = ['title', 'category', 'priority', 'deadline', 'status', 'description']
    success_url = reverse_lazy('task-list')

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'todo/task_form.html'
    fields = ['title', 'category', 'priority', 'deadline', 'status', 'description']
    success_url = reverse_lazy('task-list')

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'todo/task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'todo/profile.html'
