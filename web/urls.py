from django.urls import path
from . import views

app_name = 'comptes'

urlpatterns = [
    path('', views.index, name='index'),
    path('act/', views.actualite, name="act"),
    path('galerie/', views.galerie, name="galerie"),
]
