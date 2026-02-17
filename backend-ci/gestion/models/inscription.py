from django.db import models
from django.conf import settings
from gestion.enums import StatutInscription


class Inscription(models.Model):
    """
    Modèle représentant l'inscription d'un utilisateur à un événement.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='inscriptions'
    )
    evenement = models.ForeignKey(
        'gestion.Evenement',
        on_delete=models.CASCADE,
        related_name='inscriptions'
    )
    date_inscription = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(
        max_length=20,
        choices=StatutInscription.choices,
        default=StatutInscription.INSCRIT
    )

    class Meta:
        db_table = 'inscriptions'
        verbose_name = 'Inscription'
        verbose_name_plural = 'Inscriptions'
        unique_together = ['user', 'evenement']  # Un user ne peut s'inscrire qu'une fois à un événement

    def __str__(self):
        return f"{self.user.email} - {self.evenement.titre}"
