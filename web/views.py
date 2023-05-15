from django.shortcuts import render
from .models import Categorie, Article
from django.contrib import messages
# Create your views here.

def index(request):
    categories = Categorie.objects.all()
    context = {
        'categories': categories
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