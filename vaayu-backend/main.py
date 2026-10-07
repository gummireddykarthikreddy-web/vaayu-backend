import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3
import random
import os
import datetime
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

def init_db():
    conn = sqlite3.connect('vaayu.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            patient_id TEXT PRIMARY KEY,
            full_name TEXT,
            date_of_birth TEXT,
            blood_group TEXT,
            contact_number TEXT,
            emergency_contact TEXT,
            address TEXT,
            nearby_post_office TEXT
        )
    ''')
    
    try:
        cursor.execute("ALTER TABLE patients ADD COLUMN address TEXT")
        cursor.execute("ALTER TABLE patients ADD COLUMN nearby_post_office TEXT")
    except:
        pass
        
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
            cbc_rbc REAL,
            cbc_platelets REAL,
            lipid_profile_hdl REAL,
            lipid_profile_triglycerides REAL,
            lft_sgot REAL,
            lft_bilirubin REAL,
            kft_urea REAL,
            post_blood_sugar REAL,
            inflammatory_crp REAL,
            inflammatory_esr REAL,
            FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
        )
    ''')
    
    try:
        cursor.execute("ALTER TABLE lab_results ADD COLUMN post_blood_sugar REAL")
        cursor.execute("ALTER TABLE lab_results ADD COLUMN inflammatory_crp REAL")
        cursor.execute("ALTER TABLE lab_results ADD COLUMN inflammatory_esr REAL")
    except:
        pass
        
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS food_orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id TEXT,
            items_summary TEXT,
            total_price REAL,
            delivery_address TEXT,
            status TEXT,
            order_date TEXT,
            FOREIGN KEY(patient_id) REFERENCES patients(patient_id)
        )
    ''')
    
    cursor.execute("SELECT * FROM patients WHERE patient_id = 'VAAYU-77572'")
    if not cursor.fetchone():
        cursor.execute('''
            INSERT INTO patients (patient_id, full_name, date_of_birth, blood_group, contact_number, emergency_contact, address, nearby_post_office)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', ("VAAYU-77572", "Arjun Sharma", "1988-05-14", "O+", "9876543210", "9123456789", "H.No 4-12, Gandhi Nagar, Guntur, Andhra Pradesh - 522001", "Guntur Head Post Office, Arundelpet, Guntur - 522002"))
        
        cursor.execute('''
            INSERT INTO lab_results 
            (patient_id, report_date, hemoglobin, fasting_blood_sugar, lipid_profile_ldl, lft_sgpt, kft_creatinine, cbc_wbc, cbc_rbc, cbc_platelets, lipid_profile_hdl, lipid_profile_triglycerides, lft_sgot, lft_bilirubin, kft_urea, post_blood_sugar, inflammatory_crp, inflammatory_esr)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', ("VAAYU-77572", "2026-09-01", 10.2, 168.0, 145.0, 64.0, 1.4, 12000.0, 4.0, 140000.0, 35.0, 200.0, 50.0, 1.5, 25.0, 220.0, 8.5, 35.0))
        
        cursor.execute('''
            INSERT INTO lab_results 
            (patient_id, report_date, hemoglobin, fasting_blood_sugar, lipid_profile_ldl, lft_sgpt, kft_creatinine, cbc_wbc, cbc_rbc, cbc_platelets, lipid_profile_hdl, lipid_profile_triglycerides, lft_sgot, lft_bilirubin, kft_urea, post_blood_sugar, inflammatory_crp, inflammatory_esr)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', ("VAAYU-77572", "2026-09-28", 11.9, 132.0, 118.0, 44.0, 1.1, 8000.0, 4.6, 165000.0, 42.0, 170.0, 35.0, 1.0, 18.0, 150.0, 3.2, 22.0))
        
        cursor.execute("INSERT INTO medical_records (patient_id, record_type, description, date) VALUES (?, ?, ?, ?)", ("VAAYU-77572", "prescription", "Metformin 500mg OD for Sugar. Iron supplements for Hb.", "2026-09-28"))
        cursor.execute("INSERT INTO medical_records (patient_id, record_type, description, date) VALUES (?, ?, ?, ?)", ("VAAYU-77572", "prescription", "Amoxicillin 500mg for infection.", "2026-08-15"))
        cursor.execute("INSERT INTO medical_records (patient_id, record_type, description, date) VALUES (?, ?, ?, ?)", ("VAAYU-77572", "prescription", "Paracetamol 500mg SOS.", "2026-07-10"))
        cursor.execute("INSERT INTO medical_records (patient_id, record_type, description, date) VALUES (?, ?, ?, ?)", ("VAAYU-77572", "surgery", "Appendectomy (2015)", "2015-06-10"))
        cursor.execute("INSERT INTO medical_records (patient_id, record_type, description, date) VALUES (?, ?, ?, ?)", ("VAAYU-77572", "allergy", "Penicillin", "2020-01-01"))

    conn.commit()
    conn.close()

init_db()

class PatientRegister(BaseModel):
    full_name: str
    date_of_birth: str
    blood_group: str
    contact_number: str
    emergency_contact: str
    address: str = ""
    nearby_post_office: str = ""

class MedicalRecord(BaseModel):
    patient_id: str
    record_type: str
    description: str
    date: str

class MedicalRecordDirect(BaseModel):
    record_type: str
    record_details: str

class DailyLabReport(BaseModel):
    patient_id: str
    report_date: str
    hemoglobin: float
    fasting_blood_sugar: float
    lipid_profile_ldl: float
    lft_sgpt: float
    kft_creatinine: float
    cbc_wbc: float
    cbc_rbc: float = 0.0
    cbc_platelets: float = 0.0
    lipid_profile_hdl: float = 0.0
    lipid_profile_triglycerides: float = 0.0
    lft_sgot: float = 0.0
    lft_bilirubin: float = 0.0
    kft_urea: float = 0.0
    post_blood_sugar: float = 0.0
    inflammatory_crp: float = 0.0
    inflammatory_esr: float = 0.0

class FoodOrderCreate(BaseModel):
    patient_id: str
    items_summary: str
    total_price: float
    delivery_address: str


def calculate_recovery_and_status(lab_rows):
    if len(lab_rows) < 2:
        return {
            "recovery_rate": 0,
            "health_status": "Insufficient Data",
            "progress_breakdown": {},
            "ring_sub_metrics": {}
        }
    
    sorted_labs = sorted(lab_rows, key=lambda x: x['report_date'])
    prev = sorted_labs[-2]
    curr = sorted_labs[-1]
    
    def calc_score(p_val, c_val, t_min, t_max):
        def dist(val):
            if val < t_min: return t_min - val
            if val > t_max: return val - t_max
            return 0
        p_dist = dist(p_val)
        c_dist = dist(c_val)
        if c_dist == 0: return 1.0, "Optimal / Stable"
        if c_dist < p_dist: return 0.78, "Improved"
        if c_dist > p_dist: return 0.25, "Worsened"
        return 0.5, "No Change"
            
    metrics = [
        ("hemoglobin", 13.8, 17.2),
        ("fasting_blood_sugar", 70, 100),
        ("post_blood_sugar", 70, 140),
        ("lipid_profile_ldl", 0, 100),
        ("lft_sgpt", 7, 56),
        ("kft_creatinine", 0.7, 1.3),
        ("inflammatory_crp", 0, 3.0),
        ("inflammatory_esr", 0, 20)
    ]
    
    total_score = 0
    breakdown = {}
    for m, t_min, t_max in metrics:
        p_val = prev.get(m, 0)
        c_val = curr.get(m, 0)
        score, status = calc_score(p_val, c_val, t_min, t_max)
        total_score += score
        breakdown[m] = status
        
    recovery_rate = (total_score / len(metrics)) * 100
    if recovery_rate >= 80: health_status = "Recovering Steadily"
    elif recovery_rate >= 40: health_status = "Stable (Moderate)"
    else: health_status = "Critical Attention Needed"
    
    # Ring Sub Metrics
    ring_sub_metrics = {
        "post_blood_sugar": {"value": curr.get("post_blood_sugar", 0), "status": "High" if curr.get("post_blood_sugar", 0) > 140 else "Normal"},
        "cbc_summary": {"value": f"WBC: {curr.get('cbc_wbc',0)} | RBC: {curr.get('cbc_rbc',0)} | PLT: {curr.get('cbc_platelets',0)}", "status": "Normal" if curr.get('cbc_platelets',0) >= 150000 else "Low"},
        "lft_summary": {"value": f"SGPT: {curr.get('lft_sgpt',0)} | SGOT: {curr.get('lft_sgot',0)} | BIL: {curr.get('lft_bilirubin',0)}", "status": "Normal" if curr.get('lft_sgpt',0) <= 56 else "High"},
        "inflammatory_markers": {"value": f"CRP: {curr.get('inflammatory_crp',0)} | ESR: {curr.get('inflammatory_esr',0)}", "status": "Normal" if curr.get('inflammatory_crp',0) <= 3.0 else "High"}
    }
        
    return {
        "recovery_rate": round(recovery_rate, 2),
        "health_status": health_status,
        "progress_breakdown": breakdown,
        "ring_sub_metrics": ring_sub_metrics
    }

def get_pre_surgery_alerts(records, latest_lab):
    alerts = []
    measures = []
    for r in records:
        rtype = r["type"].lower()
        desc = r["description"]
        if rtype == "allergy":
            alerts.append(f"Allergy Alert: Patient is allergic to {desc}")
            if "penicillin" in desc.lower():
                measures.append("Administer non-beta-lactam prophylactic antibiotics 60 mins prior to incision (due to Penicillin Allergy)")
        elif rtype in ["surgery", "chronic_condition"]:
            alerts.append(f"History Alert ({r['type']}): {desc}")
            if "appendectomy" in desc.lower():
                measures.append("Review adhesions from prior Appendectomy before laparoscopic trocar placement")
            
    if latest_lab:
        if latest_lab.get("fasting_blood_sugar", 0) > 140 or latest_lab.get("post_blood_sugar", 0) > 180:
            alerts.append("High Blood Sugar: Increased risk of infection.")
            measures.append("Stabilize glycemic levels with sliding-scale insulin protocol before anesthesia")
        if latest_lab.get("hemoglobin", 0) > 0 and latest_lab.get("hemoglobin", 0) < 12:
            alerts.append("Low Hemoglobin: Increased risk of bleeding.")
            measures.append("Cross-match 2 units of Packed RBCs due to borderline Hemoglobin")
            
    return alerts, measures

def get_care_plan(patient, records, latest_lab):
    summary = f"Patient {patient['full_name']} (Blood Group {patient['blood_group']}) has {len(records)} medical records."
    diet_plan = []
    preventive = ["Maintain hand hygiene", "Drink boiled or RO water daily"]
    unhygienic = ["Street foods", "Reheated cooking oils", "Uncovered cut fruits"]
    exercise = ["20-min brisk morning walk", "Pranayama/Anulom Vilom breathing"]
    
    if latest_lab:
        if latest_lab.get("hemoglobin", 0) > 0 and latest_lab.get("hemoglobin", 0) < 13.8:
            diet_plan.append("Iron-rich Palak, Ragi, and Dates")
            preventive.append("Avoid physical overexertion")
            exercise.append("Light resistance mobility")
        if latest_lab.get("post_blood_sugar", 0) > 140:
            diet_plan.append("Low-GI Millets and Methi")
            unhygienic.append("Sugary snacks and sweetened beverages")
            exercise.append("post-meal 10-min walk for Post Blood Sugar control")
        if latest_lab.get("lft_sgpt", 0) > 56:
            diet_plan.append("Zero-oil steamed foods")
            unhygienic.append("Deep fried items")
            
    if not diet_plan:
        diet_plan.append("Balanced Indian home-cooked meals")
        
    return {
        "clinical_summary": summary,
        "prior_diet_plan": diet_plan,
        "preventive_measures": preventive,
        "unhygienic_foods_to_avoid": unhygienic,
        "daily_exercise_plan": exercise
    }

def run_lab_delta_hazard_agent(lab_rows):
    if len(lab_rows) < 2: return []
    sorted_labs = sorted(lab_rows, key=lambda x: x['report_date'])
    prev = sorted_labs[-2]
    curr = sorted_labs[-1]
    deltas = []
    
    metrics = [
        ("hemoglobin", "Hb", "g/dL", 13.8, 17.2, "Low Hb reduces oxygen transport to tissues."),
        ("post_blood_sugar", "Post Blood Sugar", "mg/dL", 70, 140, "Elevated Post Blood Sugar increases risk of microvascular damage and post-operative wound infection."),
        ("inflammatory_crp", "CRP", "mg/L", 0, 3.0, "High CRP indicates active inflammation/infection hazard."),
        ("cbc_platelets", "Platelets", "cells/mcL", 150000, 450000, "Low platelets increase bleeding hazard during surgery.")
    ]
    
    for m, name, unit, min_v, max_v, hazard in metrics:
        p = prev.get(m, 0)
        c = curr.get(m, 0)
        diff = c - p
        def dist(val):
            if val < min_v: return min_v - val
            if val > max_v: return val - max_v
            return 0
        
        p_dist = dist(p)
        c_dist = dist(c)
        
        trend = "Improved" if c_dist < p_dist else ("Worsened" if c_dist > p_dist else "Stable")
        if c_dist == 0 and p_dist == 0: trend = "Improved"
        
        sign = "+" if diff > 0 else ""
        
        if c_dist == 0:
            clinical_hazard = "Normal parameters."
        else:
            if trend == "Improved":
                if m == "hemoglobin":
                    clinical_hazard = "Mild residual anemia until reaching 13.8."
                elif m == "post_blood_sugar":
                    clinical_hazard = "Hazard of remaining slightly above normal range (< 140)."
                else:
                    clinical_hazard = hazard
            else:
                clinical_hazard = hazard

        deltas.append({
            "metric_name": name,
            "previous_value": p,
            "current_value": c,
            "delta": f"{sign}{round(diff,2)} {unit}",
            "trend": trend,
            "clinical_hazard": clinical_hazard
        })
    return deltas

@app.get("/")
def read_root():
    return {"message": "Welcome to the Vaayu Backend System!"}

@app.post("/api/register")
async def register_patient(patient: PatientRegister):
    try:
        conn = sqlite3.connect('vaayu.db')
        cursor = conn.cursor()
        patient_id = f"VAAYU-{random.randint(10000, 99999)}"
        cursor.execute('''
            INSERT INTO patients (patient_id, full_name, date_of_birth, blood_group, contact_number, emergency_contact, address, nearby_post_office)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (patient_id, patient.full_name, patient.date_of_birth, patient.blood_group, patient.contact_number, patient.emergency_contact, patient.address, patient.nearby_post_office))
        conn.commit()
        conn.close()
        return {"status": "success", "patient_id": patient_id}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/api/statistics")
@app.get("/api/analytics")
async def get_analytics():
    try:
        conn = sqlite3.connect('vaayu.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) as cnt FROM patients")
        total_patients = cursor.fetchone()["cnt"]
        
        cursor.execute("SELECT blood_group, COUNT(*) as cnt FROM patients GROUP BY blood_group")
        blood_group_counts = [{"bloodGroup": row["blood_group"], "count": row["cnt"]} for row in cursor.fetchall()]
        
        conn.close()
        
        # New Feature: Blood Units & Blood Banks
        available_blood_units = {
            "A+": 12, "A-": 4, "B+": 18, "B-": 2, "O+": 25, "O-": 8, "AB+": 6, "AB-": 1
        }
        nearby_blood_banks = [
            {"name": "Red Cross Society Blood Bank", "distance_km": 2.5, "address": "Station Road, City Center", "contact": "987650001", "available_groups": {"O+": 5, "B+": 10}},
            {"name": "Govt General Hospital Blood Bank", "distance_km": 4.0, "address": "Civil Hospital Campus", "contact": "987650002", "available_groups": {"A+": 12, "AB+": 3}},
            {"name": "Sanjeevani Lifeline Blood Bank", "distance_km": 5.2, "address": "Medical Square", "contact": "987650003", "available_groups": {"O-": 2, "A-": 1}},
            {"name": "Lions District Blood Center", "distance_km": 7.1, "address": "Lions Club Road", "contact": "987650004", "available_groups": {"B-": 3, "AB-": 1}}
        ]
        
        return {
            "status": "success",
            "total_patients": total_patients,
            "blood_group_distribution": blood_group_counts,
            "average_clinic_recovery_rate": 65.5,
            "available_blood_units": available_blood_units,
            "nearby_blood_banks": nearby_blood_banks
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/api/patient/{patient_id}")
async def get_patient_vault(patient_id: str):
    try:
        patient_id = patient_id.strip().upper()
        conn = sqlite3.connect('vaayu.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM patients WHERE patient_id = ?", (patient_id,))
        patient_row = cursor.fetchone()
        
        if not patient_row:
            return {"status": "error", "message": "Patient not found"}
            
        patient = dict(patient_row)
        
        cursor.execute("SELECT id, record_type, description, date FROM medical_records WHERE patient_id = ?", (patient_id,))
        records = [{"id": row["id"], "type": row["record_type"], "description": row["description"], "date": row["date"]} for row in cursor.fetchall()]
        
        cursor.execute("SELECT * FROM lab_results WHERE patient_id = ?", (patient_id,))
        lab_rows = [dict(row) for row in cursor.fetchall()]
        
        recovery_data = calculate_recovery_and_status(lab_rows)
        latest_lab = sorted(lab_rows, key=lambda x: x['report_date'])[-1] if lab_rows else None
        
        pre_surgery_alerts, doctor_pre_surgery_measures = get_pre_surgery_alerts(records, latest_lab)
        care_plan = get_care_plan(patient, records, latest_lab)
        lab_ai_agent = run_lab_delta_hazard_agent(lab_rows)
            
        conn.close()
        
        return {
            "status": "success",
            "patient_info": {
                "id": patient["patient_id"],
                "name": patient["full_name"],
                "dob": patient["date_of_birth"],
                "blood_group": patient["blood_group"],
                "health_status": recovery_data["health_status"],
                "address": patient.get("address", ""),
                "nearby_post_office": patient.get("nearby_post_office", ""),
                "contact_number": patient.get("contact_number", "")
            },
            "records": records,
            "recovery_insights": recovery_data,
            "pre_surgery_alerts": pre_surgery_alerts,
            "doctor_pre_surgery_measures": doctor_pre_surgery_measures,
            "care_plan": care_plan,
            "lab_ai_agent": lab_ai_agent
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

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

@app.post("/api/patient/{patient_id}/records")
async def add_medical_record_direct(patient_id: str, payload: MedicalRecordDirect):
    try:
        conn = sqlite3.connect('vaayu.db')
        cursor = conn.cursor()
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        cursor.execute('''
            INSERT INTO medical_records (patient_id, record_type, description, date)
            VALUES (?, ?, ?, ?)
        ''', (patient_id, payload.record_type, payload.record_details, date_str))
        conn.commit()
        conn.close()
        return {"status": "success", "message": "Record added securely."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.delete("/api/records/{record_id}")
async def delete_medical_record(record_id: int):
    try:
        conn = sqlite3.connect('vaayu.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM medical_records WHERE id = ?", (record_id,))
        conn.commit()
        conn.close()
        return {"status": "success", "message": "Record deleted securely."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/labs/add")
async def add_lab_report(report: DailyLabReport):
    try:
        conn = sqlite3.connect('vaayu.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO lab_results 
            (patient_id, report_date, hemoglobin, fasting_blood_sugar, lipid_profile_ldl, lft_sgpt, kft_creatinine, cbc_wbc, cbc_rbc, cbc_platelets, lipid_profile_hdl, lipid_profile_triglycerides, lft_sgot, lft_bilirubin, kft_urea, post_blood_sugar, inflammatory_crp, inflammatory_esr)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            report.patient_id, report.report_date, report.hemoglobin, 
            report.fasting_blood_sugar, report.lipid_profile_ldl, 
            report.lft_sgpt, report.kft_creatinine, report.cbc_wbc,
            report.cbc_rbc, report.cbc_platelets, report.lipid_profile_hdl,
            report.lipid_profile_triglycerides, report.lft_sgot,
            report.lft_bilirubin, report.kft_urea, report.post_blood_sugar,
            report.inflammatory_crp, report.inflammatory_esr
        ))
        conn.commit()
        conn.close()
        return {"status": "success", "message": "Daily lab report saved to Vaayu."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/api/labs/{patient_id}")
async def get_patient_labs(patient_id: str):
    try:
        conn = sqlite3.connect('vaayu.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lab_results WHERE patient_id = ? ORDER BY report_date ASC", (patient_id,))
        rows = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return {"status": "success", "data": rows}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/api/nutrition/menu/{patient_id}")
async def get_menu(patient_id: str):
    try:
        patient_id = patient_id.strip().upper()
        conn = sqlite3.connect('vaayu.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM lab_results WHERE patient_id = ? ORDER BY report_date ASC", (patient_id,))
        lab_rows = [dict(row) for row in cursor.fetchall()]
        conn.close()
        latest_lab = lab_rows[-1] if lab_rows else {}
        
        base_menu = [
            {"id": 1, "name": "Iron-Boost Palak Dal Khichdi", "price": 120, "target": "hemoglobin"},
            {"id": 2, "name": "Diabetic Low-GI Foxtail Millet Bowl", "price": 150, "target": "fasting_blood_sugar"},
            {"id": 3, "name": "Hepatoprotective Steamed Idli & Herbal Soup", "price": 100, "target": "lft_sgpt"},
            {"id": 4, "name": "Heart-Safe Oats & Flaxseed Porridge", "price": 110, "target": "lipid_profile_ldl"},
            {"id": 5, "name": "High-Protein Post-Surgery Moong Soup", "price": 130, "target": "recovery"},
            {"id": 6, "name": "Renal-Safe Low-Potassium Veggie Stew", "price": 140, "target": "kft_creatinine"},
            {"id": 7, "name": "Vaayu Seva Compact Nutrient Budget Box (High-Iron Ragi, Moong, Millet, ORS)", "price": 49, "target": "budget", "is_budget_box": True}
        ]
        
        for item in base_menu:
            item["is_recommended"] = False
            item["match_reason"] = "Nutritious option for everyday health."
            
            if item.get("is_budget_box"):
                item["is_recommended"] = True
                item["match_reason"] = "Subsidized Budget Box with all recovery nutrients tailored for low-income citizens."
            elif item["target"] == "hemoglobin" and latest_lab.get("hemoglobin", 0) > 0 and latest_lab.get("hemoglobin", 0) < 13.8:
                item["is_recommended"] = True
                item["match_reason"] = "Recommended for your low Hemoglobin."
            elif item["target"] == "fasting_blood_sugar" and latest_lab.get("fasting_blood_sugar", 0) > 100:
                item["is_recommended"] = True
                item["match_reason"] = "Best for controlling your Fasting Blood Sugar."
            elif item["target"] == "lft_sgpt" and latest_lab.get("lft_sgpt", 0) > 56:
                item["is_recommended"] = True
                item["match_reason"] = "Zero-oil diet recommended for your Liver (SGPT)."
                
        return {"status": "success", "menu": base_menu}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.post("/api/nutrition/order")
async def place_order(order: FoodOrderCreate):
    try:
        conn = sqlite3.connect('vaayu.db')
        cursor = conn.cursor()
        status_msg = "Sterile Kitchen Preparing -> Out for Fast Delivery (25 mins)"
        date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('''
            INSERT INTO food_orders (patient_id, items_summary, total_price, delivery_address, status, order_date)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (order.patient_id, order.items_summary, order.total_price, order.delivery_address, status_msg, date_str))
        conn.commit()
        conn.close()
        return {"status": "success", "message": "Order placed successfully.", "tracking_status": status_msg}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/api/nutrition/orders/{patient_id}")
async def get_patient_orders(patient_id: str):
    try:
        conn = sqlite3.connect('vaayu.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM food_orders WHERE patient_id = ? ORDER BY order_date DESC", (patient_id,))
        orders = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return {"status": "success", "orders": orders}
    except Exception as e:
        return {"status": "error", "message": str(e)}