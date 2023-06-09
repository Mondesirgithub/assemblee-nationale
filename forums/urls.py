from django.urls import path
from . import views

app_name = "forums"

urlpatterns = [
    path("", views.home, name="home"),
    path("detail/<slug>/", views.detail, name="detail"),
    path("posts/<slug>/", views.posts, name="posts"),
    path("latest_posts", views.latest_posts, name="latest_posts"),
    path("search", views.search_result, name="search_result"),
]