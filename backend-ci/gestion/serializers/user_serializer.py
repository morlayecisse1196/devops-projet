from rest_framework import serializers
from gestion.models.user import User


class UserSerializer(serializers.ModelSerializer):
    """Serializer pour la lecture des utilisateurs (GET)"""
    role_display = serializers.CharField(source='get_role_display', read_only=True)
    
    class Meta:
        model = User
        fields = [
            'id', 'prenom', 'nom', 'email', 'telephone',
            'role', 'role_display', 'actif', 'date_creation'
        ]


class SaveUserSerializer(serializers.Serializer):
    """Serializer pour la création d'un utilisateur (POST)"""
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    prenom = serializers.CharField(max_length=100)
    nom = serializers.CharField(max_length=100)
    telephone = serializers.CharField(max_length=20, required=False, allow_blank=True)
    role = serializers.ChoiceField(choices=['PELERIN', 'ADMIN'], default='PELERIN')


class UpdateUserSerializer(serializers.ModelSerializer):
    """Serializer pour la mise à jour d'un utilisateur (PUT/PATCH)"""
    class Meta:
        model = User
        fields = ['prenom', 'nom', 'telephone', 'actif']
