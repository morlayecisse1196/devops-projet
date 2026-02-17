from rest_framework import serializers
from gestion.models.inscription import Inscription
from gestion.serializers.user_serializer import UserSerializer
from gestion.serializers.evenement_serializer import EvenementSerializer


class InscriptionSerializer(serializers.ModelSerializer):
    """Serializer pour la lecture des inscriptions (GET)"""
    statut_display = serializers.CharField(source='get_statut_display', read_only=True)
    user = UserSerializer(read_only=True)
    evenement = EvenementSerializer(read_only=True)
    
    class Meta:
        model = Inscription
        fields = [
            'id', 'user', 'evenement', 'date_inscription',
            'statut', 'statut_display'
        ]


class SaveInscriptionSerializer(serializers.Serializer):
    """Serializer pour la création d'une inscription (POST)"""
    user_id = serializers.IntegerField()
    evenement_id = serializers.IntegerField()
    statut = serializers.ChoiceField(
        choices=['INSCRIT', 'ANNULE', 'PRESENT'],
        default='INSCRIT'
    )


class UpdateInscriptionSerializer(serializers.ModelSerializer):
    """Serializer pour la mise à jour d'une inscription (PUT/PATCH)"""
    class Meta:
        model = Inscription
        fields = ['statut']
