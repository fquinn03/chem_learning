from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Class_id, School, StudentProfile, TeacherProfile

class StudentForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username', 'password1', 'password2')

class TeacherForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username', 'password1', 'password2')


class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('school', 'teacher', 'class_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].queryset = TeacherProfile.objects.none()
        self.fields['class_id'].queryset = Class_id.objects.none()
        if 'school' in self.data:
            try:
                school_id = int(self.data.get('school'))
                self.fields['teacher'].queryset = TeacherProfile.objects.filter(school=school_id).order_by(user_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['teacher'].queryset = self.instance.school.teacher_set.order_by(user_id)

        if 'class_id' in self.data:
            try:
                teacher_id = int(self.data.get('class_id'))
                self.fields['class_id'].queryset = Class_id.objects.filter(teacher=teacher_id).order_by(name)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['class_id'].queryset = self.instance.teacher.class_id_set.order_by(user_id)
