from .views import UserLoginView, UserRegisterView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', UserLoginView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('register/', UserRegisterView.as_view()),
]