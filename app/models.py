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
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

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


class StudentManager(BaseUserManager):
    def create_student(self, email, year, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError("Students must have an email address")
        if not year:
            raise ValueError("Students must have a year of graduating")

        student = self.model(email=self.normalize_email(email), year=year)

        student.set_password(password)
        student.save(using=self._db)
        return student

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        student = self.create_student(email, password=password)
        student.staff = True
        student.save(using=self._db)
        return student

    def create_superuser(self, email, year, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        student = self.create_student(email, year, password=password)
        student.staff = True
        student.admin = True
        student.save(using=self._db)
        return student


class Student(AbstractBaseUser):
    year = models.IntegerField(
        validators=[
            MaxValueValidator(datetime.datetime.now().year + 5),
            MinValueValidator(2011),
        ],
        default=2011,
    )
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["year"]

    objects = StudentManager()

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin
