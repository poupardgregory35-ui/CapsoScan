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
    Moteur de règles CaspoScan - Version Mise à jour FINESS/RPPS
    Rule: 
    - Etablissement: FINESS Obligatoire, RPPS Optionnel
    - Liberal: RPPS Obligatoire, FINESS Optionnel
    """
    score = 100
    alerts = []
    
    # 1. Signature Check (Toujours obligatoire)
    if not has_signature:
        score -= 40
        alerts.append({"type": "vigilance", "msg": "Signature manquante"})
        
    # 2. Règle Typologie Urgence (SAMU/Centre 15)
    # Souvent assimilé à établissement hospitalier
    if typologie == "URGENCE" and structure_type != "etablissement":
        structure_type = "etablissement"

    # 3. Validation selon le type de structure
    if structure_type == "etablissement":
        # FINESS OBLIGATOIRE
        if not finess or not validate_finess_format(finess):
            score -= 40
            alerts.append({"type": "vigilance", "msg": "FINESS manquant ou invalide (Obligatoire pour Etablissement)"})
        # RPPS OPTIONNEL (Pas de pénalité si absent)
    
    else: # Mode LIBERAL
        # RPPS OBLIGATOIRE
        if not rpps or not validate_rpps_format(rpps):
            score -= 40
            alerts.append({"type": "vigilance", "msg": "RPPS manquant ou invalide (Obligatoire pour Libéral)"})
        # FINESS OPTIONNEL (Mais vérifié si présent)
        if finess and not validate_finess_format(finess):
            score -= 10
            alerts.append({"type": "info", "msg": "Format FINESS incorrect"})

    score = max(0, score)
    return score, alerts
