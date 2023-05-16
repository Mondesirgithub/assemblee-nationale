from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,authenticate,logout
from .forms import InscriptionForm, ConnexionForm
from django.contrib import messages
# Create your views here.

def registerDepute(request):
    pass
    # form = InscriptionForm()
    # if request.method == "POST":
    #     form = InscriptionForm(request.POST, request.FILES)

    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         messages.success(request, "Le compte a été crée avec succès !!")

    #         return redirect('index')

    # context = {
    #     'form':form
    # }

    # return render(request, 'comptes/inscription.html', context)


def loginDepute(request):
    pass