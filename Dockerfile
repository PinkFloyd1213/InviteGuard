# Utiliser une image de base Python officielle, par exemple Python 3.9
FROM python:3.9-slim

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier le fichier requirements.txt dans le conteneur pour installer les dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source de l'application dans le conteneur
COPY . .

# Exécuter main.py lorsque le conteneur démarre
CMD ["python", "main.py"]