from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django_resized import ResizedImageField
# Create your models here.



class Depute(AbstractUser):
    identifiant = models.CharField(max_length=255)
    slug = slug = models.SlugField(max_length=400, unique=True, blank=True)
    #photo = models.ImageField(upload_to="Depute/photos/", null=True, blank=True, verbose_name="Photo de l'Depute")
    photo = ResizedImageField(size=[50, 80], quality=100, upload_to="Deputes/photos/", default=None, null=True, blank=True) 
    num_post = models.IntegerField(blank=True, default=0)
    
    def __str__(self) -> str:
        return f"{self.email}"
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.first_name+self.last_name)
            
        super(Depute, self).save(*args, **kwargs)