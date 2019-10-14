from django.db import models
import datetime

class Project(models.Model):
    title: models.CharField(max_length=100)
    statement: models.CharField(max_length=300)
    date_start: models.DateTimeField(auto_now_add=True)
    date_end: models.DateTimeField(auto_now=False, auto_now_add=False)
    date_deadline: models.DateTimeField(auto_now=False, auto_now_add=False)

class Student(models.Model):
    name: models.CharField(max_length=100)
    year: models.IntegerField(validators=[MaxValueValidator(datetime.datetime.now().year+3), MinValueValidator(2014)])

class Course(models.Model):
    title: models.CharField(max_length=100)
    year: models.IntegerField
    teacher: models.CharField(max_length=100)