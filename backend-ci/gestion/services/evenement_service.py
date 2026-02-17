from django.db import transaction
from django.shortcuts import get_object_or_404
from gestion.models.evenement import Evenement
from gestion.models.lieu import Lieu


class EvenementService:

    @staticmethod
    @transaction.atomic
    def create(data):
        """Créer un nouvel événement"""
        lieu = get_object_or_404(Lieu, id=data['lieu_id'])
        
        evenement = Evenement.objects.create(
            titre=data['titre'],
            description=data.get('description', ''),
            date_heure_debut=data['date_heure_debut'],
            date_heure_fin=data['date_heure_fin'],
            nb_places_max=data.get('nb_places_max', 0),
            type=data.get('type', 'CEREMONIE'),
            lieu=lieu
        )
        return evenement

    @staticmethod
    def get_all():
        """Récupérer tous les événements actifs"""
        return Evenement.objects.filter(actif=True).select_related('lieu')

    @staticmethod
    def get_by_id(evenement_id):
        """Récupérer un événement par son ID"""
        return get_object_or_404(Evenement.objects.select_related('lieu'), id=evenement_id)

    @staticmethod
    def get_by_type(type_evenement):
        """Récupérer les événements par type"""
        return Evenement.objects.filter(type=type_evenement, actif=True).select_related('lieu')

    @staticmethod
    def get_by_lieu(lieu_id):
        """Récupérer les événements par lieu"""
        return Evenement.objects.filter(lieu_id=lieu_id, actif=True).select_related('lieu')

    @staticmethod
    def update(evenement, data):
        """Mettre à jour un événement"""
        for key, value in data.items():
            setattr(evenement, key, value)
        evenement.save()
        return evenement

    @staticmethod
    def delete(evenement):
        """Supprimer un événement (soft delete)"""
        evenement.actif = False
        evenement.save()

    @staticmethod
    def get_places_disponibles(evenement):
        """Calculer le nombre de places disponibles"""
        nb_inscrits = evenement.inscriptions.filter(statut='INSCRIT').count()
        return evenement.nb_places_max - nb_inscrits
