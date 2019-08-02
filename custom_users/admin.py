from django.contrib import admin
from .models import StudentProfile
from .models import TeacherProfile
from .models import Class_id


class StudentProfileAdimin(admin.ModelAdmin):
    pass
admin.site.register(StudentProfile, StudentProfileAdimin)

class TeacherProfileAdmin(admin.ModelAdmin):
    pass
admin.site.register(TeacherProfile, TeacherProfileAdmin)

class Class_idAdmin(admin.ModelAdmin):
    pass
admin.site.register(Class_id, Class_idAdmin)
