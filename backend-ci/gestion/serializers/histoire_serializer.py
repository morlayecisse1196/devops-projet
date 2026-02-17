from rest_framework import serializers
from gestion.models.histoire import Histoire


class HistoireSerializer(serializers.ModelSerializer):
    """Serializer pour la lecture des histoires (GET)"""
    
    class Meta:
        model = Histoire
        fields = ['id', 'titre', 'contenu', 'audio_url', 'image_url', 'ordre_affichage']


class SaveHistoireSerializer(serializers.Serializer):
    """Serializer pour la création d'une histoire (POST)"""
    titre = serializers.CharField(max_length=200)
    contenu = serializers.CharField(max_length=8000)
    audio_url = serializers.URLField(max_length=500, required=False, allow_blank=True)
    image_url = serializers.URLField(max_length=500, required=False, allow_blank=True)
    ordre_affichage = serializers.IntegerField(default=0)


class UpdateHistoireSerializer(serializers.ModelSerializer):
    """Serializer pour la mise à jour d'une histoire (PUT/PATCH)"""
    class Meta:
        model = Histoire
        fields = ['titre', 'contenu', 'audio_url', 'image_url', 'ordre_affichage']
