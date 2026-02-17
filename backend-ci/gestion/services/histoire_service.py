from django.db import transaction
from django.shortcuts import get_object_or_404
from gestion.models.histoire import Histoire


class HistoireService:

    @staticmethod
    @transaction.atomic
    def create(data):
        """Créer une nouvelle histoire"""
        histoire = Histoire.objects.create(
            titre=data['titre'],
            contenu=data['contenu'],
            audio_url=data.get('audio_url', ''),
            image_url=data.get('image_url', ''),
            ordre_affichage=data.get('ordre_affichage', 0)
        )
        return histoire

    @staticmethod
    def get_all():
        """Récupérer toutes les histoires (triées par ordre d'affichage)"""
        return Histoire.objects.all().order_by('ordre_affichage')

    @staticmethod
    def get_by_id(histoire_id):
        """Récupérer une histoire par son ID"""
        return get_object_or_404(Histoire, id=histoire_id)

    @staticmethod
    def update(histoire, data):
        """Mettre à jour une histoire"""
        for key, value in data.items():
            setattr(histoire, key, value)
        histoire.save()
        return histoire

    @staticmethod
    def delete(histoire):
        """Supprimer une histoire"""
        histoire.delete()
