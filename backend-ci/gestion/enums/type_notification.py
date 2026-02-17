from django.db import models


class TypeNotification(models.TextChoices):
    INFO = 'INFO', 'Information'
    ALERTE_SECURITE = 'ALERTE_SECURITE', 'Alerte Sécurité'
    RAPPEL_EVENEMENT = 'RAPPEL_EVENEMENT', 'Rappel Événement'
