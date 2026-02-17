from django.db import models
from gestion.enums import TypeNotification


class Notification(models.Model):
    """
    Modèle représentant une notification.
    """
    titre = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)
    date_envoi = models.DateTimeField(auto_now_add=True)
    type = models.CharField(
        max_length=30,
        choices=TypeNotification.choices,
        default=TypeNotification.INFO
    )
    envoyee = models.BooleanField(default=False)

    class Meta:
        db_table = 'notifications'
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return f"{self.titre} ({self.get_type_display()})"
