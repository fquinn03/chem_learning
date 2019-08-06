"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic.base import TemplateView
from exams.views import dotest, show_result, review
from lessons.views import complete_lesson
from teachers.views import class_list, show_students
from custom_users.views import (welcome_student, welcome_teacher, signup, signup_form_student,
signup_form_teacher, home, edit_student, student_details_added, ajax_load_teachers)

urlpatterns = [
    path('show_students/<class_name>', show_students, name = 'show_students'),
    path('complete_lesson/<lesson_id>', complete_lesson, name = 'complete_lesson'),
    path('class_list', class_list, name = 'class_list'),
    path('admin/', admin.site.urls),
    path('dotest/<exam_id>', dotest, name='dotest'),
    path('not_teacher', class_list),
    path('finish_test', dotest, name='finish_test'),
    path('show_result/<exam_id>', show_result, name = 'show_result'),
    path('review/<exam_id>', review, name='review'),
    path('welcome_student', welcome_student, name = 'welcome_student'),
    path('welcome_teacher', welcome_teacher, name = 'welcome_teacher'),
    path('users/', include('django.contrib.auth.urls')),
    path('signup', signup, name = 'signup'),
    path('signup_form_student', signup_form_student, name = 'signup_form_student'),
    path('signup_form_teacher', signup_form_teacher, name = 'signup_form_teacher'),
    path('edit_student', edit_student, name = 'edit_student'),
    path('student_details_added', student_details_added, name = 'student_details_added'),
    path('ajax_load_teachers', ajax_load_teachers, name = 'ajax_load_teachers'),
    path('', home, name='home'),

]
