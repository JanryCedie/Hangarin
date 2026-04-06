from django.contrib import admin
from django.urls import path, include
from studentorg import views
from studentorg.views import (
    HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView,
    StudentListView, StudentCreateView, StudentUpdateView, StudentDeleteView,
    CollegeListView, CollegeCreateView, CollegeUpdateView, CollegeDeleteView,
    ProgramListView, ProgramCreateView, ProgramUpdateView, ProgramDeleteView,
    OrgMemberListView, OrgMemberCreateView, OrgMemberUpdateView, OrgMemberDeleteView
)

urlpatterns = [
    path('admin/logout/', views.admin_logout_view),
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('organization_list', OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add/', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/edit/<int:pk>/', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/delete/<int:pk>/', OrganizationDeleteView.as_view(), name='organization-delete'),
    path('student_list/', StudentListView.as_view(), name='student-list'),
    path('student_list/add/', StudentCreateView.as_view(), name='student-add'),
    path('student_list/edit/<int:pk>/', StudentUpdateView.as_view(), name='student-update'),
    path('student_list/delete/<int:pk>/', StudentDeleteView.as_view(), name='student-delete'),
    path('college_list/', CollegeListView.as_view(), name='college-list'),
    path('college_list/add/', CollegeCreateView.as_view(), name='college-add'),
    path('college_list/edit/<int:pk>/', CollegeUpdateView.as_view(), name='college-update'),
    path('college_list/delete/<int:pk>/', CollegeDeleteView.as_view(), name='college-delete'),
    path('program_list/', ProgramListView.as_view(), name='program-list'),
    path('program_list/add/', ProgramCreateView.as_view(), name='program-add'),
    path('program_list/edit/<int:pk>/', ProgramUpdateView.as_view(), name='program-update'),
    path('program_list/delete/<int:pk>/', ProgramDeleteView.as_view(), name='program-delete'),
    path('member_list/', OrgMemberListView.as_view(), name='member-list'),
    path('member_list/add/', OrgMemberCreateView.as_view(), name='member-add'),
    path('member_list/edit/<int:pk>/', OrgMemberUpdateView.as_view(), name='member-update'),
    path('member_list/delete/<int:pk>/', OrgMemberDeleteView.as_view(), name='member-delete'),
    path('login/', views.LoginFormView.as_view(), name='app-login'),
    path('logout/', views.app_logout_view, name='app-logout'),
    path('accounts/', include('allauth.urls')),
    path('taskmanager/', include('taskmanager.urls')),
    path('', include('pwa.urls')),
]
