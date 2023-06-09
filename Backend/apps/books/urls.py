from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.BookList.as_view()),
    path('<int:pk>/', views.BookDetail.as_view()),
    path('add/', views.BookAdd.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)