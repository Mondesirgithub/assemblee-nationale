from django.db import models
from comptes.models import Depute


class CategorieSujet(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sujet(models.Model):
    contenu = models.CharField(max_length=200)
    categorie = models.ForeignKey(CategorieSujet, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Depute, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.contenu


class Post(models.Model):
    contenu = models.TextField()
    sujet = models.ForeignKey(Sujet, on_delete=models.CASCADE)
    parent_post = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_by = models.ForeignKey(Depute, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.pk} par {self.created_by.username}"
