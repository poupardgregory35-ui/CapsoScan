# CaspoScan

CapsoScan est une solution robuste pour la validation de prescriptions médicales (CERFA), assurant la conformité avec le référentiel CPAM (Arrêté du 23 décembre 2006).

## 🚀 Architecture

- **Frontend** : Interface HTML5 ultra-rapide avec extraction OCR locale (Tesseract.js/PDF.js).
- **Backend** : API FastAPI (Python) implémentant le moteur de règles de conformité CPAM.
- **Docker** : Stack containerisée pour un déploiement reproductible.
- **CI/CD** : Déploiement automatique vers Google Cloud Run via GitHub Actions.

## 🛠 Installation Locale

### Avec Docker (Recommandé)
```bash
docker-compose -f docker/docker-compose.yml up
```
Accès :
- Frontend : http://localhost:3000
- API Swagger : http://localhost:8000/docs

### Développement Python
```bash
cd backend
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## 📊 Conformité CPAM
Le moteur de règles calcule un score de conformité sur 100 :
- **Signature absente** : -40 points
- **RPPS manquant** : -30 points
- **Absence de cachet** : -10 points

Un score inférieur à 80 génère une alerte critique.
