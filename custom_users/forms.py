from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Class_id, School, StudentProfile, TeacherProfile

"""
Forms used to capture new user, username and password at signup,
and student or teacher data at signup.
"""


"""
First part of new student signup.
Form to create a new user.
"""
class StudentForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username', 'password1', 'password2')

"""
First part of new teacher signup.
Form to create a new user.
"""
class TeacherForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username', 'password1', 'password2')

"""
Second part of new student user signup.
Form to capture School, Teacher and Class details.
"""
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ('school', 'teacher', 'class_id')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['teacher'].queryset = TeacherProfile.objects.none() #no options available until school selected
        self.fields['class_id'].queryset = Class_id.objects.none() #no options available until teacher selected

        if 'school' in self.data: # if school has been selected
            try:
                school_id = int(self.data.get('school'))
                # update dropdown to contain teachers from that school
                self.fields['teacher'].queryset = TeacherProfile.objects.filter(school=school_id)
            except (ValueError, TypeError):
                self.fields['teacher'].queryset = TeacherProfile.objects.none()

        if 'teacher' in self.data: # if teacher has been selected
            try:
                teacher_id = int(self.data.get('teacher'))
                # update dropdown to contain the teacher's classes
                self.fields['class_id'].queryset = Class_id.objects.filter(teacher=teacher_id)
            except (ValueError, TypeError):
                self.fields['class_id'].queryset = Class_id.objects.none()
"""
Second part of new teacher user signup.
Form to capture School and Class details.
"""
class TeacherProfileForm(forms.Form):
    name = forms.ModelMultipleChoiceField(School.objects.order_by('name'))
    class_name = forms.CharField()

class AddSchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('name', 'post_code')
