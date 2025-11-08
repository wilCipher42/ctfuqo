# Utiliser une image Python légère
FROM python:3.9-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances et les installer
COPY deploy/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY ../src .

# Exposer le port de Flask
EXPOSE 5000

# Commande pour lancer l'application
CMD ["python", "app.py"]