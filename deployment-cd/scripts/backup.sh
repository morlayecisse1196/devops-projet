#!/bin/bash

# Script de backup de la base de données PostgreSQL
# Usage: ./backup.sh

set -e

# Configuration
BACKUP_DIR="${BACKUP_DIR:-./backups}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BACKUP_FILE="$BACKUP_DIR/backup_$TIMESTAMP.sql"

# Charger les variables d'environnement
if [ -f ../.env ]; then
    source ../.env
else
    echo "❌ Fichier .env non trouvé!"
    exit 1
fi

# Créer le dossier de backup s'il n'existe pas
mkdir -p "$BACKUP_DIR"

echo "🔄 Démarrage du backup de la base de données..."
echo "📁 Fichier: $BACKUP_FILE"

# Exécuter le backup via docker-compose
docker-compose exec -T db pg_dump -U "$POSTGRES_USER" "$POSTGRES_DB" > "$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "✅ Backup réussi: $BACKUP_FILE"
    
    # Compresser le backup
    gzip "$BACKUP_FILE"
    echo "📦 Fichier compressé: $BACKUP_FILE.gz"
    
    # Nettoyer les anciens backups (garder 7 jours par défaut)
    RETENTION_DAYS="${BACKUP_RETENTION_DAYS:-7}"
    find "$BACKUP_DIR" -name "backup_*.sql.gz" -mtime +$RETENTION_DAYS -delete
    echo "🧹 Anciens backups supprimés (>$RETENTION_DAYS jours)"
else
    echo "❌ Erreur lors du backup"
    exit 1
fi
