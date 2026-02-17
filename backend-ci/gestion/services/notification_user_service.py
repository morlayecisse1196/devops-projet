from django.db import transaction
from django.shortcuts import get_object_or_404
from gestion.models.notification_user import NotificationUser
from gestion.models.user import User
from gestion.models.notification import Notification


class NotificationUserService:

    @staticmethod
    @transaction.atomic
    def create(data):
        """Créer une nouvelle notification utilisateur"""
        user = get_object_or_404(User, id=data['user_id'])
        notification = get_object_or_404(Notification, id=data['notification_id'])
        
        notification_user = NotificationUser.objects.create(
            user=user,
            notification=notification,
            lue=data.get('lue', False)
        )
        return notification_user

    @staticmethod
    def get_all():
        """Récupérer toutes les notifications utilisateur"""
        return NotificationUser.objects.select_related('user', 'notification').all()

    @staticmethod
    def get_by_id(notification_user_id):
        """Récupérer une notification utilisateur par son ID"""
        return get_object_or_404(
            NotificationUser.objects.select_related('user', 'notification'),
            id=notification_user_id
        )

    @staticmethod
    def get_by_user(user_id):
        """Récupérer les notifications d'un utilisateur"""
        return NotificationUser.objects.filter(user_id=user_id).select_related('notification').order_by('-notification__date_envoi')

    @staticmethod
    def get_non_lues_by_user(user_id):
        """Récupérer les notifications non lues d'un utilisateur"""
        return NotificationUser.objects.filter(user_id=user_id, lue=False).select_related('notification').order_by('-notification__date_envoi')

    @staticmethod
    def update(notification_user, data):
        """Mettre à jour une notification utilisateur"""
        for key, value in data.items():
            setattr(notification_user, key, value)
        notification_user.save()
        return notification_user

    @staticmethod
    def delete(notification_user):
        """Supprimer une notification utilisateur"""
        notification_user.delete()

    @staticmethod
    def marquer_comme_lue(notification_user):
        """Marquer une notification comme lue"""
        notification_user.lue = True
        notification_user.save()
        return notification_user

    @staticmethod
    @transaction.atomic
    def marquer_toutes_lues(user_id):
        """Marquer toutes les notifications d'un utilisateur comme lues"""
        NotificationUser.objects.filter(user_id=user_id, lue=False).update(lue=True)
