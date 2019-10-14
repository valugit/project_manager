from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator

class Course(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField
    teacher = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    statement = models.CharField(max_length=300)
    date_start = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    date_deadline = models.DateTimeField(auto_now=False, auto_now_add=False)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    desc = models.TextField(max_length=500, blank=True)
    year = models.IntegerField(
        validators=[
            MaxValueValidator(datetime.datetime.now().year + 5),
            MinValueValidator(2014),
        ]
    )
    # users = User.objects.all().select_related('profile')


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

