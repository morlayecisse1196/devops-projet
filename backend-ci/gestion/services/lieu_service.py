from django.db import transaction
from django.shortcuts import get_object_or_404
from gestion.models.lieu import Lieu


class LieuService:

    @staticmethod
    @transaction.atomic
    def create(data):
        """Créer un nouveau lieu"""
        lieu = Lieu.objects.create(
            nom=data['nom'],
            categorie=data.get('categorie', 'AUTRE'),
            latitude=data['latitude'],
            longitude=data['longitude'],
            description=data.get('description', ''),
            adresse=data.get('adresse', '')
        )
        return lieu

    @staticmethod
    def get_all():
        """Récupérer tous les lieux actifs"""
        return Lieu.objects.filter(actif=True)

    @staticmethod
    def get_by_id(lieu_id):
        """Récupérer un lieu par son ID"""
        return get_object_or_404(Lieu, id=lieu_id)

    @staticmethod
    def get_by_categorie(categorie):
        """Récupérer les lieux par catégorie"""
        return Lieu.objects.filter(categorie=categorie, actif=True)

    @staticmethod
    def update(lieu, data):
        """Mettre à jour un lieu"""
        for key, value in data.items():
            setattr(lieu, key, value)
        lieu.save()
        return lieu

    @staticmethod
    def delete(lieu):
        """Supprimer un lieu (soft delete)"""
        lieu.actif = False
        lieu.save()
