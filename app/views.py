from app.models import Student
from rest_framework import viewsets, permissions
from app.api import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """

    permission_classes = [permissions.IsAdminUser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
