from rest_framework import serializers
from gestion.models.imam import Imam


class ImamSerializer(serializers.ModelSerializer):
    """Serializer pour la lecture des imams (GET)"""
    
    class Meta:
        model = Imam
        fields = ['id', 'nom_complet', 'biographie', 'photo_url', 'periode']


class SaveImamSerializer(serializers.Serializer):
    """Serializer pour la création d'un imam (POST)"""
    nom_complet = serializers.CharField(max_length=200)
    biographie = serializers.CharField(max_length=5000, required=False, allow_blank=True)
    photo_url = serializers.URLField(max_length=500, required=False, allow_blank=True)
    periode = serializers.CharField(max_length=50, required=False, allow_blank=True)


class UpdateImamSerializer(serializers.ModelSerializer):
    """Serializer pour la mise à jour d'un imam (PUT/PATCH)"""
    class Meta:
        model = Imam
        fields = ['nom_complet', 'biographie', 'photo_url', 'periode']
