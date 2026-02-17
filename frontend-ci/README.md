# Frontend - Gestion Événement Magal (CI)

Interface web React pour la gestion des événements Magal.

## 🏗️ Architecture

- **Framework:** React 19
- **Language:** TypeScript
- **Build Tool:** Vite
- **Styling:** Tailwind CSS
- **UI Components:** Radix UI
- **State Management:** Zustand
- **Data Fetching:** React Query (TanStack Query)
- **Forms:** React Hook Form + Zod
- **Routing:** React Router v6

## 📋 Prérequis

- Node.js 18+
- npm 9+ ou yarn
- Backend API en cours d'exécution

## 🚀 Installation Locale

### 1. Cloner le repository

```bash
git clone <url-du-repo>
cd frontend-ci
```

### 2. Installer les dépendances

```bash
npm install
# ou
yarn install
```

### 3. Configuration

Créer un fichier `.env` à la racine:

```env
VITE_API_URL=http://127.0.0.1:8000/api
```

### 4. Lancer le serveur de développement

```bash
npm run dev
# ou
yarn dev
```

L'application sera accessible sur: **http://localhost:5173**

## 🏭 Build Production

```bash
npm run build
# ou
yarn build
```

Les fichiers de production seront dans le dossier `dist/`.

### Prévisualiser le build

```bash
npm run preview
# ou
yarn preview
```

## 📚 Fonctionnalités

### 🔐 Authentification
- Page de connexion
- Page d'inscription
- Gestion des tokens JWT (access + refresh)
- Refresh automatique des tokens
- Déconnexion

### 📊 Dashboard
- Vue d'ensemble des statistiques
- Graphiques et métriques

### 📋 Gestion
- **Événements:** CRUD complet
- **Lieux:** Gestion des lieux d'événements
- **Inscriptions:** Gestion des inscriptions aux événements
- **Imams:** Informations sur les imams
- **Histoires:** Récits et histoires du Magal
- **Notifications:** Système de notifications
- **Utilisateurs:** Gestion des utilisateurs (admin)

## 📦 Structure du Projet

```
frontend-ci/
├── public/                    # Fichiers statiques
├── src/
│   ├── assets/               # Images, icons, etc.
│   ├── components/           # Composants réutilisables
│   │   ├── layout/          # Layout (Header, Sidebar, etc.)
│   │   └── ui/              # Composants UI de base
│   ├── data/                # Données statiques
│   ├── lib/                 # Utilitaires et helpers
│   ├── pages/               # Pages de l'application
│   │   ├── auth/           # Connexion, Inscription
│   │   ├── dashboard/      # Dashboard
│   │   ├── evenements/     # Gestion événements
│   │   ├── lieux/          # Gestion lieux
│   │   ├── inscriptions/   # Gestion inscriptions
│   │   ├── imams/          # Gestion imams
│   │   ├── histoires/      # Gestion histoires
│   │   ├── notifications/  # Notifications
│   │   └── utilisateurs/   # Gestion utilisateurs
│   ├── services/            # Services API
│   │   ├── api.ts          # Configuration Axios
│   │   ├── auth.service.ts
│   │   ├── evenement.service.ts
│   │   └── ...
│   ├── stores/              # State management (Zustand)
│   ├── types/               # TypeScript types
│   ├── App.tsx              # Composant principal
│   ├── main.tsx            # Point d'entrée
│   └── index.css           # Styles globaux
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.js
├── Dockerfile              # À créer (Phase 3)
├── Jenkinsfile            # À créer (Phase 8)
├── nginx.conf             # À créer (Phase 3)
└── README.md
```

## 🔌 API Integration

L'application consomme l'API backend via Axios avec:
- Intercepteurs pour ajouter automatiquement les tokens JWT
- Refresh automatique des tokens expirés
- Gestion centralisée des erreurs
- Redirection vers login si non authentifié

Voir `src/services/api.ts` pour la configuration.

## 🧪 Tests

```bash
# Lancer les tests
npm test
# ou
yarn test

# Tests avec coverage
npm run test:coverage
# ou
yarn test:coverage

# Linting
npm run lint
# ou
yarn lint
```

## 🐳 Docker

### Build de l'image

```bash
docker build -t frontend-magal:latest .
```

### Lancer avec Docker

```bash
docker run -p 80:80 -e VITE_API_URL=http://api.example.com frontend-magal:latest
```

## 🎨 Thème et Styling

- **Tailwind CSS** pour le styling utilitaire
- **Radix UI** pour les composants accessibles
- **CSS Variables** pour le thème
- Design responsive (mobile-first)

## 🔄 Pipeline CI/CD

Le pipeline Jenkins automatise:
1. ✅ Checkout du code
2. ✅ Installation des dépendances
3. ✅ Build de l'application
4. ✅ Exécution des tests
5. ✅ Linting et audit de sécurité
6. ✅ Build de l'image Docker
7. ✅ Scan de vulnérabilités
8. ✅ Push vers Docker Hub

Voir `Jenkinsfile` pour les détails.

## 🛡️ Sécurité

- Protection XSS avec React
- Validation des formulaires avec Zod
- Gestion sécurisée des tokens (localStorage)
- HTTPS en production
- CSP headers via nginx

## 🌐 Routes

### Routes Publiques
- `/login` - Page de connexion
- `/register` - Page d'inscription

### Routes Protégées (nécessitent authentification)
- `/` - Dashboard
- `/evenements` - Gestion des événements
- `/lieux` - Gestion des lieux
- `/inscriptions` - Gestion des inscriptions
- `/imams` - Gestion des imams
- `/histoires` - Gestion des histoires
- `/notifications` - Notifications
- `/utilisateurs` - Gestion des utilisateurs (admin)
- `/parametres` - Paramètres (à venir)

## 🚀 Optimisations

- Code splitting automatique avec Vite
- Lazy loading des routes
- Optimisation des images
- Compression gzip/brotli (nginx)
- Cache stratégique avec React Query

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
