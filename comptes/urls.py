from django.urls import path
from . import views

app_name = 'comptes'

urlpatterns = [
    path('register/', views.registerDepute, name="registerDepute"),
    path('login/', views.loginDepute, name="loginDepute"),
    path('validation/', views.validation, name="validation"),
    path('logout/', views.logout, name="logout"),
]
