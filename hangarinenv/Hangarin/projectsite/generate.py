import os

models = ['Task', 'Category', 'Priority', 'Note', 'SubTask']
app_dir = r"c:\Users\Janry\OneDrive\Desktop\3rdyr.2ndsem\AppDev\Hangarin\hangarinenv\Hangarin\projectsite\taskmanager"
tpl_dir = r"c:\Users\Janry\OneDrive\Desktop\3rdyr.2ndsem\AppDev\Hangarin\hangarinenv\Hangarin\projectsite\templates"

# 1. Create taskmanager/urls.py
urls_content = '''from django.urls import path
from . import views

urlpatterns = [
'''
for m in models:
    lower = m.lower()
    urls_content += f'''    path('{lower}_list/', views.{m}ListView.as_view(), name='{lower}-list'),
    path('{lower}_add/', views.{m}CreateView.as_view(), name='{lower}-add'),
    path('{lower}_edit/<int:pk>/', views.{m}UpdateView.as_view(), name='{lower}-update'),
    path('{lower}_delete/<int:pk>/', views.{m}DeleteView.as_view(), name='{lower}-delete'),
'''
urls_content += ']\n'
with open(os.path.join(app_dir, 'urls.py'), 'w') as f:
    f.write(urls_content)

# 2. Create taskmanager/views.py
views_content = '''from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Task, Category, Priority, Note, SubTask

'''
for m in models:
    lower = m.lower()
    views_content += f'''class {m}ListView(ListView):
    model = {m}
    template_name = '{lower}_list.html'
    context_object_name = '{lower}'
    paginate_by = 10

class {m}CreateView(CreateView):
    model = {m}
    fields = '__all__'
    template_name = '{lower}_form.html'
    success_url = reverse_lazy('{lower}-list')

class {m}UpdateView(UpdateView):
    model = {m}
    fields = '__all__'
    template_name = '{lower}_form.html'
    success_url = reverse_lazy('{lower}-list')

class {m}DeleteView(DeleteView):
    model = {m}
    template_name = '{lower}_del.html'
    success_url = reverse_lazy('{lower}-list')

'''
with open(os.path.join(app_dir, 'views.py'), 'w') as f:
    f.write(views_content)

# 3. Create generic templates based on studentorg templates
for m in models:
    lower = m.lower()
    
    # List template
    list_tpl = f'''{{% extends 'base.html' %}}
{{% block content %}}
<div class="content">
    <div class="container-fluid">
        <h4 class="page-title">{m}s</h4>
        <div class="row">
            <div class="col-md-12">
                <div class="card">
                    <div class="card-header">
                        <div class="card-title">{m} List <a href="{{% url '{lower}-add' %}}" class="btn btn-primary btn-sm float-right">Add New</a></div>
                    </div>
                    <div class="card-body">
                        <table class="table table-striped mt-3">
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>{m} Name / Details</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {{% for item in {lower}_list %}}
                                <tr>
                                    <td>{{{{ item.id }}}}</td>
                                    <td>{{{{ item }}}}</td>
                                    <td>
                                        <a href="{{% url '{lower}-update' item.id %}}">Edit</a> |
                                        <a href="{{% url '{lower}-delete' item.id %}}" class="text-danger">Delete</a>
                                    </td>
                                </tr>
                                {{% empty %}}
                                <tr><td colspan="3" class="text-center">No records found.</td></tr>
                                {{% endfor %}}
                            </tbody>
                        </table>
                        {{% include 'includes/pagination.html' %}}
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{{% endblock %}}'''
    with open(os.path.join(tpl_dir, f'{lower}_list.html'), 'w') as f:
        f.write(list_tpl)

    # Form template
    form_tpl = f'''{{% extends 'base.html' %}}
{{% load widget_tweaks %}}
{{% block content %}}
<div class="content">
    <div class="container-fluid">
        <h4 class="page-title">{m} Form</h4>
        <div class="card">
            <div class="card-body">
                <form method="post">
                    {{% csrf_token %}}
                    {{% for field in form %}}
                    <div class="form-group">
                        <label>{{{{ field.label }}}}</label>
                        {{% render_field field class="form-control" %}}
                    </div>
                    {{% endfor %}}
                    <button type="submit" class="btn btn-success mt-3">Save</button>
                    <a href="{{% url '{lower}-list' %}}" class="btn btn-secondary mt-3">Cancel</a>
                </form>
            </div>
        </div>
    </div>
</div>
{{% endblock %}}'''
    with open(os.path.join(tpl_dir, f'{lower}_form.html'), 'w') as f:
        f.write(form_tpl)

    # Delete template
    del_tpl = f'''{{% extends 'base.html' %}}
{{% block content %}}
<div class="content">
    <div class="container-fluid">
        <h4 class="page-title">Delete {m}</h4>
        <div class="card">
            <div class="card-body text-center">
                <h5 class="text-danger mb-4">Are you sure you want to delete "{{{{ object }}}}"?</h5>
                <form method="post">
                    {{% csrf_token %}}
                    <button type="submit" class="btn btn-danger">Yes, Delete</button>
                    <a href="{{% url '{lower}-list' %}}" class="btn btn-secondary">Cancel</a>
                </form>
            </div>
        </div>
    </div>
</div>
{{% endblock %}}'''
    with open(os.path.join(tpl_dir, f'{lower}_del.html'), 'w') as f:
        f.write(del_tpl)

print("Generation complete!")
