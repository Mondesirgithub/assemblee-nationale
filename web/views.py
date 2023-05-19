from django.shortcuts import render
from .models import Categorie, Article, ActualiteImage, ActualiteVideo
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import EvenementHemicycle
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime
from comptes.models import Depute
from .models import Annonce
# Create your views here.

def index(request):
    categories = Categorie.objects.all()
    try:
        actualiteVideo = ActualiteVideo.objects.order_by("-created_at").first()
        actualiteImage1 = ActualiteImage.objects.order_by("-created_at").first()
        actualiteImage2 = ActualiteImage.objects.order_by("-created_at").all()[1]
        image1 , image2 = actualiteImage1.imageassociee_set.all()[0], actualiteImage2.imageassociee_set.all()[0]
    except:
        actualiteVideo,actualiteImage1,actualiteImage2,image1,image2 = None
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
    actualitesVideos = ActualiteVideo.objects.all()
    actualitesImages = ActualiteImage.objects.all()
    context = {
        'actualitesVideos':actualitesVideos,
        'actualitesImages':actualitesImages
        }
    return render(request,'web/act.html', context)

def galerie(request):
    membres = Depute.objects.all()
    context = {'membres':membres}
    return render(request,'web/GaleriePhoto.html', context)

def President(request):
    try:
        president = Depute.objects.get(categorie="PRESIDENT")
    except:
        president = None
        
    context = {'president':president}        
    return render(request,'web/President.html', context)

def Membre(request):
    membres = Depute.objects.all()
    context = {'membres':membres}
    return render(request,'web/Membre_du_bureau.html', context)

def contact1(request):
    return render(request,'web/contact1.html')

def contact2(request):
    return render(request,'web/contact2.html')

def calendrierS(request):
    return render(request,'web/Calendrier_des_session.html')

def Liste_des_Lois(request):
    lois = EvenementHemicycle.objects.all()
    context = {'lois':lois}
    return render(request,'web/Liste_des_lois_adopter.html', context)

def Evenement_H(request):
    events = EvenementHemicycle.objects.all()
    paginator = Paginator(events, per_page=6)
    page = request.GET.get("page")
    evenements = None
    try:
        evenements = paginator.get_page(page)
    except PageNotAnInteger:
        evenements = paginator.get_page(1)
    except EmptyPage:
        evenements = paginator.get_page(paginator.num_pages) 
        
    context = {'evenements':evenements, 'events':events}
    
    
    return render(request,'web/Evenement_a_lhemicycle.html', context)

def Travaux_en(request):
    return render(request,'web/Travaux_en_commission.html')

def Liste_des_depute_Fon(request):
    deputes = Depute.objects.filter(categorie="DEPUTE", enFonction=True)
    context = {"depute":deputes}
    return render(request,'web/Liste_des_depute.html', context)

def Ancien_President(request):
    deputes = Depute.objects.filter(categorie="ANCIEN PRESIDENT")
    context = {'depute':deputes}
    return render(request,'web/Ancien_President.html', context)

def Liste_des_depute_P(request):
    return render(request,'web/Liste_des_depute_desP.html')



@login_required(login_url="loginForAnnonce")
def annonce(request):
    annonces = Annonce.objects.all()
    context = {
        'annonces':annonces
    }
    return render(request,'web/annonce.html', context)


def Actualite(request):
    return render(request,'web/articles.html')


def Galerie_p(request):
    return render(request,'web/GaleriePhoto.html')

def Symbole(request):
    return render(request,'web/Symbole.html')
def Vac(request):
    return render(request,'web/VacancesP.html')

def membredetail(request):
    return render(request,'web/membreDetail.html')


def searchEvenements(request):
    context = {}
    evenements = EvenementHemicycle.objects.all()
    if request.method == "POST":
        if request.POST['dateDebut'] != "" and request.POST['dateFin'] != "":
            if request.POST['dateDebut'] < request.POST['dateFin']:
                debut = datetime.strptime(request.POST['dateDebut'], '%Y-%m-%d')
                fin = datetime.strptime(request.POST['dateFin'], '%Y-%m-%d')
                evenements = EvenementHemicycle.objects.filter(date__gte=debut, date__lte=fin)
                debut = debut.strftime("%d-%m-%Y")
                fin = fin.strftime("%d-%m-%Y")
                if len(evenements) == 0:
                    messages.info(request, f"Pas d'évènements qui se sont passé entre le {debut} et le {fin}")
                else:
                    messages.info(request, f"{len(evenements)} évènement(s) correspondant(s) à votre recherche")
            else:
                messages.error(request, "La date de fin doit être supérieure à la date de début")
        else:
            messages.error(request, "Les champs de recherche ne doivent pas être vides")
    context['events'] = evenements   
    return render(request, "web/Evenement_a_lhemicycle.html", context)

def evenement_detail(request):
    return render(request,'web/evenementDetail.html')

def histoire(request):
    return render(request,'web/histoire.html')




   

