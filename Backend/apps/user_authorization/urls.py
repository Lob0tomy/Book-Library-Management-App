from .views import ObtainUserTokenPairView
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('login/', ObtainUserTokenPairView.as_view()),
    path('login/refresh/', TokenRefreshView.as_view()),
]