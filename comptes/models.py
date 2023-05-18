from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django_resized import ResizedImageField
from .resources import profiles
from tinymce.models import HTMLField
# Create your models here.

class Depute(AbstractUser):
    identifiant = models.CharField(max_length=255)
    slug = slug = models.SlugField(max_length=400, unique=True, blank=True)
    photo = ResizedImageField(size=[60, 80], quality=100, upload_to="Deputes/photos/", default=None, null=True, blank=True) 
    num_post = models.IntegerField(blank=True, default=0)
    enFonction = models.BooleanField(default=True, blank=True, null=True)
    precedentLegislature = models.BooleanField(default=False, blank=True, null=True)
    categorie = models.CharField(choices=profiles.PROFILES, max_length=100, null=True, blank=True)
    
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
    
    

class ArticlePresident(models.Model):
    user = models.ForeignKey(Depute, blank=True, null=True, on_delete=models.CASCADE)
    titre = models.CharField(max_length=255, blank=True, null=True)
    description = HTMLField()
    image = models.ImageField(upload_to="President/articles/images/", null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.titre} du president {self.user.first_name} {self.user.last_name}"
