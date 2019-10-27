from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)


class Course(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField
    course_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    statement = models.CharField(max_length=300)
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(
        auto_now=False, auto_now_add=False, blank=True, null=True
    )
    date_deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
