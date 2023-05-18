from django.contrib import admin
from .models import (Categorie, Article, ActualiteImage, ActualiteVideo, ImageAssociee,Annonce,
                     SymbolesAssemblee,EvenementHemicycle,LoiAdoptee,TravauxCommission,Picture)
# Register your models here.



admin.site.register(Annonce)
admin.site.register(SymbolesAssemblee)
admin.site.register(EvenementHemicycle)
admin.site.register(LoiAdoptee)
admin.site.register(Categorie)
admin.site.register(TravauxCommission)
admin.site.register(Article)
admin.site.register(ImageAssociee)
admin.site.register(ActualiteImage)
admin.site.register(ActualiteVideo)
admin.site.register(Picture)

