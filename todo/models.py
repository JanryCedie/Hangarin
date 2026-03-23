from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Priority(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Task(BaseModel):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Completed", "Completed"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE, related_name="tasks")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="tasks")

    def __str__(self):
        return self.title

    @property
    def progress_percentage(self):
        total = self.subtasks.count()
        if total == 0:
            return 100 if self.status == 'Completed' else 0
        completed = self.subtasks.filter(status='Completed').count()
        return int((completed / total) * 100)

class Note(BaseModel):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="notes")
    content = models.TextField()

    def __str__(self):
        return f"Note for {self.task.title}"

class SubTask(BaseModel):
    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Completed", "Completed"),
    ]
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtasks")
    title = models.CharField(max_length=255)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")

    def __str__(self):
        return self.title
