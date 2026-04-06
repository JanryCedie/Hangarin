from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        self.ensure_basic_data()
        self.create_organization(10)
        self.create_students(50)
        self.create_membership(10)

    def ensure_basic_data(self):
        colleges = [
            'College of Arts and Sciences', 'College of Engineering',
            'College of Computer Studies', 'College of Business and Accountancy',
            'College of Education', 'College of Agriculture',
            'College of Nursing', 'College of Hospitality Management'
        ]
        for c_name in colleges:
            College.objects.get_or_create(college_name=c_name)

        programs = [
            ('BS in Computer Science', 'College of Computer Studies'),
            ('BS in Information Technology', 'College of Computer Studies'),
            ('BS in Civil Engineering', 'College of Engineering'),
            ('BS in Mechanical Engineering', 'College of Engineering'),
            ('BA in English', 'College of Arts and Sciences'),
            ('BS in Biology', 'College of Arts and Sciences')
        ]
        for p_name, c_name in programs:
            college = College.objects.get(college_name=c_name)
            Program.objects.get_or_create(prog_name=p_name, college=college)

    def create_organization(self, count):
        fake = Faker()
        for _ in range(count):
            words = [fake.word() for _ in range(2)] # two words
            organization_name = ' '.join(words)
            Organization.objects.create(
                name=organization_name.title(),
                college=College.objects.order_by('?').first(),
                description=fake.sentence()
            )
        self.stdout.write(self.style.SUCCESS('Initial data for organization created successfully.'))

    def create_students(self, count):
        fake = Faker('en_PH')
        for _ in range(count):
            Student.objects.create(
                student_id=f"{fake.random_int(2020, 2025)}-{fake.random_int(1,8)}-{fake.random_number(digits=4)}",
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=Program.objects.order_by('?').first()
            )
        self.stdout.write(self.style.SUCCESS('Initial data for students created successfully.'))

    def create_membership(self, count):
        fake = Faker()
        for _ in range(count):
            OrgMember.objects.create(
                student=Student.objects.order_by('?').first(),
                organization=Organization.objects.order_by('?').first(),
                date_joined=fake.date_between(start_date="-2y", end_date="today")
            )
        self.stdout.write(self.style.SUCCESS('Initial data for student organization created successfully.'))
