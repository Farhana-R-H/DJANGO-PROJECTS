
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),

    path('teacher/dashboard/', views.teacher_dashboard, name='teacher_dashboard'),
path('teacher/session/create/', views.create_session, name='create_session'),
path('teacher/session/<int:session_id>/attendance/', views.view_session_attendance, name='view_session_attendance'),
path('teacher/assignment/create/', views.create_assignment, name='create_assignment'),
]
