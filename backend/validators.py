import re
from typing import List, Dict, Any, Tuple

REGEX_RPPS = re.compile(r"^\d{11}$")
REGEX_FINESS = re.compile(r"^\d{9}$")

def validate_rpps_format(rpps: str) -> bool:
    return bool(REGEX_RPPS.match(rpps)) if rpps else False

def validate_finess_format(finess: str) -> bool:
    return bool(REGEX_FINESS.match(finess)) if finess else False

def calculate_compliance_score(
    structure_type: str, # "liberal" ou "etablissement"
    has_signature: bool,
    rpps: str,
    finess: str,
    typologie: str = "UNITAIRE"
) -> Tuple[int, List[Dict[str, str]]]:
    """
    Moteur de règles CaspoScan - Version Spécification FINESS Conditionnel
    """
    score = 100
    alerts = []
    
    # 1. Signature Check (Toujours obligatoire)
    if not has_signature:
        score -= 40
        alerts.append({"type": "vigilance", "msg": "Signature manquante"})
        
    # 2. Règle FINESS Conditionnelle (Spécification Technique)
    if structure_type == "etablissement":
        # Règle 1 : Établissement → FINESS non requis (0 pénalité)
        pass 
    else:
        # Règle 2 : Libéral → Validation stricte
        if not finess or finess.strip() == "":
            score -= 40
            alerts.append({"type": "vigilance", "msg": "FINESS obligatoire pour les libéraux"})
        elif not validate_finess_format(finess):
            score -= 30
            alerts.append({"type": "vigilance", "msg": "Format FINESS invalide (9 chiffres requis)"})

    # 3. Règle RPPS (Libéral)
    # On garde la logique que le RPPS est requis pour les libéraux
    has_rpps = validate_rpps_format(rpps)
    if structure_type == "liberal" and not has_rpps:
        score -= 30
        alerts.append({"type": "vigilance", "msg": "RPPS manquant ou format invalide"})

    # 4. Détection Urgence / SAMU (CHU)
    # Si Urgence, on s'assure que le score ne soit pas trop pénalisé si c'est une structure hospitalière
    if typologie == "URGENCE":
        # Dans le cas d'urgence, on est souvent en mode établissement de fait
        # On pourrait imaginer un bonus ou une remise à zéro des pénalités ID
        pass

    score = max(0, score)
    return score, alerts
