from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils import timezone
from studentorg.models import Organization, Student, College, Program, OrgMember
from .forms import OrganizationForm, StudentForm, CollegeForm, ProgramForm, OrgMemberForm

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('home')

    def get_success_url(self):
        next_url = self.request.GET.get('next') or self.request.POST.get('next')
        if next_url:
            return next_url
        return super().get_success_url()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(self.request, user)
            return super(LoginFormView, self).form_valid(form)
        else:
            return self.form_invalid(form)

def app_logout_view(request):
    logout(request)
    return redirect('app-login')

def admin_logout_view(request):
    logout(request)
    return redirect('admin:login')

class HomePageView(LoginRequiredMixin, ListView):
    model = Organization
    context_object_name = 'home'
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_students"] = Student.objects.count()
        context["total_organizations"] = Organization.objects.count()
        context["total_programs"] = Program.objects.count()

        today = timezone.now().date()
        count = (
            OrgMember.objects.filter(
                date_joined__year=today.year
            )
            .values("student")
            .distinct()
            .count()
        )

        context["students_joined_this_year"] = count
        return context

class OrganizationList(ListView):
    model = Organization
    template_name = 'org_list.html'
    context_object_name = 'organization'
    paginate_by = 10

    def get_ordering(self):
        allowed = ["name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "name"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Organization.objects.filter(Q(name__icontains=query) | Q(college__college_name__icontains=query) | Q(description__icontains=query))
        return Organization.objects.all()

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_form.html'
    success_url = reverse_lazy('organization-list')

class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'student'
    paginate_by = 10

    def get_ordering(self):
        allowed = ["lastname", "firstname", "student_id"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "lastname"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Student.objects.filter(Q(lastname__icontains=query) | Q(firstname__icontains=query) | Q(student_id__icontains=query))
        return Student.objects.all()

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('student-list')

class CollegeListView(ListView):
    model = College
    template_name = 'college_list.html'
    context_object_name = 'college'
    paginate_by = 10

    def get_ordering(self):
        allowed = ["college_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "college_name"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return College.objects.filter(Q(college_name__icontains=query))
        return College.objects.all()

class CollegeCreateView(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeUpdateView(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_form.html'
    success_url = reverse_lazy('college-list')

class CollegeDeleteView(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')

class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'
    context_object_name = 'program'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Program.objects.filter(Q(prog_name__icontains=query) | Q(college__college_name__icontains=query))
        return Program.objects.all()

    def get_ordering(self):
        allowed = ["prog_name", "college__college_name"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "prog_name"

class ProgramCreateView(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramUpdateView(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_form.html'
    success_url = reverse_lazy('program-list')

class ProgramDeleteView(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')

class OrgMemberListView(ListView):
    model = OrgMember
    template_name = 'member_list.html'
    context_object_name = 'member'
    paginate_by = 10

    def get_ordering(self):
        allowed = ["student__lastname", "organization__name", "date_joined"]
        sort_by = self.request.GET.get("sort_by")
        if sort_by in allowed:
            return sort_by
        return "student__lastname"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return OrgMember.objects.filter(Q(student__lastname__icontains=query) | Q(student__firstname__icontains=query) | Q(organization__name__icontains=query))
        return OrgMember.objects.all()

class OrgMemberCreateView(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'member_form.html'
    success_url = reverse_lazy('member-list')

class OrgMemberUpdateView(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'member_form.html'
    success_url = reverse_lazy('member-list')

class OrgMemberDeleteView(DeleteView):
    model = OrgMember
    template_name = 'member_del.html'
    success_url = reverse_lazy('member-list')
