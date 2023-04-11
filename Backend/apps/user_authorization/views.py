from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import UserObtainTokenPairSerializer, UserRegisterSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import login


class UserLoginView(TokenObtainPairView):
    serializer_class = UserObtainTokenPairSerializer

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer