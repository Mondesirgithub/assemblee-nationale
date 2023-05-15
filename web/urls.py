from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/', views.articles, name='articles'),
    path('article-details/', views.article_details, name='article-details'),
]
