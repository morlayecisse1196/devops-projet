from django.db import models
from gestion.enums import TypeEvenement


class Evenement(models.Model):
    """
    Modèle représentant un événement du Magal.
    """
    titre = models.CharField(max_length=200)
    description = models.TextField(max_length=3000, blank=True)
    date_heure_debut = models.DateTimeField()
    date_heure_fin = models.DateTimeField()
    nb_places_max = models.IntegerField(default=0)
    type = models.CharField(
        max_length=20,
        choices=TypeEvenement.choices,
        default=TypeEvenement.CEREMONIE
    )
    lieu = models.ForeignKey(
        'gestion.Lieu',
        on_delete=models.CASCADE,
        related_name='evenements'
    )
    actif = models.BooleanField(default=True)

    class Meta:
        db_table = 'evenements'
        verbose_name = 'Événement'
        verbose_name_plural = 'Événements'

    def __str__(self):
        return f"{self.titre} - {self.date_heure_debut.strftime('%d/%m/%Y %H:%M')}"
