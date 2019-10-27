from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import datetime
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator


def validate_suponly_email(value):
    if not "@supinternet.fr" in value:
        raise ValidationError(
            "Sorry, the email submitted is invalid. All emails have to be from Sup'internet."
        )


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
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
        validators=[validate_suponly_email],
    )
    username = models.CharField(max_length=255, editable=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["year"]

    objects = StudentManager()

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.set_username()
        super(Student, self).save(*args, **kwargs)

    def set_username(self):
        return self.email.split("@")[0].replace(".", " ").title()

    def get_full_name(self):
        # The user is identified by their email address
        return self.username

    def get_short_name(self):
        # The user is identified by their email address
        return self.username

    def __str__(self):
        return self.username

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


class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Course(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField(
        validators=[
            MaxValueValidator(datetime.datetime.now().year + 5),
            MinValueValidator(2011),
        ],
        default=2011,
    )
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100)
    statement = models.TextField()
    date_start = models.DateTimeField(auto_now_add=True)
    date_deadline = models.DateTimeField(
        auto_now=False, auto_now_add=False, default=timezone.now
    )
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    creator_id = models.ForeignKey(Student, editable=False, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.creator_id:
            self.creator_id = self.set_creator_id()
        super(Project, self).save(*args, **kwargs)

    def set_creator_id(self):
        return request.user.id

    def __str__(self):
        return self.title


class ProjectGroup(models.Model):
    members = models.ManyToManyField(Student)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.project.title + " : " + self.members.all()[0].username + "'s group"
