from django.db import models


class Histoire(models.Model):
    """
    Modèle représentant une histoire/récit du Magal.
    """
    titre = models.CharField(max_length=200)
    contenu = models.TextField(max_length=8000)
    audio_url = models.URLField(max_length=500, blank=True)
    image_url = models.URLField(max_length=500, blank=True)
    ordre_affichage = models.IntegerField(default=0)

    class Meta:
        db_table = 'histoires'
        verbose_name = 'Histoire'
        verbose_name_plural = 'Histoires'
        ordering = ['ordre_affichage']

    def __str__(self):
        return self.titre
