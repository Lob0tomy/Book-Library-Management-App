from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from apps.users.models import User
from apps.users.serializers import UserSerializer
from .permissions import UsersPermission

class UserList(generics.ListAPIView):
    """
    List all registered users
    """
    permission_classes = [UsersPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['is_admin', 'is_staff', 'is_active']
    search_fields = ['email', 'first_name', 'last_name', 'phone_no']
    ordering_fields = ['email', 'first_name', 'last_name', 'created']


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [UsersPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer





