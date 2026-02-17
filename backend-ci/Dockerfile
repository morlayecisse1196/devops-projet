# ============================================
# Stage 1: Builder - Installation des dépendances
# ============================================
FROM python:3.11-slim as builder

# Définir les variables d'environnement pour Python
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Installer les dépendances système nécessaires pour la compilation
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Créer un répertoire de travail
WORKDIR /app

# Copier uniquement requirements.txt pour exploiter le cache Docker
COPY requirements.txt .

# Installer les dépendances Python dans un répertoire local
RUN pip install --upgrade pip && \
    pip install --prefix=/install --no-warn-script-location -r requirements.txt

# ============================================
# Stage 2: Runtime - Image finale légère
# ============================================
FROM python:3.11-slim

# Métadonnées de l'image
LABEL maintainer="votre-email@example.com" \
      description="Backend Django API - Gestion Événement Magal" \
      version="1.0.0"

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/install/lib/python3.11/site-packages \
    PATH=/install/bin:$PATH \
    DJANGO_SETTINGS_MODULE=gestion_evenement_magal.settings

# Installer uniquement les runtime dependencies (pas gcc)
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copier les dépendances Python depuis le builder
COPY --from=builder /install /install

# Créer un utilisateur non-root pour la sécurité
RUN useradd --create-home --shell /bin/bash appuser && \
    mkdir -p /app && \
    chown -R appuser:appuser /app

# Définir le répertoire de travail
WORKDIR /app

# Copier le code de l'application
COPY --chown=appuser:appuser . .

# Créer les répertoires nécessaires
RUN mkdir -p /app/staticfiles /app/media && \
    chown -R appuser:appuser /app/staticfiles /app/media

# Passer à l'utilisateur non-root
USER appuser

# Exposer le port 8000
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1

# Script de démarrage
COPY --chown=appuser:appuser docker-entrypoint.sh /app/
USER root
RUN chmod +x /app/docker-entrypoint.sh
USER appuser

# Point d'entrée
ENTRYPOINT ["/app/docker-entrypoint.sh"]

# Commande par défaut (peut être override)
CMD ["gunicorn", "gestion_evenement_magal.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120"]
