from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from lessons.models import Lesson
from .forms import AddSchoolForm, StudentForm, TeacherForm, StudentProfileForm, TeacherProfileForm
from .models import Class_id, School, TeacherProfile, StudentProfile
from exams.models import CompletedExam

"""
The custom_users app is concerned with signup and login of users
Adding teacher and student data.
Registering teachers with schools and registering students with schools and teachers.
"""


"""
Welcome teacher view. Displays the default template for any authenticated teacher user.
Gets all of a teachers classes and displays a button for each.
"""
def welcome_teacher(request):
    if request.user.is_authenticated:
        try:
            teacher = TeacherProfile.objects.select_related().get(user_id = request.user.id)
            classes = Class_id.objects.filter(teacher = teacher)
            if teacher.details_added:
                return render(request, 'custom_users/welcome_teacher.html', {'teacher': teacher,
                'classes':classes
                })
            else:
                return redirect('edit_teacher')
        except:
            return redirect('home')
    else:
        return redirect('signup')

"""
Welcome student view. Displays the default template for any authenticated student user.
Shows a students next lesson, test and gives overall summary of progress.
"""
def welcome_student(request):
    if request.user.is_authenticated:
        try:
            student = StudentProfile.objects.select_related().get(user_id = request.user.id)
            if student.details_added and student.signup_quiz_completed:
                next_lesson = Lesson.objects.get(id = student.next_lesson_id)
                progress = (student.level/0.10)
                completed_exams = CompletedExam.objects.filter(user = student)
                return render(request, 'custom_users/welcome_student.html', {'student': student,
                'next_lesson':next_lesson,
                'progress': progress,
                'completed_exams' : completed_exams,
                })
            elif student.details_added:
                return redirect('do_signup_quiz')
            else:
                return redirect('edit_student')
        except:
            return redirect('home')
    else:
        return redirect('signup')


"""
Displays the default template for an unauthenticated user.
Give option to signup as student/teacher or to login.
"""
def signup(request):
    if not request.user.is_authenticated:
        return render(request, 'signup.html')
    else:
        return redirect('home')
"""
Displays an empty Sign up form for a student user.
A User and StudentProfile are created from form data at the same time.
The new student user is logged in and redirected to add their details
through the edit_student template.
"""
def signup_form_student(request):
    if not request.user.is_authenticated:
        try:
            TeacherProfile.objects.get(user_id = request.user.id)
            return redirect('home')
        except:
            if request.method == 'POST':
                form = StudentForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    user.refresh_from_db()
                    user.save()
                    student = StudentProfile.objects.create(user=user)
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(username=user.username, password=raw_password)
                    login(request, user)
                    return redirect('edit_student')
            else:
                form=StudentForm()
            return render(request, 'signup_form_student.html', {'form': form})
    else:
        return redirect('home')

"""
Displays an empty Sign up form for a teacher user.
A User and TeacherProfile are created from form data at the same time.
The new teacher user is logged in and redirected to add their details
through the edit_teacher template.
"""
def signup_form_teacher(request):
    if not request.user.is_authenticated:
        try:
            StudentProfile.objects.get(user_id = request.user.id)
            return redirect('home')
        except:
            if request.method == 'POST':
                form = TeacherForm(request.POST)
                if form.is_valid():
                    user = form.save()
                    user.refresh_from_db()
                    user.save()
                    TeacherProfile.objects.create(user=user)
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(username=user.username, password=raw_password)
                    login(request, user)
                    return redirect('edit_teacher')
            else:
                form=TeacherForm()
                return render(request, 'signup_form_teacher.html', {'form': form})
    else:
        return redirect('home')

"""
Default view for authenticated user.
Displays either welcome_student or welcome_teacher template.
If the user is unauthenticated they are redirected to the signup template
"""
def home(request):
    if request.user.is_authenticated:
        try:
            student = StudentProfile.objects.select_related().get(user_id = request.user.id)
            level = student.level.__str__()
            if student.details_added:
                return redirect('welcome_student')
            else:
                return redirect('edit_student')
        except:
            teacher = TeacherProfile.objects.get(user_id = request.user.id)
            classes = Class_id.objects.filter(teacher = teacher)
            if teacher.details_added:
                return render(request, 'custom_users/welcome_teacher.html',{'classes':classes})
            else:
                return redirect('edit_teacher')
    else:
            return redirect('signup')
