from django.contrib import admin
from app import models

# Register your models here.
admin.site.register(models.Project)
admin.site.register(models.Student)
admin.site.register(models.Course)