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
    finess: str
) -> Tuple[int, List[Dict[str, str]]]:
    """
    Implements CPAM compliance rules extracted from frontend logic.
    Returns (score, alerts)
    """
    score = 100
    alerts = []
    
    is_etablissement = (prescripteur_type == 'ETABLISSEMENT')
    
    # 1. Signature Check
    if not has_signature:
        score -= 40
        alerts.append({"type": "vigilance", "msg": "Signature manquante"})
        
    # 2. RPPS / FINESS Checks
    has_rpps = validate_rpps_format(rpps)
    has_finess = validate_finess_format(finess)
    
    # "Si le finess est présent (établissement), pas besoin de RPPS"
    is_etablissement = is_etablissement or has_finess

    if is_etablissement:
        # Structure mode: No penalty for missing RPPS
        pass
    else:
        # Individual Prescriber
        if not has_rpps:
            score -= 30
            alerts.append({"type": "vigilance", "msg": "RPPS manquant ou format invalide"})
        
        # Cachet absent penalty (ni RPPS ni FINESS)
        if not (has_rpps or has_finess):
            score -= 10
    
    score = max(0, score)
    
    return score, alerts
