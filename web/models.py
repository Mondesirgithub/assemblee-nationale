from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=255, blank=False, verbose_name="Nom de la categorie",null=False)
    icone = models.FileField(upload_to="commissions/icones/", blank=True, null=True, verbose_name="Icone de la categorie")

    def __str__(self) -> str:
        return f"{self.nom}"


class Article(models.Model):
    titre = models.CharField(max_length=50, verbose_name="Titre de l'article", blank=False, null=False) 
    description = HTMLField()
    categorie = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING, null=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.titre} - {self.categorie.nom}"
    

class Actualite(models.Model):
    titre = models.CharField(max_length=255, blank=False, verbose_name="Titre de l'actualite")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.titre}"
    
class ActualiteVideo(Actualite):
    lien = models.FileField(upload_to="Actualites/videos/", verbose_name="Fichier de la video", null=True)
    
    def __str__(self) -> str:
        return f"{super().titre}"
    
    
class ActualiteImage(Actualite):
    description = HTMLField()
    
    def __str__(self) -> str:
        return f"{super().titre}"
    
class ImageAssociee(models.Model):
    source = models.ImageField(upload_to="actualites/images/", null=True, blank=True)
    actualiteImage = models.ForeignKey(ActualiteImage, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"image de {self.actualiteImage.titre}"


class Annonce(models.Model):
    titre = models.CharField(max_length=255)
    description = HTMLField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="Annonces/images/", null=True)
    
    def __str__(self) -> str:
        return f"{self.titre}"
    
class SymbolesAssemblee(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="SymbolesAssemblee/images/", null=True)
    description = HTMLField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.nom}"
    
    
class LoiAdoptee(models.Model):
    nom = models.CharField(max_length=255)
    fichier = models.FileField(upload_to="LoisAdoptees/pdf/", null=True)
    date = models.DateTimeField()
    typeLoi = models.CharField(max_length=30, default="", null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nom}"


class EvenementHemicycle(models.Model):
    nom = models.CharField(max_length=255)
    content = HTMLField()
    image = models.ImageField(upload_to="EvenemenetsHemicycle/images/")
    date = models.DateField()
    heureDebut = models.TimeField()
    heureFin = models.TimeField()
    lieu = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.nom}"
    

class TravauxCommission(models.Model):
    titre = models.CharField(max_length=255)
    commission = models.ForeignKey(Categorie,on_delete=models.CASCADE, null=True)
    decription = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to="TravauxEnCommission/images/", null=True, blank=True, default=None)
    
    def __str__(self) -> str:
        return f"{self.titre} pour la {self.commission.nom}"
    
    
    
class Picture(models.Model):
    source = models.ImageField(upload_to="Galerie/photos/", null=True, blank=True)
    