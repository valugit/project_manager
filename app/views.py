from app.models import Student, Teacher, Course, Project, ProjectGroup
from rest_framework import viewsets, permissions
from app.api import (
    StudentSerializer,
    TeacherSerializer,
    CourseSerializer,
    ProjectSerializer,
    ProjectGroupSerializer,
)
from app.permissions import IsOwnerOrReadOnly


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows teachers to be viewed or edited.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows courses to be viewed or edited.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """

    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def perform_create(self, serializer):
        serializer.save(creator_id=self.request.user)


class ProjectGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows project's groups to be viewed or edited.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = ProjectGroup.objects.all()
    serializer_class = ProjectGroupSerializer
