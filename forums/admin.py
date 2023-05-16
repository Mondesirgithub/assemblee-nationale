from django.contrib import admin
from .models import CategorieSujet, Sujet, Post
# Register your models here.


admin.site.register(CategorieSujet)
admin.site.register(Sujet)
admin.site.register(Post)