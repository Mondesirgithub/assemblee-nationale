from django.contrib import admin
from .models import Categorie, Article, ActualiteImage, ActualiteVideo, ImageAssociee
# Register your models here.


admin.site.register(Categorie)
admin.site.register(Article)
admin.site.register(ImageAssociee)
admin.site.register(ActualiteImage)
admin.site.register(ActualiteVideo)