"""
Gets form to add student details, validates data and saves valid
information to the database.
"""
def edit_student(request):
    if request.user.is_authenticated:
        try:
            student = StudentProfile.objects.get(user_id = request.user.id)
            if not student.details_added:
                if request.method == 'POST':
                    user = request.user
                    student = get_object_or_404(StudentProfile, user_id = user.id)
                    form = StudentProfileForm(request.POST, instance = student)
                    if form.is_valid():
                        student = form.save()
                        student.details_added = True
                        student.save()
                        return redirect('student_details_added')
                else:
                    form=StudentProfileForm()
                return render(request, 'custom_users/edit_student.html', {'form': form})
            else:
                return redirect('home')
        except:
            return redirect('home')
    else:
        return redirect('signup')
"""
Gets form to add teacher details, validates data and saves valid
information to the database.
"""
def edit_teacher(request):
    if request.user.is_authenticated:
        try:
            teacher = TeacherProfile.objects.get(user_id = request.user.id)
            if not teacher.details_added:
                if request.method == 'POST':
                    user = request.user
                    teacher = get_object_or_404(TeacherProfile, user_id = user.id)
                    form=TeacherProfileForm(request.POST)
                    if form.is_valid():
                        school = School.objects.get(id = request.POST['name'])
                        class_id = Class_id.objects.create(name = request.POST['class_name'], teacher = teacher)
                        teacher.school = school
                        teacher.class_id = class_id
                        teacher.details_added = True
                        teacher.save()
                        return render(request, 'custom_users/teacher_details_added.html', {'teacher':teacher})
                else:
                    form=TeacherProfileForm()
                    return render(request, 'custom_users/edit_teacher.html', {'form': form})
            else:
                return redirect('home')
        except:
            return redirect('home')
    else:
        return redirect('signup')

"""
Gets form to add a new school, validates data and saves valid
information to the database.
"""
def add_school(request):
    if request.user.is_authenticated:
        try:
            TeacherProfile.objects.get(user_id = request.user.id)
            if request.method == 'POST':
                user = request.user
                teacher = get_object_or_404(TeacherProfile, user_id = user.id)
                form = AddSchoolForm(request.POST)
                if form.is_valid():
                    school = form.save()
                    school.refresh_from_db()
                    school.save()
                    teacher.school = school
                    return render(request, 'custom_users/teacher_details_added.html', {'teacher': teacher})
            else:
                form=AddSchoolForm()
                return render(request, 'custom_users/add_school.html', {'form': form})
        except:
            return redirect('home')
    else:
        return redirect('signup')

"""
Displays a summary of the details just added by the student user when
signing up.
"""
def student_details_added(request):
    if request.user.is_authenticated:
        try:
            student = StudentProfile.objects.get(user_id = request.user.id)
            if student.details_added:
                return render(request, 'custom_users/student_details_added.html', {'student': student})
            else:
                return redirect('edit_student')
        except:
            return redirect('home')
    else:
        return redirect('signup')
"""
Displays a summary of the details just added by the teacher user when
signing up.
"""
def teacher_details_added(request):
    if request.user.is_authenticated:
        try:
            teacher = TeacherProfile.objects.get(user_id = request.user.id)
            if teacher.details_added:
                return render(request, 'custom_users/teacher_details_added.html', {'teacher': teacher})
            else:
                return redirect('edit_teacher')
        except:
            return redirect('home')
    else:
        return redirect('signup')

"""
Used to create a dynamic dropdown menu within the add student details form.
When a student has selected their school this view updates the select teacher
dropdown menu, so that only teachers in that school can be selected.
"""
def ajax_load_teachers(request):
    school_id = request.GET.get('school')
    teachers = TeacherProfile.objects.filter(school=school_id).order_by('user_id')
    return render(request, 'custom_users/ajax_load_teachers.html', {'teachers': teachers})

"""
Used to create a dynamic dropdown menu within the add student details form.
When a student has selected their school and their teacher this view updates the
dropdown menu, so that only classes beloning to that teacher can be selected.
"""
def ajax_load_classes(request):
    teacher_id = request.GET.get('teacher')
    class_ids = Class_id.objects.filter(teacher=teacher_id).order_by('name')
    return render(request, 'custom_users/ajax_load_classes.html', {'class_ids': class_ids})
