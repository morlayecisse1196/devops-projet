from rest_framework import serializers
from gestion.models.notification_user import NotificationUser
from gestion.serializers.user_serializer import UserSerializer
from gestion.serializers.notification_serializer import NotificationSerializer


class NotificationUserSerializer(serializers.ModelSerializer):
    """Serializer pour la lecture des notifications utilisateur (GET)"""
    user = UserSerializer(read_only=True)
    notification = NotificationSerializer(read_only=True)
    
    class Meta:
        model = NotificationUser
        fields = ['id', 'user', 'notification', 'lue']


class SaveNotificationUserSerializer(serializers.Serializer):
    """Serializer pour la création d'une notification utilisateur (POST)"""
    user_id = serializers.IntegerField()
    notification_id = serializers.IntegerField()
    lue = serializers.BooleanField(default=False)


class UpdateNotificationUserSerializer(serializers.ModelSerializer):
    """Serializer pour la mise à jour d'une notification utilisateur (PUT/PATCH)"""
    class Meta:
        model = NotificationUser
        fields = ['lue']
