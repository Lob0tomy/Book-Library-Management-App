from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserObtainTokenPairSerializer, UserRegisterSerializer
from rest_framework import generics


class UserObtainTokenPairView(TokenObtainPairView):
    serializer_class = UserObtainTokenPairSerializer

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer