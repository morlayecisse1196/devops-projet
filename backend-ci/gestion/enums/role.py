from django.db import models


class Role(models.TextChoices):
    PELERIN = 'PELERIN', 'Pèlerin'
    ADMIN = 'ADMIN', 'Administrateur'
