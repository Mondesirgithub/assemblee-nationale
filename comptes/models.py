from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Depute(AbstractUser):
    identifiant = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="Depute/photos/", null=True, blank=True, verbose_name="Photo du depute")
    
    class Meta:
        db_table = 'Depute'
        
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
        