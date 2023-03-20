from django.contrib import admin
from .models import User, Course, Student, Enrollment

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)
