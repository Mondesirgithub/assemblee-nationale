from django.contrib import admin
from .models import Categorie, Article, ActualiteImage, ActualiteVideo
# Register your models here.


admin.site.register(Categorie)
admin.site.register(Article)
admin.site.register(ActualiteImage)
admin.site.register(ActualiteVideo)