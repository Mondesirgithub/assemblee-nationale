from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Depute(AbstractUser):
    identifiant = models.CharField(max_length=255)