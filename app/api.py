from app.models import Student, Teacher, Course, Project, ProjectGroup
from rest_framework import serializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Student
        fields = ["url", "username", "email", "year", "password"]

    def create(self, validated_data):
        user = super(StudentSerializer, self).create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teacher
        fields = ["url", "first_name", "last_name"]


class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = ["url", "title", "year", "teacher_id"]


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = [
            "url",
            "title",
            "statement",
            "date_start",
            "date_deadline",
            "course_id",
            "creator_id",
        ]


class ProjectGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectGroup
        fields = ["url", "members", "project"]
