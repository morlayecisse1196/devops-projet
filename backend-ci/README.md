# Backend - Gestion Événement Magal (CI)

API REST Django pour la gestion des événements Magal.

## 🏗️ Architecture

- **Framework:** Django 4.2 + Django REST Framework
- **Authentification:** JWT (Simple JWT)
- **Base de données:** PostgreSQL (production) / SQLite (développement)
- **Documentation API:** Swagger/OpenAPI (drf-spectacular)

## 📋 Prérequis

- Python 3.11+
- PostgreSQL 14+ (pour production)
- Docker & Docker Compose (pour containerisation)

## 🚀 Installation Locale

### 1. Cloner le repository

```bash
git clone <url-du-repo>
cd backend-ci
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configuration

Créer un fichier `.env` à la racine:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3

# Pour PostgreSQL (production)
# DATABASE_URL=postgresql://user:password@localhost:5432/dbname

ALLOWED_HOSTS=localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=http://localhost:5173,http://localhost:3000
```

### 5. Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Créer un superuser

```bash
python manage.py createsuperuser
```

### 7. Lancer le serveur

```bash
python manage.py runserver
```

L'API sera accessible sur: **http://127.0.0.1:8000**

## 📚 Documentation API

Une fois le serveur lancé, accédez à:

- **Swagger UI:** http://127.0.0.1:8000/api/docs/
- **ReDoc:** http://127.0.0.1:8000/api/redoc/
- **Schéma OpenAPI:** http://127.0.0.1:8000/api/schema/

## 🔑 Endpoints Principaux

### Authentification
- `POST /api/auth/login/` - Connexion (obtenir access & refresh tokens)
- `POST /api/auth/refresh/` - Rafraîchir l'access token

### Ressources (nécessitent authentification)
- `GET/POST /api/users/` - Liste/Créer utilisateurs
- `GET/POST /api/evenements/` - Liste/Créer événements
- `GET/POST /api/lieux/` - Liste/Créer lieux
- `GET/POST /api/inscriptions/` - Liste/Créer inscriptions
- `GET/POST /api/imams/` - Liste/Créer imams
- `GET/POST /api/histoires/` - Liste/Créer histoires
- `GET/POST /api/notifications/` - Liste/Créer notifications

## 🧪 Tests

```bash
# Lancer tous les tests
python manage.py test

# Tests avec coverage
coverage run --source='.' manage.py test
coverage report
```

## 🐳 Docker

### Build de l'image

```bash
docker build -t backend-magal:latest .
```

### Lancer avec Docker

```bash
docker run -p 8000:8000 -e DATABASE_URL=sqlite:///db.sqlite3 backend-magal:latest
```

## 📦 Structure du Projet

```
backend-ci/
├── gestion/                    # Application principale
│   ├── models/                # Modèles de données
│   ├── serializers/           # Serializers DRF
│   ├── views/                 # Vues/Controllers
│   ├── services/              # Logique métier
│   ├── urls/                  # Configuration des routes
│   └── enums/                 # Énumérations
├── gestion_evenement_magal/   # Configuration Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── Dockerfile                 # À créer (Phase 2)
├── Jenkinsfile               # À créer (Phase 7)
└── README.md
```

## 🔄 Pipeline CI/CD

Le pipeline Jenkins automatise:
1. ✅ Checkout du code
2. ✅ Installation des dépendances
3. ✅ Exécution des tests
4. ✅ Scan de sécurité (Bandit, Safety)
5. ✅ Build de l'image Docker
6. ✅ Scan de vulnérabilités (Trivy)
7. ✅ Push vers Docker Hub

Voir `Jenkinsfile` pour les détails.

## 🛡️ Sécurité

- Authentification JWT avec refresh tokens
- CORS configuré
- Validation des données avec serializers
- Protection CSRF
- Scan automatique des vulnérabilités

## 📝 Modèles de Données

### User
- Authentification par email
- Rôles: PELERIN, ORGANISATEUR, ADMIN
- Champs: prenom, nom, email, telephone, role

### Événement
- Gestion des événements Magal
- Lié à un lieu et des inscriptions

### Inscription
- Inscription des pèlerins aux événements
- Statut: EN_ATTENTE, CONFIRMEE, ANNULEE

(Voir la documentation Swagger pour tous les modèles)

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
