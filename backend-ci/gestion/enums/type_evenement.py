from django.db import models


class TypeEvenement(models.TextChoices):
    CONFERENCE = 'CONFERENCE', 'Conférence'
    CHANT = 'CHANT', 'Chant'
    CEREMONIE = 'CEREMONIE', 'Cérémonie'
