from django.db import transaction
from django.shortcuts import get_object_or_404
from gestion.models.inscription import Inscription
from gestion.models.user import User
from gestion.models.evenement import Evenement
from gestion.enums import StatutInscription


class InscriptionService:

    @staticmethod
    @transaction.atomic
    def create(data):
        """Créer une nouvelle inscription"""
        user = get_object_or_404(User, id=data['user_id'])
        evenement = get_object_or_404(Evenement, id=data['evenement_id'])
        
        # Vérifier si l'inscription existe déjà
        if Inscription.objects.filter(user=user, evenement=evenement).exists():
            raise ValueError("L'utilisateur est déjà inscrit à cet événement")
        
        inscription = Inscription.objects.create(
            user=user,
            evenement=evenement,
            statut=data.get('statut', StatutInscription.INSCRIT)
        )
        return inscription

    @staticmethod
    def get_all():
        """Récupérer toutes les inscriptions"""
        return Inscription.objects.select_related('user', 'evenement', 'evenement__lieu').all()

    @staticmethod
    def get_by_id(inscription_id):
        """Récupérer une inscription par son ID"""
        return get_object_or_404(
            Inscription.objects.select_related('user', 'evenement', 'evenement__lieu'),
            id=inscription_id
        )

    @staticmethod
    def get_by_user(user_id):
        """Récupérer les inscriptions d'un utilisateur"""
        return Inscription.objects.filter(user_id=user_id).select_related('evenement', 'evenement__lieu')

    @staticmethod
    def get_by_evenement(evenement_id):
        """Récupérer les inscriptions à un événement"""
        return Inscription.objects.filter(evenement_id=evenement_id).select_related('user')

    @staticmethod
    def update(inscription, data):
        """Mettre à jour une inscription"""
        for key, value in data.items():
            setattr(inscription, key, value)
        inscription.save()
        return inscription

    @staticmethod
    def delete(inscription):
        """Supprimer une inscription"""
        inscription.delete()

    @staticmethod
    def annuler(inscription):
        """Annuler une inscription"""
        inscription.statut = StatutInscription.ANNULE
        inscription.save()
        return inscription

    @staticmethod
    def marquer_present(inscription):
        """Marquer un participant comme présent"""
        inscription.statut = StatutInscription.PRESENT
        inscription.save()
        return inscription
