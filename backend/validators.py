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
    
    # Implicit "Cachet" presence logic
    has_cachet = has_rpps or has_finess
    
    if is_etablissement:
        # "quand c'est une structure pas besoin de finess"
        # Logic from doc seems to apply no penalty for structure specific missing IDs?
        # Re-reading: 
        # "Nous ne pénalisons plus l'absence de FINESS pour les structures."
        # Does it imply we check anything else? 
        # The code block for isEtablissement was empty in the source.
        pass
    else:
        # Individual Prescriber
        if not has_rpps:
            score -= 30
            alerts.append({"type": "vigilance", "msg": "RPPS manquant ou format invalide"})
        
        if not has_cachet:
            score -= 10
            # Note: "We don't alert explicitly for cachet missing if RPPS is also missing"
    
    score = max(0, score)
    
    return score, alerts
