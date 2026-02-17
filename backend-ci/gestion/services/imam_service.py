from django.db import transaction
from django.shortcuts import get_object_or_404
from gestion.models.imam import Imam


class ImamService:

    @staticmethod
    @transaction.atomic
    def create(data):
        """Créer un nouvel imam"""
        imam = Imam.objects.create(
            nom_complet=data['nom_complet'],
            biographie=data.get('biographie', ''),
            photo_url=data.get('photo_url', ''),
            periode=data.get('periode', '')
        )
        return imam

    @staticmethod
    def get_all():
        """Récupérer tous les imams"""
        return Imam.objects.all()

    @staticmethod
    def get_by_id(imam_id):
        """Récupérer un imam par son ID"""
        return get_object_or_404(Imam, id=imam_id)

    @staticmethod
    def update(imam, data):
        """Mettre à jour un imam"""
        for key, value in data.items():
            setattr(imam, key, value)
        imam.save()
        return imam

    @staticmethod
    def delete(imam):
        """Supprimer un imam"""
        imam.delete()
