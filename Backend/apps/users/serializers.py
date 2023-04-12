from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'phone_no', 'created', 'borrowed_books', 'photo', 'is_staff', 'is_admin', 'is_active']


