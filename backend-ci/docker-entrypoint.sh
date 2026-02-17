#!/bin/bash

# Script de démarrage pour le conteneur Django
set -e

echo "🚀 Démarrage du conteneur Django..."

# Attendre que la base de données soit prête
if [ -n "$DATABASE_URL" ] || [ -n "$POSTGRES_HOST" ]; then
    echo "⏳ Attente de la base de données PostgreSQL..."
    
    # Extraire l'hôte depuis DATABASE_URL ou utiliser POSTGRES_HOST
    if [ -n "$DATABASE_URL" ]; then
        DB_HOST=$(echo $DATABASE_URL | sed -E 's|.*@([^:/]+).*|\1|')
        DB_PORT=$(echo $DATABASE_URL | sed -E 's|.*:([0-9]+)/.*|\1|')
    else
        DB_HOST=${POSTGRES_HOST:-db}
        DB_PORT=${POSTGRES_PORT:-5432}
    fi
    
    # Boucle d'attente jusqu'à ce que PostgreSQL soit prêt
    until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "${POSTGRES_USER:-postgres}" 2>/dev/null; do
        echo "⏳ PostgreSQL n'est pas encore prêt sur $DB_HOST:$DB_PORT - attente..."
        sleep 2
    done
    
    echo "✅ PostgreSQL est prêt!"
fi

# Exécuter les migrations
echo "🔄 Exécution des migrations..."
python manage.py migrate --noinput

# Collecter les fichiers statiques (avec skip si erreur)
echo "📦 Collecte des fichiers statiques..."
python manage.py collectstatic --noinput --clear 2>/dev/null || echo "⚠️  Collecte des statiques ignorée (pas configuré)"

# Créer un superuser si les variables sont définies (optionnel)
if [ -n "$DJANGO_SUPERUSER_EMAIL" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ]; then
    echo "👤 Création du superuser..."
    python manage.py shell -c "
from django.contrib.auth import get_user_model;
User = get_user_model();
if not User.objects.filter(email='$DJANGO_SUPERUSER_EMAIL').exists():
    User.objects.create_superuser(
        email='$DJANGO_SUPERUSER_EMAIL',
        username='${DJANGO_SUPERUSER_USERNAME:-admin}',
        password='$DJANGO_SUPERUSER_PASSWORD'
    );
    print('✅ Superuser créé avec succès');
else:
    print('ℹ️  Superuser existe déjà');
" || echo "⚠️  Erreur lors de la création du superuser"
fi

echo "✅ Initialisation terminée!"
echo "🎯 Démarrage du serveur..."

# Exécuter la commande passée au conteneur
exec "$@"
