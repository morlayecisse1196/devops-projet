from rest_framework import serializers
from gestion.models.evenement import Evenement
from gestion.serializers.lieu_serializer import LieuSerializer


class EvenementSerializer(serializers.ModelSerializer):
    """Serializer pour la lecture des événements (GET)"""
    type_display = serializers.CharField(source='get_type_display', read_only=True)
    lieu = LieuSerializer(read_only=True)
    
    class Meta:
        model = Evenement
        fields = [
            'id', 'titre', 'description', 'date_heure_debut', 'date_heure_fin',
            'nb_places_max', 'type', 'type_display', 'lieu', 'actif'
        ]


class SaveEvenementSerializer(serializers.Serializer):
    """Serializer pour la création d'un événement (POST)"""
    titre = serializers.CharField(max_length=200)
    description = serializers.CharField(max_length=3000, required=False, allow_blank=True)
    date_heure_debut = serializers.DateTimeField()
    date_heure_fin = serializers.DateTimeField()
    nb_places_max = serializers.IntegerField(default=0)
    type = serializers.ChoiceField(
        choices=['CONFERENCE', 'CHANT', 'CEREMONIE'],
        default='CEREMONIE'
    )
    lieu_id = serializers.IntegerField()


class UpdateEvenementSerializer(serializers.ModelSerializer):
    """Serializer pour la mise à jour d'un événement (PUT/PATCH)"""
    class Meta:
        model = Evenement
        fields = [
            'titre', 'description', 'date_heure_debut', 'date_heure_fin',
            'nb_places_max', 'type', 'actif'
        ]
