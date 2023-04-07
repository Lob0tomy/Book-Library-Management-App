from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import ObtainUserTokenPairSerializer


class ObtainUserTokenPairView(TokenObtainPairView):
    serializer_class = ObtainUserTokenPairSerializer