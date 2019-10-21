from django.contrib.auth.models import User, Group
from app.models import Student
from rest_framework import viewsets, permissions
from app.api import UserSerializer, GroupSerializer, StudentSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    permission_classes = [permissions.IsAdminUser]
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    permission_classes = [permissions.IsAdminUser]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """

    permission_classes = [permissions.IsAdminUser]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
