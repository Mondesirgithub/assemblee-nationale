import hashlib
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Depute
from django.core.mail import EmailMessage
from django.conf import settings 
from django.template.loader import render_to_string
from django.contrib.auth.signals import user_logged_in


@receiver(user_logged_in)
def seConnecter(sender, request, user, **kwargs):
    subject = "Permission d'intégrer le forum"
    token = user.email+user.first_name+user.last_name
    token = hashlib.sha512((token).encode('utf-8')).hexdigest()[:10]
    user.identifiant = token
    user.save()
    context = {
        'user': user
    }
    template = render_to_string("comptes/email_validation.html" , context)
    email = EmailMessage(
        subject,
        template,
        settings.EMAIL_HOST_USER,
        [user.email]
    )
    email.fail_silently = False
    email.send()
    

