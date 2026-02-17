# Déploiement - Gestion Événement Magal (CD)

Repository de déploiement automatisé pour l'application Gestion Événement Magal.

## 🏗️ Architecture

Ce repository contient la configuration pour déployer l'application complète composée de:
- **Backend API** (Django)
- **Frontend Web** (React)
- **Base de données** (PostgreSQL)

## 📋 Prérequis

- Docker 20.10+
- Docker Compose 2.0+
- Jenkins (pour le pipeline CD)
- Compte Docker Hub
- Serveur de déploiement (Linux recommandé)

## 🚀 Déploiement avec Docker Compose

### 1. Cloner le repository

```bash
git clone <url-du-repo>
cd deployment-cd
```

### 2. Configuration des variables d'environnement

Copier le fichier d'exemple et le configurer:

```bash
cp .env.example .env
```

Éditer `.env`:

```env
# Database
POSTGRES_DB=magal_db
POSTGRES_USER=magal_user
POSTGRES_PASSWORD=changeme_secure_password
POSTGRES_HOST=db
POSTGRES_PORT=5432

# Django Backend
DJANGO_SECRET_KEY=your-super-secret-key-change-me
DJANGO_DEBUG=False
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,your-domain.com
DJANGO_CORS_ORIGINS=http://localhost,https://your-domain.com

# Docker Images (from Docker Hub)
BACKEND_IMAGE=your-dockerhub-username/backend-magal:latest
FRONTEND_IMAGE=your-dockerhub-username/frontend-magal:latest

# API URL for Frontend
VITE_API_URL=http://localhost:8000/api
# En production: VITE_API_URL=https://api.your-domain.com/api
```

### 3. Déploiement

#### Développement/Test
```bash
docker-compose up -d
```

#### Production
```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### 4. Vérification

```bash
# Vérifier les services
docker-compose ps

# Voir les logs
docker-compose logs -f

# Logs d'un service spécifique
docker-compose logs -f backend
```

## 📦 Services

### 1. Base de données PostgreSQL
- **Port:** 5432 (interne)
- **Volume:** `postgres_data` (persistant)
- **Health check:** Automatique

### 2. Backend (Django API)
- **Port:** 8000
- **URL:** http://localhost:8000
- **Documentation API:** http://localhost:8000/api/docs/
- **Dépend de:** db

### 3. Frontend (React + Nginx)
- **Port:** 80 (ou 3000 en dev)
- **URL:** http://localhost
- **Dépend de:** backend

## 🔄 Pipeline CD (Jenkins)

Le pipeline automatise le déploiement:

### Étapes du Pipeline

1. **Pull des Images**
   - Récupère les dernières images depuis Docker Hub
   
2. **Health Check Pré-déploiement**
   - Vérifie l'état des services actuels
   
3. **Backup Base de Données**
   - Sauvegarde PostgreSQL avant mise à jour
   
4. **Déploiement Rolling Update**
   - Démarre nouvelles instances
   - Effectue health checks
   - Bascule le trafic
   - Arrête anciennes instances
   
5. **Vérification Post-déploiement**
   - Tests de smoke
   - Vérification endpoints critiques
   
6. **Rollback Automatique**
   - En cas d'échec, restaure version précédente

### Déclencheurs

- **Manuel:** Depuis Jenkins
- **Automatique:** Après succès des pipelines CI (backend + frontend)
- **Webhook:** Post-push sur branche `main`

Voir `Jenkinsfile` pour les détails.

## 🗂️ Structure du Projet

```
deployment-cd/
├── docker-compose.yml          # Configuration principale
├── docker-compose.prod.yml     # Overrides production
├── .env.example               # Template variables d'environnement
├── .env                       # Variables (gitignored)
├── Jenkinsfile               # Pipeline CD
├── scripts/
│   ├── backup.sh            # Script de backup DB
│   ├── restore.sh           # Script de restauration DB
│   ├── healthcheck.sh       # Script de health check
│   └── deploy.sh            # Script de déploiement
├── monitoring/
│   └── prometheus.yml       # Configuration monitoring (optionnel)
└── README.md
```

## 🛡️ Sécurité

### Bonnes Pratiques

1. **Variables d'environnement**
   - Ne jamais commit le fichier `.env`
   - Utiliser des secrets forts en production
   - Rotation régulière des secrets

2. **Réseau Docker**
   - Réseau isolé pour les services
   - Exposition minimale des ports
   - Communication interne sécurisée

3. **Volumes**
   - Volumes nommés pour la persistance
   - Backups réguliers
   - Permissions appropriées

4. **Images Docker**
   - Utiliser des versions taggées (pas `latest` en prod)
   - Scanner les vulnérabilités
   - Images à jour

## 🔧 Commandes Utiles

### Gestion des Services

```bash
# Démarrer tous les services
docker-compose up -d

# Arrêter tous les services
docker-compose down

# Redémarrer un service
docker-compose restart backend

# Recréer un service (pull nouvelle image)
docker-compose pull backend
docker-compose up -d --no-deps --build backend

# Voir les logs en temps réel
docker-compose logs -f --tail=100

# Exécuter une commande dans un conteneur
docker-compose exec backend python manage.py migrate
docker-compose exec db psql -U magal_user -d magal_db
```

### Backup & Restore

```bash
# Backup manuel de la base de données
./scripts/backup.sh

# Restaurer depuis un backup
./scripts/restore.sh backups/backup-2024-01-15.sql
```

### Monitoring

```bash
# Statistiques des conteneurs
docker stats

# Espace utilisé
docker system df

# Nettoyer les ressources inutilisées
docker system prune -a
```

## 📊 Health Checks

Chaque service implémente des health checks:

### Backend
```bash
curl http://localhost:8000/api/health/
```

### Frontend
```bash
curl http://localhost/
```

### Database
```bash
docker-compose exec db pg_isready -U magal_user
```

## 🔄 Stratégie de Déploiement Sans Interruption

### Rolling Update (Recommandé)

1. Démarrer nouvelle instance du service
2. Attendre health check OK
3. Router le trafic vers nouvelle instance
4. Arrêter ancienne instance

### Blue-Green Deployment (Avancé)

1. Deux environnements identiques (Blue/Green)
2. Déployer sur l'environnement inactif
3. Tester
4. Basculer le proxy/load balancer
5. Garder l'ancien pour rollback rapide

## 🚨 Troubleshooting

### Les services ne démarrent pas

```bash
# Vérifier les logs
docker-compose logs

# Vérifier la configuration
docker-compose config

# Recréer les conteneurs
docker-compose down -v
docker-compose up -d
```

### Problèmes de connexion à la DB

```bash
# Vérifier que la DB est prête
docker-compose exec db pg_isready

# Se connecter à la DB
docker-compose exec db psql -U magal_user -d magal_db

# Vérifier les migrations
docker-compose exec backend python manage.py showmigrations
```

### Frontend ne peut pas joindre le Backend

1. Vérifier `VITE_API_URL` dans `.env`
2. Vérifier CORS dans le backend
3. Vérifier que les services sont sur le même réseau Docker

## 📈 Monitoring (Optionnel)

Pour un monitoring avancé, intégrer:
- **Prometheus** - Métriques
- **Grafana** - Visualisation
- **ELK Stack** - Logs centralisés
- **Sentry** - Tracking des erreurs

Configuration dans `monitoring/`

## 🤝 Contribution

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit (`git commit -m 'Add AmazingFeature'`)
4. Push (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence [Votre Licence]

## 👥 Auteurs

- Votre équipe DevOps

## 📞 Support

Pour toute question, contactez [votre-email]
