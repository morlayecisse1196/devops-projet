from django.db import transaction
from django.shortcuts import get_object_or_404
from gestion.models.notification import Notification
from gestion.models.notification_user import NotificationUser
from gestion.models.user import User


class NotificationService:

    @staticmethod
    @transaction.atomic
    def create(data):
        """Créer une nouvelle notification"""
        notification = Notification.objects.create(
            titre=data['titre'],
            message=data['message'],
            type=data.get('type', 'INFO')
        )
        return notification

    @staticmethod
    def get_all():
        """Récupérer toutes les notifications"""
        return Notification.objects.all().order_by('-date_envoi')

    @staticmethod
    def get_by_id(notification_id):
        """Récupérer une notification par son ID"""
        return get_object_or_404(Notification, id=notification_id)

    @staticmethod
    def get_by_type(type_notification):
        """Récupérer les notifications par type"""
        return Notification.objects.filter(type=type_notification).order_by('-date_envoi')

    @staticmethod
    def update(notification, data):
        """Mettre à jour une notification"""
        for key, value in data.items():
            setattr(notification, key, value)
        notification.save()
        return notification

    @staticmethod
    def delete(notification):
        """Supprimer une notification"""
        notification.delete()

    @staticmethod
    @transaction.atomic
    def envoyer_a_tous(notification):
        """Envoyer une notification à tous les utilisateurs"""
        users = User.objects.filter(actif=True)
        notification_users = [
            NotificationUser(user=user, notification=notification)
            for user in users
        ]
        NotificationUser.objects.bulk_create(notification_users)
        notification.envoyee = True
        notification.save()
        return notification

    @staticmethod
    @transaction.atomic
    def envoyer_a_user(notification, user_id):
        """Envoyer une notification à un utilisateur spécifique"""
        user = get_object_or_404(User, id=user_id)
        NotificationUser.objects.create(user=user, notification=notification)
        return notification
