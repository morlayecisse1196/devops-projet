#!/bin/bash

# Script de restauration de la base de données PostgreSQL
# Usage: ./restore.sh <backup_file>

set -e

if [ $# -eq 0 ]; then
    echo "❌ Usage: $0 <backup_file>"
    echo "Exemple: $0 backups/backup_20240115_120000.sql.gz"
    exit 1
fi

BACKUP_FILE=$1

# Vérifier que le fichier existe
if [ ! -f "$BACKUP_FILE" ]; then
    echo "❌ Fichier introuvable: $BACKUP_FILE"
    exit 1
fi

# Charger les variables d'environnement
if [ -f ../.env ]; then
    source ../.env
else
    echo "❌ Fichier .env non trouvé!"
    exit 1
fi

echo "⚠️  ATTENTION: Cette opération va écraser la base de données actuelle!"
read -p "Continuer? (yes/no): " -r
if [[ ! $REPLY =~ ^[Yy][Ee][Ss]$ ]]; then
    echo "❌ Restauration annulée"
    exit 1
fi

echo "🔄 Démarrage de la restauration..."

# Décompresser si nécessaire
if [[ $BACKUP_FILE == *.gz ]]; then
    echo "📦 Décompression du backup..."
    gunzip -k "$BACKUP_FILE"
    BACKUP_FILE="${BACKUP_FILE%.gz}"
fi

# Restaurer la base de données
echo "🔄 Restauration de la base de données..."
docker-compose exec -T db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" < "$BACKUP_FILE"

if [ $? -eq 0 ]; then
    echo "✅ Restauration réussie!"
else
    echo "❌ Erreur lors de la restauration"
    exit 1
fi
