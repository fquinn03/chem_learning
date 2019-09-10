from django.contrib.auth import login, authenticate
from .models import Class_id, School, StudentProfile, TeacherProfile

"""
Code for user_passes_test tests
"""
# returns True if teacher has NOT added their details
def do_not_have_teacher_details(user):
    teacher = TeacherProfile.objects.get(user_id = user.id)
    return not teacher.details_added

# returns True if student has NOT added their details
def do_not_have_student_details(user):
    student = StudentProfile.objects.get(user_id = user.id)
    return not student.details_added

# returns True if student has NOT completed signup quiz
def sign_up_quiz_already_completed(user):
    student = StudentProfile.objects.get(user_id = user.id)
    return not student.signup_quiz_completed

# returns True if teacher has added their details
def have_teacher_details(user):
    teacher = TeacherProfile.objects.get(user_id = user.id)
    return teacher.details_added

# returns True if student has added their details
def have_student_details(user):
    student = StudentProfile.objects.get(user_id = user.id)
    return student.details_added

# returns True if student has completed signup quiz
def have_student_signup(user):
    student = StudentProfile.objects.get(user_id = user.id)
    return student.signup_quiz_completed

# returns True if the user is a student
def user_is_student(user):
    try:
        StudentProfile.objects.get(user_id = user.id)
        return True
    except:
        return False

# returns True if the user is a teacher
def user_is_teacher(user):
    try:
        TeacherProfile.objects.get(user_id = user.id)
        return True
    except:
        return False

# returns True if the student has completed all lcvels
def is_finished(user):
    student = StudentProfile.objects.get(user_id = user.id)
    return student.level > 4 #hardcoded final level number

"""
Code to get width of progress bar
Needs to be changed depending on number of levels
"""
def get_progress(user):
    student = StudentProfile.objects.get(user_id = user)
    progress = ((student.level-1)*25) #hardcoded depending on how many levels
    if progress > 100:
        progress = 100
    return progress

"""
create student in the database and log them in
"""
def create_student_and_login(request, form):
    user = form.save()
    user.refresh_from_db()
    user.save()
    student = StudentProfile.objects.create(user=user)
    raw_password = form.cleaned_data.get('password1')
    user = authenticate(username=user.username, password=raw_password)
    login(request, user)

"""
create teacher in the database and log them
"""
def create_teacher_and_login(request, form):
    user = form.save()
    user.refresh_from_db()
    user.save()
    TeacherProfile.objects.create(user=user)
    raw_password = form.cleaned_data.get('password1')
    user = authenticate(username=user.username, password=raw_password)
    login(request, user)

"""
Save student details when the add them at signup
"""
def save_student_details(form):
    student = form.save()
    student.details_added = True
    student.save()

"""
Save school details when teacher creates new school if theirs is
missing at signup
"""
def save_school_details(form):
    school = form.save()
    school.refresh_from_db()
    school.save()
