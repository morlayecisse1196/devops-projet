from rest_framework import serializers
from gestion.models.notification import Notification


class NotificationSerializer(serializers.ModelSerializer):
    """Serializer pour la lecture des notifications (GET)"""
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    
    class Meta:
        model = Notification
        fields = ['id', 'titre', 'message', 'date_envoi', 'type', 'type_display', 'envoyee']


class SaveNotificationSerializer(serializers.Serializer):
    """Serializer pour la création d'une notification (POST)"""
    titre = serializers.CharField(max_length=200)
    message = serializers.CharField(max_length=2000)
    type = serializers.ChoiceField(
        choices=['INFO', 'ALERTE_SECURITE', 'RAPPEL_EVENEMENT'],
        default='INFO'
    )


class UpdateNotificationSerializer(serializers.ModelSerializer):
    """Serializer pour la mise à jour d'une notification (PUT/PATCH)"""
    class Meta:
        model = Notification
        fields = ['titre', 'message', 'type', 'envoyee']
