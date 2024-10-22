from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import StudentAdminCreationForm, StudentAdminChangeForm
from .models import Student, Teacher, Course, Project, ProjectGroup


class StudentAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = StudentAdminChangeForm
    add_form = StudentAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ("email", "admin")
    list_filter = ("admin",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ()}),
        ("Permissions", {"fields": ("admin",)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "year", "password1", "password2"),
            },
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    filter_horizontal = ()


admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Project)
admin.site.register(ProjectGroup)

admin.site.unregister(Group)
