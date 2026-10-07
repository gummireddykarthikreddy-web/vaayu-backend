from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import date, datetime
import uuid

# --- 1. The Patient Profile ---
class PatientProfile(BaseModel):
    # Generating a unique ID for every user automatically
    patient_id: str = Field(default_factory=lambda: f"VAAYU-{uuid.uuid4().hex[:8].upper()}")
    full_name: str
    date_of_birth: date
    blood_group: str
    contact_number: str
    emergency_contact: str
    # We can eventually link this to Aadhaar or ABHA verification flows
    is_identity_verified: bool = False 
    created_at: datetime = Field(default_factory=datetime.now)

# --- 2. The Medical Vault (Historical Data) ---
class PastSurgery(BaseModel):
    procedure_name: str
    date_of_surgery: date
    surgeon_notes: Optional[str] = None
    complications: Optional[str] = None

class MedicalHistory(BaseModel):
    patient_id: str
    chronic_conditions: List[str] = []
    past_surgeries: List[PastSurgery] = []
    active_prescriptions: List[str] = []
    known_allergies: List[str] = []

# --- 3. The Daily Lab Report ---
class DailyLabReport(BaseModel):
    report_id: str = Field(default_factory=lambda: uuid.uuid4().hex)
    patient_id: str
    date_submitted: date = Field(default_factory=date.today)
    
    # Specific Lab Metrics you requested
    hemoglobin_level: float # g/dL
    cbc_wbc_count: float # cells/mcL
    lipid_ldl: float # mg/dL
    lipid_hdl: float # mg/dL
    fasting_blood_sugar: float # mg/dL
    lft_sgpt: float # U/L (Liver)
    kft_creatinine: float # mg/dL (Kidney)
    
    # The AI will generate these after analyzing the metrics above
    calculated_recovery_rate: Optional[float] = None
    ai_diet_recommendation_id: Optional[str] = None