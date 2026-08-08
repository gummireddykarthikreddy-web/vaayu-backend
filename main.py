from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uuid
import sqlite3
from datetime import datetime
import os

# Import the Google AI library
import google.generativeai as genai

# ==========================================
# 🔒 SECURE WAY: Pull the key from Render's environment!
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# ==========================================

# Only configure if the key exists (prevents crashes if missing)
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Use the latest, fastest model
ai_model = genai.GenerativeModel('gemini-3.5-flash') 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect("vaayu.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id TEXT PRIMARY KEY,
            full_name TEXT,
            date_of_birth TEXT,
            blood_group TEXT,
            contact_number TEXT,
            emergency_contact TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medical_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            record_type TEXT,
            record_details TEXT,
            date_added TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# --- MODELS ---
class PatientProfile(BaseModel):
    full_name: str
    date_of_birth: str
    blood_group: str
    contact_number: str
    emergency_contact: str

class MedicalRecord(BaseModel):
    record_type: str
    record_details: str

# --- ENDPOINTS ---
@app.post("/api/register")
def register_patient(profile: PatientProfile):
    unique_id = f"VAAYU-{uuid.uuid4().hex[:8].upper()}"
    conn = sqlite3.connect("vaayu.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO patients (patient_id, full_name, date_of_birth, blood_group, contact_number, emergency_contact)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (unique_id, profile.full_name, profile.date_of_birth, profile.blood_group, profile.contact_number, profile.emergency_contact))
    conn.commit()
    conn.close()
    return {"status": "success", "patient_id": unique_id}

@app.post("/api/patient/{patient_id}/records")
def add_medical_record(patient_id: str, record: MedicalRecord):
    conn = sqlite3.connect("vaayu.db")
    cursor = conn.cursor()
    date_added = datetime.today().strftime("%b %d, %Y") 
    cursor.execute("""
        INSERT INTO medical_records (patient_id, record_type, record_details, date_added)
        VALUES (?, ?, ?, ?)
    """, (patient_id.upper(), record.record_type, record.record_details, date_added))
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Record added."}

@app.delete("/api/records/{record_id}")
def delete_medical_record(record_id: int):
    conn = sqlite3.connect("vaayu.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM medical_records WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Record deleted."}

@app.get("/api/patient/{patient_id}")
def get_patient_vault(patient_id: str):
    conn = sqlite3.connect("vaayu.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT full_name, date_of_birth, blood_group FROM patients WHERE patient_id = ?", (patient_id.upper(),))
    row = cursor.fetchone()
    
    if not row:
        conn.close()
        return {"status": "error", "message": "Patient not found."}

    cursor.execute("SELECT id, record_type, record_details, date_added FROM medical_records WHERE patient_id = ?", (patient_id.upper(),))
    records = cursor.fetchall()
    conn.close()

    history = {
        "chronic_conditions": [],
        "past_surgeries": [],
        "active_prescriptions": [],
        "allergies": []
    }

    for r_id, r_type, details, date_added in records:
        if r_type == "allergy":
            history["allergies"].append({"id": r_id, "detail": details, "date": date_added})
        elif r_type == "prescription":
            history["active_prescriptions"].append({"id": r_id, "detail": details, "date": date_added})
        elif r_type == "surgery":
            history["past_surgeries"].append({"id": r_id, "procedure": details, "date": date_added, "notes": "Added via Portal"})

    try:
        dob = datetime.strptime(row[1], "%Y-%m-%d")
        today = datetime.today()
        age = str(today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)))
    except:
        age = "N/A"

    return {
        "status": "success",
        "patient_id": patient_id.upper(),
        "profile": {
            "name": row[0],
            "dob": row[1],
            "blood_group": row[2],
            "age": age
        },
        "history": history
    }

# --- AI AGENT ENDPOINT ---
@app.get("/api/patient/{patient_id}/summary")
def generate_ai_summary(patient_id: str):
    # Safety check: Is the API key loaded from the environment?
    if not GEMINI_API_KEY:
        return {"status": "error", "message": "API key is missing in the cloud environment."}

    # 1. Fetch the patient data using our existing function
    patient_data = get_patient_vault(patient_id)
    
    if patient_data.get("status") == "error":
        return {"status": "error", "message": "Cannot generate summary for unknown patient."}

    # 2. Build the Prompt (giving the AI its instructions)
    prompt = f"""
    You are a highly advanced AI clinical assistant for the Vaayu medical portal. 
    Analyze the following patient data and medical history: 
    {patient_data}
    
    Provide a concise, professional 3-bullet point health summary for the doctor. 
    Explicitly flag any potential risks if they have allergies, or simply state their current status.
    Do not use markdown bolding in your response, keep it plain text.
    """

    # 3. Ask Gemini to generate the response
    try:
        response = ai_model.generate_content(prompt)
        return {"status": "success", "ai_summary": response.text}
    except Exception as e:
        return {"status": "error", "message": str(e)}from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uuid
import sqlite3
from datetime import datetime
import os

