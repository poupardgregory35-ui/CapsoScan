# CaspoScan - Spécifications de conformité CPAM

Ce document détaille la logique métier implémentée dans le moteur de validation CaspoScan pour l'analyse des prescriptions médicales de transport.

---

## 1. Règles d'Extraction (Gemini AI)
L'intelligence artificielle analyse le document et détermine automatiquement le type de structure.

| Donnée | Règle d'extraction | Particularité OCR |
| :--- | :--- | :--- |
| **Structure** | Détection mot-clés (CHU, Clinique...) | Détermine l'obligation (RPPS vs FINESS) |
| **RPPS** | 11 chiffres consécutifs | Obligatoire pour **Libéral** |
| **FINESS** | 9 chiffres consécutifs | Obligatoire pour **Établissement** |
| **Signature** | Détection bas à droite | Toujours **Obligatoire** |

---

## 2. Logique de Scoring

### A. Règle Commune
*   **Signature manquante** : `-40 points` (CRITIQUE)

### B. Cas : Structure ÉTABLISSEMENT / URGENCE
*   **FINESS manquant ou invalide** : `-40 points`
*   **RPPS** : Optionnel (0 pénalité si absent)

### C. Cas : Structure LIBÉRAL
*   **RPPS manquant ou invalide** : `-40 points`
*   **FINESS** : Optionnel (0 pénalité si absent, -10 si mauvais format présent)

---

## 3. Seuils de Conformité UI
🟢 **90-100** : Conforme | 🟠 **50-89** : Vigilance | 🔴 **0-49** : Critique

---

## 4. Spécifications Techniques
*   **Traitement PDF** : Conversion haute résolution (Scale 2.0x), analyse de la première page uniquement.
*   **Moteur local** : Analyse client-side pour une confidentialité maximale.

## 5. Protection des Données (HDS & RGPD)
CaspoScan applique une politique de **Zero-Storage** :

*   **Analyse en RAM uniquement** : Les documents sont chargés en mémoire vive pour l'OCR et jamais écrits sur disque.
*   **Purge Immédiate** : La source de l'image est détruite (purgée) dès que l'extraction textuelle est terminée.
*   **Affichage Sécurisé** : Aucun aperçu visuel du document n'est affiché dans l'interface (prévention des captures d'écran).
*   **Confidentialité totale** : Aucune donnée ne quitte le navigateur.

---
*Document certifié conforme aux exigences de sécurité CapsoScan pour le déploiement HDS.*
