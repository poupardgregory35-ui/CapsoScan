# Guide de Déploiement CapsoScan

## ☁️ Google Cloud Platform (GCP)

### 1. Prérequis
- Un projet GCP avec la facturation activée.
- APIs activées : `run.googleapis.com`, `cloudbuild.googleapis.com`.

### 2. Déploiement via GitHub Actions
Le déploiement est automatisé. Pour l'activer :
1. Ajoutez votre projet GCP dans les secrets GitHub sous le nom `GCP_PROJECT_ID`.
2. Générez une clé de compte de service au format JSON avec les rôles "Cloud Run Admin" et "Storage Admin".
3. Ajoutez cette clé dans les secrets GitHub sous le nom `GCP_SA_KEY`.

### 3. Déploiement Manuel (Gcloud CLI)
```bash
gcloud builds submit --tag gcr.io/VOTRE_PROJET/capsoscan-api -f docker/Dockerfile.backend .
gcloud run deploy capsoscan-api --image gcr.io/VOTRE_PROJET/capsoscan-api --region europe-west1 --allow-unauthenticated
```

## 🏥 Hébergement HDS (Lomaco)
Pour un déploiement sur l'infrastructure HDS de Lomaco :
1. Transférez le dossier `backend/` sur le serveur HDS.
2. Configurez les variables d'environnement `PORT` et `GCP_PROJECT_ID`.
3. Assurez-vous que Python 3.9+ est installé et lancez via Uvicorn.
