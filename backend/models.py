from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Validation(BaseModel):
    rule: str
    status: bool
    message: str

class ScanResponse(BaseModel):
    scan_id: str
    timestamp: datetime
    rpps: Optional[str] = None
    finess: Optional[str] = None
    code_acte: Optional[str] = None
    score_confiance: float
    qualite_image: str
    statut: str
    validations: List[Validation] = []
