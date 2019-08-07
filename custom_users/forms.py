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

        if 'teacher' in self.data and 'class_id' in self.data:
            try:
                school_id = int(self.data.get('school'))
                self.fields['teacher'].queryset = TeacherProfile.objects.filter(school=school_id)
                teacher_id = int(self.data.get('teacher'))
                self.fields['class_id'].queryset = Class_id.objects.filter(teacher=teacher_id)
            except (ValueError, TypeError):
                pass
        """
        elif self.instance.pk:
            self.fields['teacher'].queryset = self.instance.school.teacher_set
            self.fields['class_id'].queryset = self.instance.teacher.class_id_set
        """
