from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate
from .forms import InscriptionForm, ConnexionForm, ValidationForm
from django.contrib import messages
import hashlib
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Depute
from django.conf import settings 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as lt
from django.http import HttpResponse
from .models import Depute
# Create your views here.

def registerDepute(request):
    form = InscriptionForm()
    if request.method == "POST":
        form = InscriptionForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.email
            user.save()
            messages.success(request, "Le compte a été crée avec succès !!")
            return redirect('web:index')

    context = {
        'form':form
    }
    

    return render(request, 'comptes/registerDepute.html', context)


def loginDepute(request):
    form = ConnexionForm()
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user:
                subject = "Permission d'integrer le forum"
                template = 'comptes/email_validation.html'
                token = user.email+user.first_name+user.last_name
                token = hashlib.sha512((token).encode('utf-8')).hexdigest()[:10]
                user.identifiant = token
                user.save()
                login(request, user)
                context = {'user': user}
                html_message = render_to_string(template, context)
                plain_message = strip_tags(html_message)  # Version texte brut du message
                recipient_list = [user.email]
                send_mail(subject, plain_message, settings.EMAIL_HOST_USER, recipient_list, html_message=html_message)

                messages.info(request, "Veuillez entrer le code que vous avez reçu via mail !!")
                
                return redirect('validation')
            else:
                messages.error(request, "Username ou email incorrect !")

    context = {
        'form':form
    }

    return render(request, 'comptes/loginDepute.html', context)


@login_required
def validation(request):
    form = ValidationForm()
    if request.method == "POST":
        form = ValidationForm(request.POST)
        if form.is_valid():
            try:
                user = Depute.objects.get(identifiant=form.cleaned_data['identifiant'])
                login(request, user)
                messages.success(request, "Connexion reussie , Bienvenue sur le forum")
                return redirect('forums:home')
            except:
                messages.error(request, "L'identifiant est incorrect !")

    context = {
        'form':form
    }
    
    return render(request, 'comptes/validation.html', context)


@login_required
def logout(request):
    user = request.user
    user.identifiant = ""
    user.save()
    lt(request)
    messages.info(request, "Vous avez été déconnecté")
    return redirect("web:index")




def check_input_connexion(request, nom):
    form = ConnexionForm(request.POST)
    erreurs = form[nom].errors 
    erreurs = f"<span color='red'>{erreurs}</span>"
    if not form.is_valid():
        erreurs += "<script>$(function(){$('#submit').attr('disabled','true');});</script>"
    else:
        erreurs += "<script>$(function(){$('#submit').removeAttr('disabled');});</script>"
    return HttpResponse(erreurs)


def check_input_validation(request, nom):
    form = ValidationForm(request.POST)
    erreurs = form[nom].errors 

    erreurs = f"<span color='red'>{erreurs}</span>"
    if not form.is_valid():
        erreurs += "<script>$(function(){$('#submit').attr('disabled','true');});</script>"
    else:
        erreurs += "<script>$(function(){$('#submit').removeAttr('disabled');});</script>"
    return HttpResponse(erreurs)

def Affichage(request,id_Depute):
    personne=Depute.objects.get(id=id_Depute)
    kate=personne.kate
    Depute_on_rel =Depute.objects.filter(kate=kate)
    return render(request,"web/GaleriePhoto.html",
                  {"article":personne,
                  "aer":Depute_on_rel})
    