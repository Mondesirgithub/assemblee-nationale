from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .resources import profiles
import re



class InscriptionForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput({'class':'form-control'}), label="Mot de passe")
    password2 = forms.CharField(widget=forms.PasswordInput({'class':'form-control'}), label="Confirmez votre mot de passe")
    photo = forms.ImageField(widget=forms.FileInput({'class':'form-control'}), label="Photo", required=False)

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['last_name', 'first_name', 'email','categorie','password1', 'password2', 'photo']
        labels = {
            'last_name': 'Nom(s)',
            'first_name': 'Prénom(s)',
            'email': 'Email',
            'categorie': 'Catégorie du membre'
        }
        widgets = {
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'categorie': forms.Select(attrs={'class': 'form-control'})
        }



class ConnexionForm(forms.Form):
	email = forms.CharField(required=True,widget=forms.EmailInput({'class':'form-control'}), label="Email")
	password = forms.CharField(widget=forms.PasswordInput({'class':'form-control'}), label="Mot de passe")
 
 
	def __init__(self, *args, **kwargs):
		super(ConnexionForm, self).__init__(*args, **kwargs)

		for name, field in self.fields.items():
				field.widget.attrs.update({
					'hx-post' : f"/comptes/check_input_connexion/{name}",
					'hx-trigger': "keyup",
					'hx-target':f'#{name}_errors'
					})
	
	def clean_email(self):
		return self.champObligatoire(self.cleaned_data['email'])

	def clean_email(self):
		email = self.cleaned_data['email']
		if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
			raise forms.ValidationError("Adresse e-mail invalide")
		if email == '':
			raise forms.ValidationError("L'email est obligatoire")
		
		return email
 

	def clean_password(self):
		password = self.cleaned_data['password']
		if len(password) < 8:
			raise forms.ValidationError("Le mot de passe doit avoir au moins 8 caractères")
		if password == '':
			raise forms.ValidationError("Le mot de passe est obligatoire")
		
		return password
 
class ValidationForm(forms.Form):
	identifiant = forms.CharField(widget=forms.TextInput({'class':'form-control'}), label="Identifiant")
 
 
	def __init__(self, *args, **kwargs):
		super(ValidationForm, self).__init__(*args, **kwargs)

		for name, field in self.fields.items():
				field.widget.attrs.update({
					'hx-post' : f"/comptes/check_input_validation/{name}",
     				'hx-trigger': "keyup",
					'hx-target':f'#{name}_errors'
					})