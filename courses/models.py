from django.db import models

# Create your models here.
class User(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()

class Course(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    body = models.TextField()
    author = models.ForeignKey('User', related_name='courses', on_delete=models.CASCADE)

class Student(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  courses = models.ManyToManyField(Course)
