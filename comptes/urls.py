from django.urls import path
from . import views
from django.contrib.auth import views as myviews

app_name = 'comptes'

urlpatterns = [
    path('register/', views.registerDepute, name="registerDepute"),
    path('login/', views.loginDepute, name="loginDepute"),
    path('validation/', views.validation, name="validation"),
    path('logout/', views.logout, name="logout"),
    path('check_input_connexion/<str:nom>', views.check_input_connexion, name='check_input_connexion'),
    path('check_input_validation/<str:nom>', views.check_input_validation, name='check_input_validation'),
    path('reset_password/', myviews.PasswordResetView.as_view(template_name='comptes/password_reset.html'), name='reset_password'),
    path('reset_password_send/', myviews.PasswordResetDoneView.as_view(template_name='comptes/password_reset_sent.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', myviews.PasswordResetConfirmView.as_view(template_name='comptes/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', myviews.PasswordResetCompleteView.as_view(template_name='comptes/password_reset_done.html'), name='password_reset_complete'),
]
