from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  def __str__(self):
     return self.title

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
#    body = models.TextField()
#    longread = models.CharField(max_length=255)
    author = models.ForeignKey('User', related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Student(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  courses = models.ManyToManyField(Course, through="Enrollment")

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    mark = models.IntegerField()

class Longread(models.Model):					#кажется логичным вынести это в отдельное приложение
    title = models.CharField(max_length=255)
    course = models.ForeignKey('Course', related_name='longreads', on_delete=models.CASCADE)

class Task(models.Model):
    longread = models.ForeignKey('Longread', related_name='tasks', on_delete=models.CASCADE)
    condition = models.TextField()

class Solution(models.Model):
    variant = models.TextField()
    task = models.ForeignKey('Task', related_name='variant', on_delete=models.CASCADE)
