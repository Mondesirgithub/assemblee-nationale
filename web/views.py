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
        'image2':image2,
    }
    
    return render(request, 'web/index.html', context)



def article_details(request, id):
    context = {}
    try:
        article = Article.objects.get(pk=id)
        categorie = Categorie.objects.get(pk=article.categorie.pk)
        articles = categorie.article_set.all()
        context = {
            'article': article,
            'articles': articles
        }
    except:
        messages.error(request, "L'article n'existe pas")

    return render(request, 'web/article_details.html', context)


def articles(request, pk):
    context = {}
    try:
        categorie = Categorie.objects.get(pk=pk)
        articles = categorie.article_set.all()
        context = {
            'articles': articles,
            'categorie': categorie
        }
    except:
        messages.error(request, "La categorie n'existe pas")

    return render(request, 'web/articles.html', context)