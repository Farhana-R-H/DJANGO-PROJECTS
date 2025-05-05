from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileForm
from .models import Profile
from .models import Session, Attendance, Assignment
from .forms import SessionForm, AssignmentForm  

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            # Save user
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            # Save profile
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            # Log the user in
            login(request, user)

            # Redirect based on user_type
            if profile.user_type == 'teacher':
                return redirect('teacher_dashboard')
            else:
                return redirect('student_dashboard')

    else:
        user_form = UserRegisterForm()
        profile_form = ProfileForm()

    return render(request, 'registration/register.html', {
        'form': user_form,
        'profile_form': profile_form
    })

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user:
            # Log the user in
            login(request, user)

            # Get the profile of the logged-in user to check the user_type (teacher/student)
            profile = Profile.objects.get(user=user)

            # Check user_type to redirect to appropriate dashboard
            if profile.user_type == 'teacher':
                return redirect('teacher_dashboard')  # Redirect teacher to teacher's dashboard
            else:
                return redirect('student_dashboard')  # Redirect student to student dashboard
            
        else:
            return render(request, 'registration/login.html', {'error': 'Invalid credentials'})

    return render(request, 'registration/login.html')

def homepage(request):
    return render(request, 'homepage.html')
@login_required
def dashboard(request):
    profile = Profile.objects.get(user=request.user)

    if profile.user_type == 'teacher':
        return render(request, 'dashboard_teacher.html', {'profile': profile})
    else:
        return render(request, 'dashboard_student.html', {'profile': profile})
    
@login_required
def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)

    return render(request, 'profile_edit.html', {'form': form})


@login_required
def teacher_dashboard(request):
    profile = Profile.objects.get(user=request.user)
    
    if profile.user_type != 'teacher':  # If the user is not a teacher, redirect to student dashboard
        return redirect('student_dashboard')

    # Here you can load teacher-specific data like sessions, students' attendance, assignments, etc.
    sessions = Session.objects.filter(teacher=request.user)  # Fetch all sessions taught by the teacher
    assignments = Assignment.objects.filter(teacher=request.user)  # Fetch assignments given by the teacher

    return render(request, 'teacher_dashboard.html', {'profile': profile,'sessions': sessions, 'assignments': assignments})
@login_required
def create_session(request):
    profile = Profile.objects.get(user=request.user)

    if profile.user_type != 'teacher':
        return redirect('dashboard')  # Only teachers can create sessions

    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.teacher = request.user
            session.save()
            form.save_m2m()  # Save many-to-many field (students)

            # Create attendance records for each student in the session
            for student in session.students.all():
                Attendance.objects.create(session=session, student=student)

            return redirect('teacher_dashboard')
    else:
        form = SessionForm()

    return render(request, 'create_session.html', {'form': form})

@login_required
def view_session_attendance(request, session_id):
    session = Session.objects.get(id=session_id)
    profile = Profile.objects.get(user=request.user)

    # Only allow access if user is a teacher and owns the session
    if profile.user_type != 'teacher' or session.teacher != request.user:
        return redirect('dashboard')

    attendance_records = Attendance.objects.filter(session=session)

    if request.method == 'POST':
        for record in attendance_records:
            record.present = request.POST.get(f'present_{record.student.id}') == 'on'
            record.save()
        return redirect('teacher_dashboard')

    return render(request, 'view_session_attendance.html', {
        'session': session,
        'attendance_records': attendance_records
    })
@login_required
def create_assignment(request):
    profile = Profile.objects.get(user=request.user)

    if profile.user_type != 'teacher':
        return redirect('dashboard')

    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.teacher = request.user
            assignment.save()
            form.save_m2m()  # Save students assigned
            return redirect('teacher_dashboard')
    else:
        form = AssignmentForm()

    return render(request, 'create_assignment.html', {'form': form})