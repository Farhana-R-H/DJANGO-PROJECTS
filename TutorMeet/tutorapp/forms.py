from django import forms
from django.contrib.auth.models import User
from .models import Profile
from .models import Session, Assignment

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    phone = forms.CharField(max_length=15)
    dob = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    # Adding user_type as a choice between 'student' and 'teacher'
    user_type = forms.ChoiceField(choices=[('student', 'Student'), ('teacher', 'Teacher')]) 

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        
        # Create profile for user with the user_type selected during registration
        user_profile = Profile.objects.create(user=user, user_type=self.cleaned_data['user_type'])
        return user_profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['phone', 'dob', 'guardian_name', 'guardian_phone', 'class_level', 'school_name', 'device_used', 'board', 'profile_picture']
    
    def save(self, commit=True):
        profile = super().save(commit=False)
        
        # Optionally, you can ensure that only teachers can edit user_type, or block this field from editing
        if commit:
            profile.save()
        return profile

class SessionForm(forms.ModelForm):
    # You can use ModelChoiceField to filter out the students related to the teacher
    students = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=True, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Session
        fields = ['date', 'topic', 'students']  # Allow the teacher to select students for the session
    
    def __init__(self, *args, **kwargs):
        teacher_user = kwargs.pop('teacher_user', None)
        super().__init__(*args, **kwargs)

        # If teacher is passed, filter students based on user_type
        if teacher_user:
            teacher_profile = Profile.objects.get(user=teacher_user)
            if teacher_profile.user_type == 'teacher':
                # Here we assume that we want to list students from the same teacher
                self.fields['students'].queryset = User.objects.filter(profile__user_type='student')

class AssignmentForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=True, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'students']  # Let the teacher select students to assign homework to
    
    def __init__(self, *args, **kwargs):
        teacher_user = kwargs.pop('teacher_user', None)
        super().__init__(*args, **kwargs)

        # Filter the students based on the teacher
        if teacher_user:
            teacher_profile = Profile.objects.get(user=teacher_user)
            if teacher_profile.user_type == 'teacher':
                self.fields['students'].queryset = User.objects.filter(profile__user_type='student')
