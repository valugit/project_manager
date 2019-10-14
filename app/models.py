from django.db import models

# Create your models here.
class Project(models.Model):
    project_title: models.CharField(max_length=100)
    project_statement: models.CharField(max_length=300)
    date_start: models.DateTimeField(auto_now_add=True)
    date_end: models.DateTimeField(auto_now=False, auto_now_add=False)
