#!/bin/bash

# Script de vérification de santé des services
# Usage: ./healthcheck.sh

set -e

echo "🏥 Vérification de santé des services..."
echo "========================================"

# Charger les variables d'environnement
if [ -f ../.env ]; then
    source ../.env
else
    echo "❌ Fichier .env non trouvé!"
    exit 1
fi

BACKEND_URL="${BACKEND_URL:-http://localhost:8000}"
FRONTEND_URL="${FRONTEND_URL:-http://localhost}"
ALL_HEALTHY=true

# Fonction de health check
check_service() {
    local service_name=$1
    local url=$2
    local max_retries=3
    local retry=0
    
    while [ $retry -lt $max_retries ]; do
        if curl -f -s -o /dev/null "$url"; then
            echo "✅ $service_name: OK"
            return 0
        fi
        retry=$((retry + 1))
        sleep 2
    done
    
    echo "❌ $service_name: FAILED"
    ALL_HEALTHY=false
    return 1
}

# Vérifier PostgreSQL
echo ""
echo "🗄️  Database (PostgreSQL):"
if docker-compose exec -T db pg_isready -U "$POSTGRES_USER" > /dev/null 2>&1; then
    echo "✅ PostgreSQL: OK"
else
    echo "❌ PostgreSQL: FAILED"
    ALL_HEALTHY=false
fi

# Vérifier Backend
echo ""
echo "⚙️  Backend API:"
check_service "Backend Health" "$BACKEND_URL/api/health/" || true
check_service "Backend Swagger" "$BACKEND_URL/api/docs/" || true

# Vérifier Frontend
echo ""
echo "🌐 Frontend:"
check_service "Frontend" "$FRONTEND_URL/" || true

# Vérifier les conteneurs Docker
echo ""
echo "🐳 Docker Containers:"
docker-compose ps

echo ""
echo "========================================"

if [ "$ALL_HEALTHY" = true ]; then
    echo "✅ Tous les services sont opérationnels"
    exit 0
else
    echo "❌ Certains services rencontrent des problèmes"
    exit 1
fi
