from django.shortcuts import render
from .models import Categorie, Article, ActualiteImage, ActualiteVideo
from django.contrib import messages
# Create your views here.

def index(request):
    categories = Categorie.objects.all()
    actualiteVideo = ActualiteVideo.objects.order_by("-created_at").first()
    actualiteImage1 = ActualiteImage.objects.order_by("-created_at").first()
    actualiteImage2 = ActualiteImage.objects.order_by("-created_at").all()[1]
    
    image1 , image2 = actualiteImage1.imageassociee_set.all()[0], actualiteImage2.imageassociee_set.all()[0]
    
    context = {
        'categories': categories,
        'actualiteVideo': actualiteVideo,
        'actualiteImage1': actualiteImage1,
        'actualiteImage2': actualiteImage2,
        'image1':image1,
        'image2':image2
    }
    
    return render(request, 'web/index.html', context)



def article_details(request, id):
    try:
        article = Article.objects.get(pk=id)
        categorie = Categorie.objects.get(pk=article.categorie.pk)
        articles = categorie.article_set.all()
    except:
        messages.error(request, "L'article n'existe pas")

    context = {
        'article': article,
        'articles': articles
    }
    return render(request, 'web/article_details.html', context)


def articles(request, pk):
    try:
        categorie = Categorie.objects.get(pk=pk)
        articles = categorie.article_set.all()
    except:
        messages.error(request, "La categorie n'existe pas")

    context = {
        'articles': articles,
        'categorie': categorie
    }

    return render(request, 'web/articles.html', context)


def actualite_video_details(request, id):
    try:
        actualiteVideo = ActualiteVideo.objects.get(pk=id)
        videos = ActualiteVideo.objects.all()
    except:
        messages.error(request, "La video n'existe pas")
    
    context = {
        'actualiteVideo':actualiteVideo,
        'videos':videos
    }
    
    return render(request, 'web/actualite_video_details.html', context)




def actualite_image_details(request, id):
    try:
        actualiteImage = ActualiteImage.objects.get(pk=id)
        imageAssociees = actualiteImage.imageassociee_set.all()
    except:
        messages.error(request, "La video n'existe pas")
    
    context = {
        'actualiteImage':actualiteImage,
        'imageAssociees':imageAssociees
    }
    
    return render(request, 'web/actualite_image_details.html', context)

def actualite(request):
    return render(request,'web/act.html')

def galerie(request):
    return render(request,'web/GaleriePhoto.html')

