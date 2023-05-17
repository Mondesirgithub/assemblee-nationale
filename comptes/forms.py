from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms



class InscriptionForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput({'class':'form-control'}), label="Mot de passe")
    password2 = forms.CharField(widget=forms.PasswordInput({'class':'form-control'}), label="Confirmez votre mot de passe")
    photo = forms.ImageField(widget=forms.FileInput({'class':'form-control'}), label="Photo", required=False)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['last_name', 'first_name', 'email', 'password1', 'password2', 'photo']
        labels = {
            'last_name': 'Nom(s)',
            'first_name': 'Prénom(s)',
            'email': 'Email'
        }
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }



class ConnexionForm(forms.Form):
	email = forms.CharField(required=True,widget=forms.TextInput({'class':'form-control'}), label="Email")
	password = forms.CharField(widget=forms.PasswordInput({'class':'form-control'}), label="Mot de passe")
 
 
class ValidationForm(forms.Form):
	identifiant = forms.CharField(widget=forms.TextInput({'class':'form-control'}), label="Identifiant")