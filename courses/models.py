from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  def __str__(self):
     return self.title

class Course(models.Model):                                                               # модель курсов             
    title = models.CharField(max_length=255)
    description = models.TextField()
#    body = models.TextField()
#    longread = models.CharField(max_length=255)
    author = models.ForeignKey('User', related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Student(models.Model):                                                             # модель студентов
    name = models.CharField(max_length=255)
    email = models.EmailField()
    courses = models.ManyToManyField(Course, through="Enrollment")
    level = models.IntegerField()

    def __str__(self):
        return self.title

class Enrollment(models.Model):                                                          # связь между студентами и курсами
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    mark = models.IntegerField()


class Longread(models.Model):                                                            # лонгрид
    title = models.CharField(max_length=255)
    course = models.ForeignKey('Course', related_name='longreads', on_delete=models.CASCADE)
    longread_id = models.IntegerField()

    def __str__(self):
        return self.title

class Task(models.Model):                                                                # задачи в лонгриде
    longread = models.ForeignKey('Longread', related_name='tasks', on_delete=models.CASCADE)
    condition = models.TextField()
    level = models.IntegerField()
    unit_id = models.IntegerField()
    trueAnswer = models.TextField()



class Solution(models.Model):                                                            # варианты решений к задаче
    variant = models.TextField()
    task = models.ForeignKey('Task', related_name='variant', on_delete=models.CASCADE)

class Unit(models.Model):                                                                # блоки текста в лонгриде
    title = models.CharField(max_length=255)
    body = models.TextField()
    level = models.IntegerField()
    unit_id = models.IntegerField()
    longread = models.ForeignKey('Longread', related_name='units', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
