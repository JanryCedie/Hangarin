from django.core.management.base import BaseCommand
from taskmanager.models import Priority, Category, Task, SubTask, Note
from faker import Faker
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Creates initial fake data for the Task Manager app'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting to create initial data...")
        fake = Faker()

        # Create Priority records
        priority_names = ["high", "medium", "low", "critical", "optional"]
        priorities = []
        for name in priority_names:
            p, _ = Priority.objects.get_or_create(name=name)
            priorities.append(p)
        self.stdout.write(self.style.SUCCESS('Priorities generated.'))

        # Create Category records
        category_names = ["Work", "School", "Personal", "Finance", "Projects"]
        categories = []
        for name in category_names:
            c, _ = Category.objects.get_or_create(name=name)
            categories.append(c)
        self.stdout.write(self.style.SUCCESS('Categories generated.'))

        # Status sequences
        # The ERD requested statuses: Pending, In Progress, Completed
        status_elements = ["Pending", "In Progress", "Completed"]

        # Use Faker for Tasks
        self.stdout.write("Generating Tasks, Notes, and SubTasks (this may take a moment)...")
        tasks = []
        for _ in range(20):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=status_elements),
                category=random.choice(categories),
                priority=random.choice(priorities)
            )
            tasks.append(task)
            
            # Generate SubTasks
            for _ in range(random.randint(1, 4)):
                SubTask.objects.create(
                    title=fake.sentence(nb_words=4),
                    status=fake.random_element(elements=status_elements),
                    parent_task=task
                )
            
            # Generate Notes
            for _ in range(random.randint(1, 3)):
                Note.objects.create(
                    task=task,
                    content=fake.paragraph(nb_sentences=2)
                )

        self.stdout.write(self.style.SUCCESS('Successfully completed data generation!'))
