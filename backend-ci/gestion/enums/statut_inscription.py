from django.db import models


class StatutInscription(models.TextChoices):
    INSCRIT = 'INSCRIT', 'Inscrit'
    ANNULE = 'ANNULE', 'Annulé'
    PRESENT = 'PRESENT', 'Présent'
