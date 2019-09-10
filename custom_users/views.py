from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect, get_object_or_404
from lessons.models import Lesson
from .forms import AddSchoolForm, StudentForm, TeacherForm, StudentProfileForm, TeacherProfileForm
from .models import Class_id, School, TeacherProfile, StudentProfile
from .utils import (create_student_and_login, create_teacher_and_login, do_not_have_student_details,
do_not_have_teacher_details, get_progress, user_is_teacher, user_is_student, have_student_details,
have_teacher_details, have_student_signup,is_finished, save_school_details, save_student_details)
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
@login_required
@user_passes_test(user_is_teacher)
@user_passes_test(have_teacher_details, login_url = 'edit_teacher',  redirect_field_name = 'get_teacher_details' )
def welcome_teacher(request):
    teacher = TeacherProfile.objects.get(user_id = request.user.id)
    classes = Class_id.objects.filter(teacher = teacher)
    return render(request, 'custom_users/welcome_teacher.html', {'teacher': teacher,
    'classes':classes
    })


"""
Welcome student view. Displays the default template for any authenticated student user.
Shows a students next lesson, test and gives overall summary of progress.
"""
@login_required
@user_passes_test(user_is_student)
@user_passes_test(have_student_details, login_url = 'edit_student',  redirect_field_name = 'get_student_details' )
@user_passes_test(have_student_signup,  login_url = 'do_signup_quiz', redirect_field_name = 'do_signup_quiz')
def welcome_student(request):
    student = StudentProfile.objects.select_related().get(user_id = request.user.id)
    if is_finished(request.user):
        return redirect('congratulations')
    next_lesson = Lesson.objects.get(id = student.next_lesson_id)
    progress = get_progress(request.user.id)
    completed_exams = CompletedExam.objects.filter(user = student)
    return render(request, 'custom_users/welcome_student.html', {'student': student,
    'next_lesson':next_lesson,
    'progress': progress,
    'completed_exams' : completed_exams,
    })


"""
Displays the default template for an unauthenticated user.
Give option to signup as student/teacher or to login.
"""
def signup(request):
    return render(request, 'signup.html')

"""
Displays an empty Sign up form for a student user.
A User and StudentProfile are created from form data at the same time.
The new student user is logged in and redirected to add their details
through the edit_student template.
"""
def signup_form_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            create_student_and_login(request, form)
            return redirect('edit_student')
        else:
            return render(request, 'signup_form_student.html', {'form': form})
    else:
        form=StudentForm()
        return render(request, 'signup_form_student.html', {'form': form})


"""
Displays an empty Sign up form for a teacher user.
A User and TeacherProfile are created from form data at the same time.
The new teacher user is logged in and redirected to add their details
through the edit_teacher template.
"""
def signup_form_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            create_teacher_and_login(request, form)
            return redirect('edit_teacher')
        else:
            return render(request, 'signup_form_teacher.html', {'form': form})
    else:
        form=TeacherForm()
        return render(request, 'signup_form_teacher.html', {'form': form})

"""
Default view for authenticated user.
Displays either welcome_student or welcome_teacher template.
If the user is unauthenticated they are redirected to the signup template
"""

def home(request):
    if request.user.is_authenticated:
        try:
            student = StudentProfile.objects.select_related().get(user_id = request.user.id)
            if student:
                return redirect('welcome_student')
        except:
            teacher = TeacherProfile.objects.get(user_id = request.user.id)
            classes = Class_id.objects.filter(teacher = teacher)
            if teacher:
                return render(request, 'custom_users/welcome_teacher.html',{'classes':classes})
    else:
        return redirect('signup')

"""
Gets form to add student details, validates data and saves valid
information to the database.
"""
@login_required
@user_passes_test(user_is_student)
@user_passes_test(do_not_have_student_details, login_url = 'welcome_student')
def edit_student(request):
    student = StudentProfile.objects.get(user_id = request.user.id)
    if request.method == 'POST':
        student = get_object_or_404(StudentProfile, user_id = request.user.id)
        form = StudentProfileForm(request.POST, instance = student)
        if form.is_valid():
            save_student_details(form)
            return redirect('student_details_added')
        else:
            return render(request, 'custom_users/edit_student.html', {'form': form})
    else:
        form=StudentProfileForm()
        return render(request, 'custom_users/edit_student.html', {'form': form})

"""
Gets form to add teacher details, validates data and saves valid
information to the database.
"""
@login_required
@user_passes_test(user_is_teacher)
@user_passes_test(do_not_have_teacher_details, login_url = 'welcome_teacher')
def edit_teacher(request):
    teacher = TeacherProfile.objects.get(user_id = request.user.id)
    if request.method == 'POST':
        user = request.user
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
            return render(request, 'custom_users/edit_teacher.html', {'form': form})
    else:
        form=TeacherProfileForm()
        return render(request, 'custom_users/edit_teacher.html', {'form': form})

"""
Gets form to add a new school, validates data and saves valid
information to the database.
"""
@login_required
@user_passes_test(user_is_teacher, login_url = 'welcome_student')
def add_school(request):
    if request.method == 'POST':
        user = request.user
        teacher = TeacherProfile.objects.get(user_id = user.id)
        form = AddSchoolForm(request.POST)
        if form.is_valid():
            save_school_details(form)
            return redirect('edit_teacher')
        else:
            return render(request, 'custom_users/add_school.html', {'form': form})
    else:
        form=AddSchoolForm()
        return render(request, 'custom_users/add_school.html', {'form': form})

"""
Displays a summary of the details just added by the student user when
signing up.
"""
@login_required
@user_passes_test(user_is_student)
def student_details_added(request):
    student = StudentProfile.objects.get(user_id = request.user.id)
    return render(request, 'custom_users/student_details_added.html', {'student': student})

"""
Displays a summary of the details just added by the teacher user when
signing up.
"""
@login_required
@user_passes_test(user_is_teacher)
def teacher_details_added(request):
    teacher = TeacherProfile.objects.get(user_id = request.user.id)
    return render(request, 'custom_users/teacher_details_added.html', {'teacher': teacher})


"""
Used to create a dynamic dropdown menu within the add student details form.
When a student has selected their school this view updates the select teacher
dropdown menu, so that only teachers in that school can be selected.
"""
@login_required
@user_passes_test(user_is_student, login_url = 'welcome_teacher')
def ajax_load_teachers(request):
    school_id = request.GET.get('school')
    teachers = TeacherProfile.objects.filter(school=school_id).order_by('user_id')
    return render(request, 'custom_users/ajax_load_teachers.html', {'teachers': teachers})

"""
Used to create a dynamic dropdown menu within the add student details form.
When a student has selected their school and their teacher this view updates the
dropdown menu, so that only classes beloning to that teacher can be selected.
"""
@login_required
@user_passes_test(user_is_student, login_url = 'welcome_teacher')
def ajax_load_classes(request):
    teacher_id = request.GET.get('teacher')
    class_ids = Class_id.objects.filter(teacher=teacher_id).order_by('name')
    return render(request, 'custom_users/ajax_load_classes.html', {'class_ids': class_ids})

"""
Used to change a student's needs_help stats
which in turn changes the "help" icon on welcome_student page
"""
def get_help(request):
    student = StudentProfile.objects.get(user_id = request.user.id)
    student.needs_help = True
    student.save()
    return redirect('welcome_student')

def cancel_help(request):
    student = StudentProfile.objects.get(user_id = request.user.id)
    student.needs_help = False
    student.save()
    return redirect('welcome_student')
