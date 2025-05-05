from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    dob = models.DateField(default='2000-01-01')
    guardian_name = models.CharField(max_length=100, blank=True, null=True)
    guardian_phone = models.CharField(max_length=15, blank=True, null=True)
    class_level = models.CharField(max_length=50, blank=True, null=True)
    school_name = models.CharField(max_length=255, blank=True, null=True)
    device_used = models.CharField(max_length=50, blank=True, null=True)
    board = models.CharField(max_length=10, choices=[('CBSE', 'CBSE'), ('State', 'State')], blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', default='default.jpg')
    USER_TYPE_CHOICES = [
    ('student', 'Student'),
    ('teacher', 'Teacher'),
]
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='student')
    def __str__(self):
        return self.user.username

class Session(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)  # Teacher who is conducting the session
    date = models.DateTimeField()  # When the session is scheduled
    topic = models.CharField(max_length=255)  # What the session is about
    students = models.ManyToManyField(User, related_name="sessions")  # Students invited to the session

    def __str__(self):
        return f"Session: {self.topic} on {self.date}"

# Model to track attendance for each student in a session
class Attendance(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)  # Which session the attendance is for
    student = models.ForeignKey(User, on_delete=models.CASCADE)  # Which student
    present = models.BooleanField(default=False)  # Was the student present?

    def __str__(self):
        return f"Attendance for {self.student.username} in session {self.session.topic}"

# Model for Assignments
class Assignment(models.Model):
    title = models.CharField(max_length=100)  # The title of the assignment
    description = models.TextField()  # Details about the assignment
    due_date = models.DateTimeField()  # When is the assignment due
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)  # Who created the assignment
    students = models.ManyToManyField(User, related_name='assignments')  # Which students will do it

    def __str__(self):
        return self.title
