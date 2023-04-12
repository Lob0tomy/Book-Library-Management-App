from django.urls import path
from . import views
from .views import UserList

urlpatterns = [
    path('', UserList.as_view())

]