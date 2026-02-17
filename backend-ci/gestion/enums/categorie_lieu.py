from django.db import models


class CategorieLieu(models.TextChoices):
    GRANDE_MOSQUEE = 'GRANDE_MOSQUEE', 'Grande Mosquée'
    RESIDENCE = 'RESIDENCE', 'Résidence'
    DAARA = 'DAARA', 'Daara'
    AUTRE = 'AUTRE', 'Autre'
