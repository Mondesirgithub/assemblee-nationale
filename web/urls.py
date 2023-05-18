from django.urls import path
from . import views

app_name = 'web'

urlpatterns = [
    path('', views.index, name='index'),
    path('articles/<str:pk>', views.articles, name='articles'),
    path('article-details/<str:id>', views.article_details, name='article-details'),
    path('actualite-video-details/<str:id>', views.actualite_video_details, name='actualite-video-details'),
    path('actualite-image-details/<str:id>', views.actualite_image_details, name='actualite-image-details'),
    path('act/', views.actualite, name="act"),
    path('galerie/<str:id>', views.galerie, name='galerie'),
    path('President/', views.President, name='President'),
    path('Mmbr/', views.Membre, name='Membre'),
    path('contact1/', views.contact1, name='contact1'),
    path('contact2/', views.contact2, name='contact2'),
    path('calendrier/', views.calendrierS, name='calendrierS'),
    path('Liste/', views.Liste_des_Lois, name='Liste_de_loi'),
    path('Evenement_H/', views.Evenement_H, name='Evenement_H'),
    path('Travaux/', views.Travaux_en, name='Travaux'),
    path('Liste_depute/', views.Liste_des_depute_Fon, name='Liste_depute'),
    path('Ancien/', views.Ancien_President, name='Ancien'),
    path('Liste_d/', views.Liste_des_depute_P, name='Liste_d'),
    path('Annonce/', views.Annonce, name='Annonce'),
    path('Actualite/', views.Actualite, name='Actualite'),
    path('Galerie_p/', views.Galerie_p, name='Galerie_p'),
    path('Symbole/', views.Symbole, name='Symbole'),
    path('Vac/', views.Vac, name='Vac'),
]

   