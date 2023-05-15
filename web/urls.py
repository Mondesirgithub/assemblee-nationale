from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<str:pk>', views.articles, name='articles'),
    path('article-details/<str:id>', views.article_details, name='article-details'),
]
