from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django_resized import ResizedImageField
from .resources import profiles
# Create your models here.

class Depute(AbstractUser):
    identifiant = models.CharField(max_length=255)
    slug = slug = models.SlugField(max_length=400, unique=True, blank=True)
    photo = ResizedImageField(size=[50, 80], quality=100, upload_to="Deputes/photos/", default=None, null=True, blank=True) 
    num_post = models.IntegerField(blank=True, default=0)
    categorie = models.Choices(profiles.PROFILES, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.email}"
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name+self.last_name)
            
        super(Depute, self).save(*args, **kwargs)
        
        
class ImageAssociee(models.Model):
    source = models.ImageField(upload_to="Membres/images/", null=True, blank=True)
    membre = models.ForeignKey(Depute,on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"Image de {self.membre.first_name} {self.membre.last_name}"