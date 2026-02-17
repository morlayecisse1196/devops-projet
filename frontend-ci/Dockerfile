# Étape 1 : Construction (Build) - On passe à Node 20
FROM node:20-alpine AS build
WORKDIR /app

# Installation des dépendances
COPY package*.json ./
# Utilisation de --network=host peut parfois aider si vous avez des soucis réseau sur AWS
RUN npm install

# Copie du code source et build
COPY . .
RUN npm run build

# Étape 2 : Production avec Nginx
FROM nginx:stable-alpine
COPY --from=build /app/dist /usr/share/nginx/html
# Note : Vite génère souvent un dossier 'dist' et non 'build'. 
# Vérifiez si votre dossier de sortie est 'dist' ou 'build' !

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
