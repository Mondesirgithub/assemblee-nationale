from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerDepute, name="registerDepute"),
    path('login/', views.loginDepute, name="loginDepute"),
]
