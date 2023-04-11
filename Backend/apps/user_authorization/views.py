from .serializers import UserRegisterSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from apps.users.permissions import UsersPermission

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer


class LogoutView(APIView):
    permission_classes = (UsersPermission,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)