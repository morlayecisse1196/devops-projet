from django.db import models
from gestion.enums import CategorieLieu


class Lieu(models.Model):
    """
    Modèle représentant un lieu du Magal.
    """
    nom = models.CharField(max_length=200)
    categorie = models.CharField(
        max_length=20,
        choices=CategorieLieu.choices,
        default=CategorieLieu.AUTRE
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(max_length=2000, blank=True)
    adresse = models.CharField(max_length=500, blank=True)
    actif = models.BooleanField(default=True)

    class Meta:
        db_table = 'lieux'
        verbose_name = 'Lieu'
        verbose_name_plural = 'Lieux'

    def __str__(self):
        return f"{self.nom} ({self.get_categorie_display()})"
