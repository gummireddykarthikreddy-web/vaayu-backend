from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
import random
import os
import google.generativeai as genai

# --- APP SETUP ---
app = FastAPI()

# Allow your frontend to talk to your backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini AI (Make sure your environment variable is set on Render!)
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", "YOUR_API_KEY_HERE"))
model = genai.GenerativeModel('gemini-1.5-flash')

# --- DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('vaayu.db')
    cursor = conn.cursor()
    
    # 1. Patients Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            patient_id TEXT PRIMARY KEY,
            full_name TEXT,
            date_of_birth TEXT,
            blood_group TEXT,
            contact_number TEXT,
            emergency_contact TEXT
        )
    ''')
    
    # 2. Medical Records Table (for the Vault)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medical_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            record_type TEXT,
            description TEXT,
            date TEXT,
            FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
        )
    ''')

    # 3. Daily Lab Results Table (PHASE 1)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS lab_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            report_date TEXT,
            hemoglobin REAL,
            fasting_blood_sugar REAL,
            lipid_profile_ldl REAL,
            lft_sgpt REAL,
            kft_creatinine REAL,
            cbc_wbc REAL,
            FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
        )
    ''')
    
    conn.commit()
    conn.close()

# Run database setup on startup
init_db()


# --- DATA MODELS ---
class PatientRegister(BaseModel):
    full_name: str
    date_of_birth: str
    blood_group: str
    contact_number: str
    emergency_contact: str

class MedicalRecord(BaseModel):
    patient_id: str
    record_type: str
    description: str
    date: str

class DailyLabReport(BaseModel):
    patient_id: str
    report_date: str
    hemoglobin: float
    fasting_blood_sugar: float
    lipid_profile_ldl: float
    lft_sgpt: float
    kft_creatinine: float
    cbc_wbc: float


# --- API ENDPOINTS ---

@app.get("/")
def read_root():
    return {"message": "Welcome to the Vaayu Backend System!"}

# 1. Registration Endpoint
@app.post("/api/register")
async def register_patient(patient: PatientRegister):
    try:
        conn = sqlite3.connect('vaayu.db')
        cursor = conn.cursor()
        
        # Generate a unique ID (e.g., VAAYU-48291)
        patient_id = f"VAAYU-{random.randint(10000, 99999)}"
        
        cursor.execute('''
            INSERT INTO patients (patient_id, full_name, date_of_birth, blood_group, contact_number, emergency_contact)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (patient_id, patient.full_name, patient.date_of_birth, patient.blood_group, patient.contact_number, patient.emergency_contact))
        
        conn.commit()
        conn.close()
        
        return {"status": "success", "patient_id": patient_id}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# 2. Analytics Dashboard Endpoint
@app.get("/api/statistics")
async def get_statistics():
    try:
        conn = sqlite3.connect('vaayu.db')
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM patients")
        total_patients = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM medical_records")
        total_records = cursor.fetchone()[0]
        
        cursor.execute("SELECT blood_group, COUNT(*) FROM patients GROUP BY blood_group")
        blood_group_counts = [{"bloodGroup": row[0], "count": row[1]} for row in cursor.fetchall()]
        
        conn.close()
        return {
            "status": "success",
            "total_patients": total_patients,
            "total_records": total_records,
            "blood_group_distribution": blood_group_counts
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# 3. Patient Vault & AI Summarizer
@app.get("/api/patient/{patient_id}")
async def get_patient_vault(patient_id: str):
    try:
        conn = sqlite3.connect('vaayu.db')
        cursor = conn.cursor()
        
        # Get patient details
        cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
        patient = cursor.fetchone()
        
        if not patient:
            return {"status": "error", "message": "Patient not found"}
            
        # Get medical records
        cursor.execute("SELECT record_type, description, date FROM medical_records WHERE patient_id = ?", (patient_id,))
        records = [{"type": row[0], "description": row[1], "date": row[2]} for row in cursor.fetchall()]
        
        # Use AI to generate a clinical summary
        prompt = f"Act as a chief medical officer. Summarize this patient's history in 2 short, professional sentences. Name: {patient[1]}, Blood Group: {patient[3]}. Records: {records}"
        ai_response = model.generate_content(prompt)
        ai_summary = ai_response.text
        
        conn.close()
        
        return {
            "status": "success",
            "patient_info": {
                "id": patient[0],
                "name": patient[1],
                "dob": patient[2],
                "blood_group": patient[3]
            },
            "records": records,
            "ai_summary": ai_summary
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

# 4. Add Medical Record to Vault
@app.post("/api/records/add")
async def add_medical_record(record: MedicalRecord):
    try:
        conn = sqlite3.connect('vaayu.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO medical_records (patient_id, record_type, description, date)
            VALUES (?, ?, ?, ?)
        ''', (record.patient_id, record.record_type, record.description, record.date))
        
        conn.commit()
        conn.close()
        return {"status": "success", "message": "Record added securely."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# --- PHASE 1: NEW LAB & VITALS ENDPOINTS ---

# 5. Save Daily Lab Report
@app.post("/api/labs/add")
async def add_lab_report(report: DailyLabReport):
    try:
        conn = sqlite3.connect('vaayu.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO lab_results 
            (patient_id, report_date, hemoglobin, fasting_blood_sugar, lipid_profile_ldl, lft_sgpt, kft_creatinine, cbc_wbc)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            report.patient_id, report.report_date, report.hemoglobin, 
            report.fasting_blood_sugar, report.lipid_profile_ldl, 
            report.lft_sgpt, report.kft_creatinine, report.cbc_wbc
        ))
        
        conn.commit()
        conn.close()
        return {"status": "success", "message": "Daily lab report saved to Vaayu."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# 6. Get Lab History for Charts
@app.get("/api/labs/{patient_id}")
async def get_patient_labs(patient_id: str):
    try:
        conn = sqlite3.connect('vaayu.db')
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT report_date, hemoglobin, fasting_blood_sugar, lipid_profile_ldl, lft_sgpt, kft_creatinine, cbc_wbc 
            FROM lab_results 
            WHERE patient_id = ?
            ORDER BY report_date ASC
        ''', (patient_id,))
        
        rows = cursor.fetchall()
        conn.close()
        
        history = []
        for row in rows:
            history.append({
                "date": row[0],
                "hemoglobin": row[1],
                "fasting_blood_sugar": row[2],
                "lipid_profile_ldl": row[3],
                "lft_sgpt": row[4],
                "kft_creatinine": row[5],
                "cbc_wbc": row[6]
            })
            
        return {"status": "success", "data": history}
    except Exception as e:
        return {"status": "error", "message": str(e)}