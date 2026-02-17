from django.db import models


class Imam(models.Model):
    """
    Modèle représentant un Imam / Guide spirituel.
    """
    nom_complet = models.CharField(max_length=200)
    biographie = models.TextField(max_length=5000, blank=True)
    photo_url = models.URLField(max_length=500, blank=True)
    periode = models.CharField(max_length=50, blank=True)  # ex: "1927-2007"

    class Meta:
        db_table = 'imams'
        verbose_name = 'Imam'
        verbose_name_plural = 'Imams'

    def __str__(self):
        return f"{self.nom_complet} ({self.periode})"
