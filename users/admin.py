from django.contrib import admin
from .models import User
from .models import StudentProfile
from .models import TeacherProfile
from .models import Class_id

admin.site.register(User)
admin.site.register(StudentProfile)
admin.site.register(TeacherProfile)
admin.site.register(Class_id)
