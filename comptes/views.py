from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,authenticate
from .forms import InscriptionForm, ConnexionForm, ValidationForm
from django.contrib import messages
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
                login(request, user)
                # login(request, user)
                messages.info(request, "Veuillez entrer le code que vous avez reçu via mail !!")
                return redirect('comptes:validation')
            else:
                messages.error(request, "Username ou email incorrect !")

    context = {
        'form':form
    }

    return render(request, 'comptes/loginDepute.html', context)


def validation(request):
    form = ValidationForm()
    if request.method == "POST":
        form = ValidationForm(request.POST)
        if form.is_valid():
            try:
                user = Depute.objects.get(identifiant=form.cleaned_data['identifiant'])
                login(request, user)
                messages.info(request, "Bienvenue sur le forum")
                return redirect('forums:index')
            except:
                messages.error(request, "L'identifiant est incorrect !")
                print("L'identifiant est incorrect !")

    context = {
        'form':form
    }
    
    return render(request, 'comptes/validation.html', context)