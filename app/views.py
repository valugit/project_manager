from app.models import Student, Teacher, Course, Project, ProjectGroup
from rest_framework import viewsets, permissions
from app.api import (
    StudentSerializer,
    TeacherSerializer,
    CourseSerializer,
    ProjectSerializer,
    ProjectGroupSerializer,
)


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """

    permission_classes = [permissions.IsAdminUser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """

    permission_classes = [permissions.IsAdminUser]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """

    permission_classes = [permissions.IsAdminUser]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """

    permission_classes = [permissions.IsAdminUser]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows project's groups to be viewed or edited.
    """

    permission_classes = [permissions.IsAdminUser]
    queryset = ProjectGroup.objects.all()
    serializer_class = ProjectGroupSerializer
