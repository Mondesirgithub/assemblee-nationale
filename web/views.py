from django.shortcuts import render
from .models import Categorie
# Create your views here.

def index(request):
    categories = Categorie.objects.all()
    context = {
        'categories': categories
    }
    
    return render(request, 'web/index.html', context)
def actualite(request):
    return render(request,'web/act.html')

def galerie(request):
    return render(request,'web/GaleriePhoto.html')