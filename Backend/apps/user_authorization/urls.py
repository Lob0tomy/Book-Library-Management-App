from .views import UserRegisterView, LogoutView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('register/', UserRegisterView.as_view()),
    path('logout/', LogoutView.as_view())
]