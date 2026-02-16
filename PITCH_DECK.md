# 📊 CapsoScan - Pitch Deck (8 Slides)

**Objectif : Convaincre Benjamin de l'impact immédiat sur la trésorerie des clients.**

---

## Slide 1 : La Promesse
**Titre :** CapsoScan : Sécurisez 100% du CA Transport Sanitaire
**Sous-titre :** La première IA de validation de prescriptions connectée au référentiel CPAM.
**Visuel :** Logo CapsoScan + Image d'un CERFA validé ✅

**Script :**
"Bonjour. Aujourd'hui, je vais vous montrer comment on peut récupérer les 50 000 € que chaque société d'ambulance perd chaque année à cause de simples erreurs administratives."

---

## Slide 2 : Le Problème (L'Hémorragie)
**Titre :** 2,5% de Rejets = 50k€ de Trésorerie Bloquée
**Points clés :**
- **2,5%** de taux de rejet moyen secteur.
- Pour une société de 2M€ CA = **50 000 €** perdus ou bloqués/an.
- **Cause n°1 :** Erreurs conformité (Signature manquante, RPPS invalide).
- **Conséquence :** Temps administratif perdu, délais de paiement x3.

**Visuel :** Graphique simple "Entonnoir de facturation" montrant la fuite de cash.

---

## Slide 3 : La Solution CapsoScan
**Titre :** Un "Douanier Numérique" avant l'envoi CPAM
**Concept :**
Validation automatique des pièces justificatives *avant* la télétransmission.
1. **Scan** (PDA/Mobile).
2. **Analyse IA & Règles Métier** (Immédiat).
3. **Verdict** : GO / NO-GO.

**Visuel :** Schéma simple : PDA -> CapsoScan -> CPAM (avec barrière verte/rouge).

---

## Slide 4 : La Technologie (Notre Force)
**Titre :** Conforme au Référentiel CPAM (Arrêté 2006)
**Points clés :**
- Ce n'est pas juste de l'IA générative.
- **Backend Rigoureux** : Implémente le cahier des charges officiel.
- **Règles Actives :**
  - ✅ Présence Signature (-40 pts).
  - ✅ Validité RPPS/FINESS (-30 pts).
  - ✅ Cohérence Dates.

**Visuel :** Capture d'écran du Swagger API ou bout de code `validators.py` (Rassurant/Robuste).

---

## Slide 5 : Démo Technique (Le "Wow")
**Titre :** 2 Secondes pour Éviter un Rejet
**Action :**
*Vidéo ou Live Démo :*
1. Upload CERFA invalide → ❌ **Bloqué** (Alerte: "Signature manquante").
2. Upload CERFA valide → ✅ **Validé**.

**Message :** "Le système a vu ce que l'humain fatigué a raté."

---

## Slide 6 : ROI et Impact (L'Argument Benjamin)
**Titre :** Rentabilité dès le 1er mois
**Chiffres :**
- **Taux de rejet visé :** < 0.1% (vs 2.5%).
- **Gain direct :** +49k€ de trésorerie/an par client.
- **Gain indirect :** 2h/jour de gestion administrative économisée.

**Visuel :** Tableau comparatif "Avant / Avec CapsoScan".

---

## Slide 7 : Intégration & Roadmap
**Titre :** Prêt pour l'Infrastructure Lomaco
**Points clés :**
- **Aujourd'hui :** API Dockerisée, prête à déployer.
- **Semaine prochaine :** Intégration flux PDA.
- **Q2 :** Extension Mutuelles (OCR cartes tiers-payant).

**Visuel :** Timeline simple (MVP -> Prod -> Scale).

---

## Slide 8 : Conclusion
**Titre :** Transformons la Conformité en Profit
**Appel à l'action :**
"La technologie est prête. Les règles CPAM sont codées.
Lançons un pilote sur 5 dossiers cette semaine."

**Visuel :** Contact + QR Code vers démo live.
