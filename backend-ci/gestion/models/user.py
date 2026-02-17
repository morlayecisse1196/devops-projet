from django.db import models
from django.contrib.auth.models import AbstractUser
from gestion.enums import Role


class User(AbstractUser):
    """
    Modèle User personnalisé qui étend AbstractUser.
    Remplace le modèle User par défaut de Django.
    """
    prenom = models.CharField(max_length=100, blank=True)
    nom = models.CharField(max_length=100, blank=True)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20, unique=True, null=True, blank=True)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PELERIN
    )
    actif = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    # Utiliser l'email comme identifiant de connexion
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'users'
        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.email})"