# Import the Google AI library
import google.generativeai as genai

# ==========================================
# 🔒 SECURE WAY: Pull the key from Render's environment!
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
# ==========================================

# Only configure if the key exists (prevents crashes if missing)
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Use the latest, fastest model
ai_model = genai.GenerativeModel('gemini-3.5-flash') 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect("vaayu.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS patients (
            patient_id TEXT PRIMARY KEY,
            full_name TEXT,
            date_of_birth TEXT,
            blood_group TEXT,
            contact_number TEXT,
            emergency_contact TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medical_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            record_type TEXT,
            record_details TEXT,
            date_added TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# --- MODELS ---
class PatientProfile(BaseModel):
    full_name: str
    date_of_birth: str
    blood_group: str
    contact_number: str
    emergency_contact: str

class MedicalRecord(BaseModel):
    record_type: str
    record_details: str

# --- ENDPOINTS ---
@app.post("/api/register")
def register_patient(profile: PatientProfile):
    unique_id = f"VAAYU-{uuid.uuid4().hex[:8].upper()}"
    conn = sqlite3.connect("vaayu.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO patients (patient_id, full_name, date_of_birth, blood_group, contact_number, emergency_contact)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (unique_id, profile.full_name, profile.date_of_birth, profile.blood_group, profile.contact_number, profile.emergency_contact))
    conn.commit()
    conn.close()
    return {"status": "success", "patient_id": unique_id}

@app.post("/api/patient/{patient_id}/records")
def add_medical_record(patient_id: str, record: MedicalRecord):
    conn = sqlite3.connect("vaayu.db")
    cursor = conn.cursor()
    date_added = datetime.today().strftime("%b %d, %Y") 
    cursor.execute("""
        INSERT INTO medical_records (patient_id, record_type, record_details, date_added)
        VALUES (?, ?, ?, ?)
    """, (patient_id.upper(), record.record_type, record.record_details, date_added))
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Record added."}

@app.delete("/api/records/{record_id}")
def delete_medical_record(record_id: int):
    conn = sqlite3.connect("vaayu.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM medical_records WHERE id = ?", (record_id,))
    conn.commit()
    conn.close()
    return {"status": "success", "message": "Record deleted."}

@app.get("/api/patient/{patient_id}")
def get_patient_vault(patient_id: str):
    conn = sqlite3.connect("vaayu.db")
    cursor = conn.cursor()
    
    cursor.execute("SELECT full_name, date_of_birth, blood_group FROM patients WHERE patient_id = ?", (patient_id.upper(),))
    row = cursor.fetchone()
    
    if not row:
        conn.close()
        return {"status": "error", "message": "Patient not found."}

    cursor.execute("SELECT id, record_type, record_details, date_added FROM medical_records WHERE patient_id = ?", (patient_id.upper(),))
    records = cursor.fetchall()
    conn.close()

    history = {
        "chronic_conditions": [],
        "past_surgeries": [],
        "active_prescriptions": [],
        "allergies": []
    }

    for r_id, r_type, details, date_added in records:
        if r_type == "allergy":
            history["allergies"].append({"id": r_id, "detail": details, "date": date_added})
        elif r_type == "prescription":
            history["active_prescriptions"].append({"id": r_id, "detail": details, "date": date_added})
        elif r_type == "surgery":
            history["past_surgeries"].append({"id": r_id, "procedure": details, "date": date_added, "notes": "Added via Portal"})

    try:
        dob = datetime.strptime(row[1], "%Y-%m-%d")
        today = datetime.today()
        age = str(today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day)))
    except:
        age = "N/A"

    return {
        "status": "success",
        "patient_id": patient_id.upper(),
        "profile": {
            "name": row[0],
            "dob": row[1],
            "blood_group": row[2],
            "age": age
        },
        "history": history
    }

# --- AI AGENT ENDPOINT ---
@app.get("/api/patient/{patient_id}/summary")
def generate_ai_summary(patient_id: str):
    # Safety check: Is the API key loaded from the environment?
    if not GEMINI_API_KEY:
        return {"status": "error", "message": "API key is missing in the cloud environment."}

    # 1. Fetch the patient data using our existing function
    patient_data = get_patient_vault(patient_id)
    
    if patient_data.get("status") == "error":
        return {"status": "error", "message": "Cannot generate summary for unknown patient."}

    # 2. Build the Prompt (giving the AI its instructions)
    prompt = f"""
    You are a highly advanced AI clinical assistant for the Vaayu medical portal. 
    Analyze the following patient data and medical history: 
    {patient_data}
    
    Provide a concise, professional 3-bullet point health summary for the doctor. 
    Explicitly flag any potential risks if they have allergies, or simply state their current status.
    Do not use markdown bolding in your response, keep it plain text.
    """

    # 3. Ask Gemini to generate the response
    try:
        response = ai_model.generate_content(prompt)
        return {"status": "success", "ai_summary": response.text}
    except Exception as e:
        return {"status": "error", "message": str(e)}