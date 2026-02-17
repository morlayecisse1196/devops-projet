from django.db import models
from django.conf import settings


class NotificationUser(models.Model):
    """
    Modèle de liaison entre Notification et User.
    Permet de savoir si un utilisateur a lu une notification.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notification_users'
    )
    notification = models.ForeignKey(
        'gestion.Notification',
        on_delete=models.CASCADE,
        related_name='notification_users'
    )
    lue = models.BooleanField(default=False)

    class Meta:
        db_table = 'notification_users'
        verbose_name = 'Notification Utilisateur'
        verbose_name_plural = 'Notifications Utilisateurs'
        unique_together = ['user', 'notification']

    def __str__(self):
        status = "Lue" if self.lue else "Non lue"
        return f"{self.user.email} - {self.notification.titre} ({status})"
