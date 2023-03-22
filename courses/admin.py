from django.contrib import admin
from .models import User, Course, Student, Enrollment, Longread, Task, Solution

admin.site.register(User)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Longread)
admin.site.register(Task)
admin.site.register(Solution)
