# 🌐 Déploiement Frontend sur Vercel

**URL Production visée :** https://capsoscan-frontend.vercel.app

---

## 🛠 Configuration (vercel.json)

Le fichier `vercel.json` à la racine redirige automatiquement le trafic vers le dossier `frontend/`.

## 🚀 Étapes de Déploiement

### 1. via Dashboard Vercel (Recommandé)
1. Importe le repo `poupardgregory35/ui`.
2. Framework : `Other`.
3. Root Directory : `./`.
4. Output Directory : `frontend`.
5. Ajoute la variable d'env `API_URL` pointant vers ton API GCP.

### 2. via CLI Vercel
```bash
npm install -g vercel
vercel login
vercel --prod
```

---

## ⚠️ Point Critique : CORS
Le backend (FastAPI) est configuré pour accepter les requêtes venant de :
- `http://localhost:3000`
- `https://capsoscan-frontend.vercel.app`
- Les domaines `*.vercel.app` (previews)

Si tu changes d'URL Vercel, n'oublie pas de mettre à jour `backend/main.py`.
