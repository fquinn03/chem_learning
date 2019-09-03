from django.contrib.auth.decorators import user_passes_test, login_required
from custom_users.utils import user_is_teacher, user_is_student, have_teacher_details
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from custom_users.models import Class_id, StudentProfile, TeacherProfile
from exams.models import Exam, Question, UserAnswer
from .forms import AddClassForm

"""
If user is a teacher, a list of their classes is sent to the template
If not they are redirected to not teacher template
"""
@login_required
@user_passes_test(user_is_teacher, login_url = 'welcome_student')
@user_passes_test(have_teacher_details, login_url = 'edit_teacher',  redirect_field_name = 'get_teacher_details' )
def class_list(request):
    user = request.user
    teacher = TeacherProfile.objects.get(user_id = user.id)
    classes = Class_id.objects.filter(teacher = teacher)
    return render(request, 'teachers/class_list.html', {
    'user': user,
    'classes':classes,
    })

"""
If a teacher clicks on a class in the above class_list view/template
A list of students in that class is sent to the template.
"""
@login_required
@user_passes_test(user_is_teacher)
@user_passes_test(have_teacher_details, login_url = 'edit_teacher',  redirect_field_name = 'get_teacher_details' )
def show_students(request, class_name):
    user = request.user
    teacher = TeacherProfile.objects.get(user_id = user.id)
    group = Class_id.objects.get(name = class_name, teacher_id = user.id)
    students = StudentProfile.objects.select_related().filter(class_id = group.id)
    return render(request, 'teachers/show_students.html', {
    'group': group,
    'students': students,
    })

@login_required
@user_passes_test(user_is_teacher)
@user_passes_test(have_teacher_details, login_url = 'edit_teacher',  redirect_field_name = 'get_teacher_details' )
def see_student_test(request, exam_id, student_id):
    student = StudentProfile.objects.get(user_id = student_id)
    exam = Exam.objects.get(id = exam_id)
    questions = Question.objects.all().filter(exam = exam_id)
    question_and_answer = {}
    for question in questions:
        answer = UserAnswer.objects.get(question = question.id, user = student.user_id)
        question_and_answer[question.text] = answer.user_answer
    return render(request, 'teachers/see_student_test.html', {
    'question_and_answer': question_and_answer,
    'student':student,
    'exam':exam
    })

@login_required
@user_passes_test(user_is_teacher)
@user_passes_test(have_teacher_details, login_url = 'edit_teacher',  redirect_field_name = 'get_teacher_details' )
def add_class(request):
    if request.method == 'POST':
        teacher = TeacherProfile.objects.get(user_id = request.user.id)
        form = AddClassForm(request.POST)
        if form.is_valid():
            class_name = form.cleaned_data['name']
            Class_id.objects.create(name = class_name, teacher = teacher)
            return redirect('welcome_teacher')
        else:
            return render(request, 'teachers/add_class.html', {'form': form})
    else:
        form=AddClassForm()
        return render(request, 'teachers/add_class.html', {'form': form})
