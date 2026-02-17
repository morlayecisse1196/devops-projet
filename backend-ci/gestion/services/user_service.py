from django.db import transaction
from django.shortcuts import get_object_or_404
from gestion.models.user import User
from gestion.enums import Role


class UserService:

    @staticmethod
    @transaction.atomic
    def create(data):
        """Créer un nouvel utilisateur"""
        user = User.objects.create_user(
            username=data['email'],
            email=data['email'],
            password=data['password'],
            prenom=data['prenom'],
            nom=data['nom'],
            telephone=data.get('telephone', ''),
            role=data.get('role', Role.PELERIN)
        )
        return user

    @staticmethod
    def get_all():
        """Récupérer tous les utilisateurs"""
        return User.objects.all()

    @staticmethod
    def get_by_id(user_id):
        """Récupérer un utilisateur par son ID"""
        return get_object_or_404(User, id=user_id)

    @staticmethod
    def get_by_email(email):
        """Récupérer un utilisateur par son email"""
        return get_object_or_404(User, email=email)

    @staticmethod
    def update(user, data):
        """Mettre à jour un utilisateur"""
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return user

    @staticmethod
    def delete(user):
        """Supprimer un utilisateur"""
        user.delete()

    @staticmethod
    def get_pelerins():
        """Récupérer tous les pèlerins"""
        return User.objects.filter(role=Role.PELERIN)

    @staticmethod
    def get_admins():
        """Récupérer tous les admins"""
        return User.objects.filter(role=Role.ADMIN)
