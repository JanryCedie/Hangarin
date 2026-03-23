import os
import django
import random
from faker import Faker
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from todo.models import Priority, Category, Task, Note, SubTask

fake = Faker()

def seed_data():
    # 1. Populating Priority
    priorities = ["High", "Medium", "Low", "Critical", "Optional"]
    priority_objs = []
    for p in priorities:
        obj, created = Priority.objects.get_or_create(name=p)
        priority_objs.append(obj)
    print(f"Created {len(priority_objs)} priorities.")

    # 2. Populating Category
    categories = ["Work", "School", "Personal", "Finance", "Projects"]
    category_objs = []
    for c in categories:
        obj, created = Category.objects.get_or_create(name=c)
        category_objs.append(obj)
    print(f"Created {len(category_objs)} categories.")

    # 3. Generating Random Tasks
    task_titles = [
        "Finish Midterm Project", "Buy Groceries", "Call Mom", "Fix Bug in API",
        "Prepare Presentation", "Clean the Room", "Enroll in React Course", "Pay Electricity Bill",
        "Read 10 Pages of Book", "Update Portfolio", "Go to Gym", "Meeting with Client",
        "Submit Weekly Report", "Plan Weekend Trip", "Organize Workspace", "Water the Plants",
        "Doctor's Appointment", "Research New Framework", "Renew Passport", "Attend Webinar"
    ]
    
    random.shuffle(task_titles)

    for i in range(20):
        title = task_titles[i] if i < len(task_titles) else fake.sentence(nb_words=4)
        status = random.choice(['Pending', 'In Progress', 'Completed'])
        category = random.choice(Category.objects.all())
        priority = random.choice(Priority.objects.all())
        deadline = timezone.now() + timezone.timedelta(days=random.randint(1, 30))
        
        task = Task.objects.create(
            title=title,
            description=fake.paragraph(nb_sentences=3),
            status=status,
            category=category,
            priority=priority,
            deadline=deadline
        )
        
        # Add a note
        Note.objects.create(
            task=task,
            content=fake.sentence()
        )
        
        # Add 1-4 subtasks
        for _ in range(random.randint(1, 4)):
            SubTask.objects.create(
                parent_task=task,
                title=fake.sentence(nb_words=3),
                status=random.choice(['Pending', 'Completed'])
            )

    print("Successfully seeded 20 tasks with notes and subtasks.")

if __name__ == "__main__":
    seed_data()
