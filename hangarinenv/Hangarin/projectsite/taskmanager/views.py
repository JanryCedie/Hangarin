from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, Category, Priority, Note, SubTask

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'task'
    paginate_by = 10

class TaskCreateView(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_del.html'
    success_url = reverse_lazy('task-list')

class CategoryListView(ListView):
    model = Category
    template_name = 'category_list.html'
    context_object_name = 'category'
    paginate_by = 10

class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'category_form.html'
    success_url = reverse_lazy('category-list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'category_del.html'
    success_url = reverse_lazy('category-list')

class PriorityListView(ListView):
    model = Priority
    template_name = 'priority_list.html'
    context_object_name = 'priority'
    paginate_by = 10

class PriorityCreateView(CreateView):
    model = Priority
    fields = '__all__'
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityUpdateView(UpdateView):
    model = Priority
    fields = '__all__'
    template_name = 'priority_form.html'
    success_url = reverse_lazy('priority-list')

class PriorityDeleteView(DeleteView):
    model = Priority
    template_name = 'priority_del.html'
    success_url = reverse_lazy('priority-list')

class NoteListView(ListView):
    model = Note
    template_name = 'note_list.html'
    context_object_name = 'note'
    paginate_by = 10

class NoteCreateView(CreateView):
    model = Note
    fields = '__all__'
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteUpdateView(UpdateView):
    model = Note
    fields = '__all__'
    template_name = 'note_form.html'
    success_url = reverse_lazy('note-list')

class NoteDeleteView(DeleteView):
    model = Note
    template_name = 'note_del.html'
    success_url = reverse_lazy('note-list')

class SubTaskListView(ListView):
    model = SubTask
    template_name = 'subtask_list.html'
    context_object_name = 'subtask'
    paginate_by = 10

class SubTaskCreateView(CreateView):
    model = SubTask
    fields = '__all__'
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskUpdateView(UpdateView):
    model = SubTask
    fields = '__all__'
    template_name = 'subtask_form.html'
    success_url = reverse_lazy('subtask-list')

class SubTaskDeleteView(DeleteView):
    model = SubTask
    template_name = 'subtask_del.html'
    success_url = reverse_lazy('subtask-list')

