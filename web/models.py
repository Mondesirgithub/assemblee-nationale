from django.db import models

# Create your models here.
class Categorie(models.Model):
    nom = models.CharField(max_length=255, blank=False, verbose_name="Nom de la categorie",null=False)
    icone = models.FileField(upload_to="commissions/icones/", blank=True, null=True, verbose_name="Icone de la categorie")

    def __str__(self) -> str:
        return f"{self.nom}"


class Article(models.Model):
    titre = models.CharField(max_length=50, verbose_name="Titre de l'article", blank=False, null=False) 
    description = models.TextField(verbose_name="Description de l'article", blank=False, null=False)
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
    lien = models.CharField(max_length=255, blank=False, verbose_name="Lien de la video", null=False)
    
    def __str__(self) -> str:
        return f"{super().titre}"
    
    
class ActualiteImage(Actualite):
    description = models.TextField(verbose_name="Description de l'actualite", blank=False, null=False)
    
    def __str__(self) -> str:
        return f"{super().titre}"
    
class ImageAssociee(models.Model):
    source = models.ImageField(upload_to="actualites/images/", null=True, blank=True)
    actualiteImage = models.ForeignKey(ActualiteImage, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"image de {self.actualiteImage.titre}"
    