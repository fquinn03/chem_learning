from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username', 'password1', 'password2')

class TeacherForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username', 'password1', 'password2')
