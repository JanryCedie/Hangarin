from studentorg.models import Organization, Student, College, Program

def sidebar_counts(request):
    return {
        'org_count': Organization.objects.count(),
        'student_count': Student.objects.count(),
        'college_count': College.objects.count(),
        'program_count': Program.objects.count(),
    }
