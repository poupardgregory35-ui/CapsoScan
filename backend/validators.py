import re
from typing import List, Dict, Any, Tuple

REGEX_RPPS = re.compile(r"^\d{11}$")
REGEX_FINESS = re.compile(r"^\d{9}$")

def validate_rpps_format(rpps: str) -> bool:
    return bool(REGEX_RPPS.match(rpps)) if rpps else False

def validate_finess_format(finess: str) -> bool:
    return bool(REGEX_FINESS.match(finess)) if finess else False

def calculate_compliance_score(
    prescripteur_type: str, # 'INDIVIDUEL' or 'ETABLISSEMENT'
    has_signature: bool,
    rpps: str,
    finess: str,
    typologie: str = "UNITAIRE" # 'URGENCE', 'UNITAIRE', 'ITERATIVE'
) -> Tuple[int, List[Dict[str, str]]]:
    """
    Moteur de règles CaspoScan - Conformité CPAM
    """
    score = 100
    alerts = []
    
    # 1. Signature Check (Toujours obligatoire)
    if not has_signature:
        score -= 40
        alerts.append({"type": "vigilance", "msg": "Signature manquante"})
        
    # 2. Identification RPPS / FINESS
    has_rpps = validate_rpps_format(rpps)
    has_finess = validate_finess_format(finess)
    
    # Règle Établissement/Urgence (CHU/SAMU)
    # Si Urgence ou FINESS présent ou Type Etablissement -> On est en mode Structure
    is_structure = (prescripteur_type == 'ETABLISSEMENT') or has_finess or (typologie == "URGENCE")
    
    if is_structure:
        # Mode Structure (Hôpitaux, SAMU, Cliniques)
        # Pas de pénalité pour RPPS ou FINESS car médecins salariés
        pass
    else:
        # Mode Libéral / Individuel
        if not has_rpps:
            score -= 30
            alerts.append({"type": "vigilance", "msg": "RPPS manquant ou format invalide"})
        
        # Pénalité cachet (ni RPPS ni FINESS du prescripteur)
        if not (has_rpps or has_finess):
            score -= 10
    
    score = max(0, score)
    return score, alerts
