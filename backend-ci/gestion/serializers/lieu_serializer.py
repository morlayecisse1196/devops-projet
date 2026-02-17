from rest_framework import serializers
from gestion.models.lieu import Lieu


class LieuSerializer(serializers.ModelSerializer):
    """Serializer pour la lecture des lieux (GET)"""
    categorie_display = serializers.CharField(source='get_categorie_display', read_only=True)
    
    class Meta:
        model = Lieu
        fields = [
            'id', 'nom', 'categorie', 'categorie_display',
            'latitude', 'longitude', 'description', 'adresse', 'actif'
        ]


class SaveLieuSerializer(serializers.Serializer):
    """Serializer pour la création d'un lieu (POST)"""
    nom = serializers.CharField(max_length=200)
    categorie = serializers.ChoiceField(
        choices=['GRANDE_MOSQUEE', 'RESIDENCE', 'DAARA', 'AUTRE'],
        default='AUTRE'
    )
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    description = serializers.CharField(max_length=2000, required=False, allow_blank=True)
    adresse = serializers.CharField(max_length=500, required=False, allow_blank=True)


class UpdateLieuSerializer(serializers.ModelSerializer):
    """Serializer pour la mise à jour d'un lieu (PUT/PATCH)"""
    class Meta:
        model = Lieu
        fields = ['nom', 'categorie', 'latitude', 'longitude', 'description', 'adresse', 'actif']
