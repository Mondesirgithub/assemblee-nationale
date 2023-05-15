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



def article_details(request, catId):
    context = {}
    try:
        article = Article.objects.get(pk=catId)
        categorie = Categorie.objects.get(pk=article.pk)
        articles = categorie.article_set.all()
        context = {
            'article': article,
            'articles': articles
        }
    except:
        messages.error(request, "L'article n'existe pas")

    return render(request, 'web/article_details.html', context)


def articles(request, pk):
    context = {'article':None}
    try:
        categorie = Categorie.objects.get(pk=pk)
        articles = categorie.articles_set.all()
        context = {
            'articles': articles,
            'categorie': categorie
        }
    except:
        messages.error(request, "La categorie n'existe pas")

    return render(request, 'web/articles.html', context)