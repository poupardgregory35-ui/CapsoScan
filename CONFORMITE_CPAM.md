# CaspoScan - Spécifications de conformité CPAM

Ce document détaille la logique métier implémentée dans le moteur de validation CapsoScan pour l'analyse des prescriptions médicales de transport.

---

## 1. Règles d'Extraction (Gemini AI)
L'intelligence artificielle (Gemini 3 Flash) est configurée avec les filtres suivants :

| Donnée | Règle d'extraction | Particularité OCR |
| :--- | :--- | :--- |
| **RPPS** | 11 chiffres consécutifs | Extrait même si collé à du texte (ex: `Id:12345678901`) |
| **FINESS** | 9 chiffres consécutifs | Extrait même si collé à du texte (ex: `Structure350000741`) |
| **Signature** | Détection bas à droite | Inclut signatures manuscrites et tampons humides |
| **Typologie** | Analyse contextuelle | `URGENCE` si "SAMU", "SMUR" ou "Centre 15" |

---

## 2. Logique de Scoring (Moteur de Règles)
Le score initial est de **100/100**.

### A. Règle Commune
*   **Signature manquante** : `-40 points` (Alerte Vigilance)

### B. Cas : Prescripteur INDIVIDUEL (Libéral)
*   **RPPS absent ou invalide** : `-30 points` (Alerte Vigilance)
*   **Absence totale d'ID (ni RPPS, ni FINESS)** : `-10 points` (Pénalité cachet)
*   *Note : Le RPPS est l'identifiant légal obligatoire ici.*

### C. Cas : ÉTABLISSEMENT / URGENCE (Hôpitaux, SAMU, Cliniques)
*   **Mode Structure activé si** : Typologie "URGENCE" OU mot-clé SAMU/CHU OU FINESS présent.
*   **FINESS absent** : `0 point` (Autorisé pour les salariés)
*   **RPPS absent** : `0 point` (Autorisé pour les salariés)
*   **Logique** : Dans les structures publiques/privées, les prescripteurs sont salariés, l'identification de la structure ou de l'urgence prime.

---

## 3. Seuils de Conformité UI
Le résultat visuel dans l'application suit ces seuils :

*   🟢 **90 - 100** : **Conforme** (Prêt pour télétransmission)
*   🔵 **70 - 89** : **Satisfaisant** (Anomalies mineures)
*   🟠 **50 - 69** : **Vigilance** (Données clés manquantes)
*   🔴 **0 - 49** : **Critique** (Document non recevable)

---

## 4. Spécifications Techniques
*   **Regex RPPS** : `^\d{11}$`
*   **Regex FINESS** : `^\d{9}$`
*   **Traitement PDF** : Conversion haute résolution (Scale 2.0x), analyse de la **page 1 uniquement**.

---
*Document de référence pour le déploiement HDS et conformité réglementaire.*
