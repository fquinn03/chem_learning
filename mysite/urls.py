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
from django.contrib import admin
from django.urls import path
from exams.views import dotest, show_result, review
from lessons.views import complete_lesson
from teachers.views import class_list
from users.views import show_students, welcome

urlpatterns = [
    path('show_students/<class_name>/<teacher_id>', show_students, name = 'show_students'),
    path('complete_lesson/<lesson_id>', complete_lesson, name = 'complete_lesson'),
    path('class_list/<user_id>', class_list, name = 'class_list'),
    path('admin/', admin.site.urls),
    path('dotest/<exam_id>', dotest, name='dotest'),
    path('not_teacher', class_list),
    path('finish_test', dotest),
    path('show_result/<exam_id>', show_result, name = 'show_result'),
    path('review/<exam_id>', review, name='review'),
    path('', welcome),
]
