from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from models import ScanResponse, Validation
from validators import calculate_compliance_score
from datetime import datetime
import uuid
from typing import List, Optional, Any

app = FastAPI(title="CaspoScan API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://capsoscan-frontend.vercel.app",
        "https://*.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.post("/scan/pda", response_model=ScanResponse)
async def scan_pda(
    rpps: Optional[str] = Form(None),
    finess: Optional[str] = Form(None),
    typologie: Optional[str] = Form("UNITAIRE"),
    structure_type: Optional[str] = Form("liberal"), # "liberal" ou "etablissement"
    hasSignature: Optional[str] = Form("true"),
    file: UploadFile = File(...)
):
    # Simulation OCR
    scan_id = f"PDA-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    timestamp = datetime.now()
    
    rpps_val = rpps if rpps else ""
    finess_val = finess if finess else ""
    
    # Conversion du string "true"/"false" en boolean Python
    has_sig_bool = str(hasSignature).lower() == "true"
    
    score, alerts = calculate_compliance_score(
        structure_type=structure_type,
        has_signature=has_sig_bool,
        rpps=rpps_val,
        finess=finess_val,
        typologie=typologie
    )
    
    statut = "VALID" if score >= 80 else "INVALID"
    
    return ScanResponse(
        scan_id=scan_id,
        timestamp=timestamp,
        rpps=rpps_val,
        finess=finess_val,
        code_acte="VSL",
        score_confiance=score / 100.0,
        qualite_image="HIGH",
        statut=statut,
        validations=[
            Validation(
                rule=alert.get("type", "unknown").upper(),
                status=False, 
                message=alert.get("msg", "Alert")
            ) for alert in alerts
        ]
    )

@app.post("/scan/vitale", response_model=ScanResponse)
async def scan_vitale(file: UploadFile = File(...)):
     return ScanResponse(
        scan_id=f"VIT-{datetime.now().strftime('%Y%m%d%H%M%S')}",
        timestamp=datetime.now(),
        rpps=None,
        finess=None,
        code_acte=None,
        score_confiance=0.99,
        qualite_image="HIGH",
        statut="VALID",
        validations=[]
    )

@app.post("/scan/batch")
async def scan_batch(files: List[UploadFile] = File(...)):
    return {"batch_id": str(uuid.uuid4()), "files_processed": len(files)}
