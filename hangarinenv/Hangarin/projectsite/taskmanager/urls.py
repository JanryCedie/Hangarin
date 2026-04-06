from django.urls import path
from . import views

urlpatterns = [
    path('task_list/', views.TaskListView.as_view(), name='task-list'),
    path('task_add/', views.TaskCreateView.as_view(), name='task-add'),
    path('task_edit/<int:pk>/', views.TaskUpdateView.as_view(), name='task-update'),
    path('task_delete/<int:pk>/', views.TaskDeleteView.as_view(), name='task-delete'),
    path('category_list/', views.CategoryListView.as_view(), name='category-list'),
    path('category_add/', views.CategoryCreateView.as_view(), name='category-add'),
    path('category_edit/<int:pk>/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category_delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('priority_list/', views.PriorityListView.as_view(), name='priority-list'),
    path('priority_add/', views.PriorityCreateView.as_view(), name='priority-add'),
    path('priority_edit/<int:pk>/', views.PriorityUpdateView.as_view(), name='priority-update'),
    path('priority_delete/<int:pk>/', views.PriorityDeleteView.as_view(), name='priority-delete'),
    path('note_list/', views.NoteListView.as_view(), name='note-list'),
    path('note_add/', views.NoteCreateView.as_view(), name='note-add'),
    path('note_edit/<int:pk>/', views.NoteUpdateView.as_view(), name='note-update'),
    path('note_delete/<int:pk>/', views.NoteDeleteView.as_view(), name='note-delete'),
    path('subtask_list/', views.SubTaskListView.as_view(), name='subtask-list'),
    path('subtask_add/', views.SubTaskCreateView.as_view(), name='subtask-add'),
    path('subtask_edit/<int:pk>/', views.SubTaskUpdateView.as_view(), name='subtask-update'),
    path('subtask_delete/<int:pk>/', views.SubTaskDeleteView.as_view(), name='subtask-delete'),
]
