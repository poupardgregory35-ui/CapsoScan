from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from models import ScanResponse, Validation
from validators import calculate_compliance_score
from datetime import datetime
import uuid
from typing import List

app = FastAPI(title="CapsoScan API", version="1.0.0")

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
    file: UploadFile = File(...)
):
    # Simulation OCR (still simulated)
    scan_id = f"PDA-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    timestamp = datetime.now()
    
    # Use provided values or defaults
    rpps_val = rpps if rpps else "10002030405"
    finess_val = finess if finess else "350000123"
    has_signature = True # Simulated correct signature
    
    score, alerts = calculate_compliance_score(
        prescripteur_type="INDIVIDUEL", # Default for now
        has_signature=has_signature,
        rpps=rpps_val,
        finess=finess_val
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
