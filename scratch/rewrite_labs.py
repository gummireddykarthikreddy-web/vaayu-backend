import os

code = """import React from 'react';
import { ScrollView, TouchableOpacity } from 'react-native';
import { useRouter } from 'expo-router';

export default function LabsScreen() {
  const router = useRouter();

  return (
    <ScrollView contentContainerStyle={{ flexGrow: 1, backgroundColor: '#050B14', padding: 40, alignItems: 'center' }}>
      <style>{`
        * { box-sizing: border-box; }
        @keyframes float3DCard {
          0%, 100% { transform: translateY(0px) scale(1); }
          50% { transform: translateY(-5px) scale(1.02); }
        }
        .glass-pod {
          background: linear-gradient(145deg, #0F172A, #020617);
          border: 1px solid rgba(0, 229, 255, 0.3);
          box-shadow: inset 0 2px 10px rgba(255,255,255,0.1), 0 10px 30px rgba(0,0,0,0.5);
          border-radius: 16px;
          padding: 25px;
          margin-bottom: 25px;
        }
        .pod-title {
          color: #00E5FF; font-size: 14px; font-weight: 900; letter-spacing: 2px; margin-top: 0; margin-bottom: 20px;
          border-bottom: 1px solid rgba(0,229,255,0.2); padding-bottom: 10px;
        }
        .input-group {
          display: flex; flex-direction: column; gap: 8px; flex: 1; margin-bottom: 15px;
        }
        .input-label {
          color: #94A3B8; font-size: 11px; font-weight: bold; letter-spacing: 1px;
        }
        .cyber-input {
          background: rgba(0,0,0,0.4);
          border: 1px solid rgba(0, 229, 255, 0.3);
          color: #FFF;
          padding: 12px 15px;
          border-radius: 8px;
          font-family: 'Courier New', monospace;
          font-weight: bold;
          outline: none;
          transition: all 0.2s;
          width: 100%;
        }
        .cyber-input:focus {
          border-color: #00E5FF;
          box-shadow: 0 0 10px rgba(0,229,255,0.3);
        }
        .row {
          display: flex; flex-direction: row; gap: 20px;
        }
      `}</style>

      <div style={{ width: '100%', maxWidth: 1000, display: 'flex', flexDirection: 'column' }}>
        
        {/* HEADER */}
        <div style={{ display: 'flex', flexDirection: 'column', marginBottom: 40 }}>
          <TouchableOpacity onPress={() => router.back()} style={{ alignSelf: 'flex-start', marginBottom: 20 }}>
            <div style={{ background: 'rgba(0,229,255,0.1)', border: '1px solid #00E5FF', borderRadius: 8, padding: '8px 15px', color: '#00E5FF', fontWeight: 'bold', fontSize: 12 }}>
              [ ← Back to Vaayu Hub ]
            </div>
          </TouchableOpacity>
          <h1 style={{ margin: 0, color: '#FFF', fontSize: 28, fontWeight: '900', letterSpacing: 1.5, textShadow: '0 0 15px rgba(255,255,255,0.5)' }}>5-PANEL LAB DIAGNOSTICS INPUT PODS</h1>
          <p style={{ margin: '5px 0 0 0', color: '#00E5FF', fontSize: 12, fontWeight: 'bold', letterSpacing: 2 }}>DIAGNOSTIC DATA ENTRY CONSOLE</p>
        </div>

        {/* POD 1: PATIENT IDENTIFICATION */}
        <div className="glass-pod">
          <h2 className="pod-title">[ PATIENT IDENTIFICATION ]</h2>
          <div className="row">
            <div className="input-group" style={{ marginBottom: 0 }}>
              <label className="input-label">[ PATIENT ID ]</label>
              <input type="text" className="cyber-input" placeholder="e.g., VAAYU-XXXXX" />
            </div>
            <div className="input-group" style={{ marginBottom: 0 }}>
              <label className="input-label">[ REPORT DATE ]</label>
              <input type="text" className="cyber-input" placeholder="YYYY-MM-DD" />
            </div>
          </div>
        </div>

        {/* ROW 2: 3 Columns */}
        <div className="row" style={{ marginBottom: 25, gap: 25 }}>
          {/* POD 2 */}
          <div className="glass-pod" style={{ flex: 1, marginBottom: 0 }}>
            <h2 className="pod-title">[ GENERAL & SUGAR ]</h2>
            <div className="input-group"><label className="input-label">[ HEMOGLOBIN (G/DL) ]</label><input type="text" className="cyber-input" /></div>
            <div className="input-group"><label className="input-label">[ FASTING BLOOD SUGAR (MG/DL) ]</label><input type="text" className="cyber-input" /></div>
            <div className="input-group" style={{ marginBottom: 0 }}><label className="input-label">[ POST BLOOD SUGAR (MG/DL) ]</label><input type="text" className="cyber-input" /></div>
          </div>
          
          {/* POD 3 */}
          <div className="glass-pod" style={{ flex: 1, marginBottom: 0 }}>
            <h2 className="pod-title">[ INFLAMMATORY MARKERS ]</h2>
            <div className="input-group"><label className="input-label">[ CRP (MG/L) ]</label><input type="text" className="cyber-input" /></div>
            <div className="input-group"><label className="input-label">[ ESR (MM/HR) ]</label><input type="text" className="cyber-input" /></div>
          </div>

          {/* POD 4 */}
          <div className="glass-pod" style={{ flex: 1, marginBottom: 0 }}>
            <h2 className="pod-title">[ CBC (COMPLETE BLOOD COUNT) ]</h2>
            <div className="input-group"><label className="input-label">[ WBC (CELLS/MCL) ]</label><input type="text" className="cyber-input" /></div>
            <div className="input-group"><label className="input-label">[ RBC (MILLION/MCL) ]</label><input type="text" className="cyber-input" /></div>
            <div className="input-group" style={{ marginBottom: 0 }}><label className="input-label">[ PLATELETS (CELLS/MCL) ]</label><input type="text" className="cyber-input" /></div>
          </div>
        </div>

        {/* POD 5: LIPID PROFILE */}
        <div className="glass-pod">
          <h2 className="pod-title">[ LIPID PROFILE ]</h2>
          <div className="row">
            <div className="input-group" style={{ marginBottom: 0 }}><label className="input-label">[ LDL (MG/DL) ]</label><input type="text" className="cyber-input" /></div>
            <div className="input-group" style={{ marginBottom: 0 }}><label className="input-label">[ HDL (MG/DL) ]</label><input type="text" className="cyber-input" /></div>
            <div className="input-group" style={{ marginBottom: 0 }}><label className="input-label">[ TRIGLYCERIDES (MG/DL) ]</label><input type="text" className="cyber-input" /></div>
          </div>
        </div>

        {/* POD 6: LFT & KFT */}
        <div className="glass-pod">
          <h2 className="pod-title">[ LFT & KFT (LIVER & KIDNEY) ]</h2>
          <div className="row">
            <div className="input-group"><label className="input-label">[ SGPT (U/L) ]</label><input type="text" className="cyber-input" /></div>
            <div className="input-group"><label className="input-label">[ SGOT (U/L) ]</label><input type="text" className="cyber-input" /></div>
            <div className="input-group"><label className="input-label">[ BILIRUBIN (MG/DL) ]</label><input type="text" className="cyber-input" /></div>
          </div>
          <div className="row">
            <div className="input-group" style={{ marginBottom: 0 }}><label className="input-label">[ CREATININE (MG/DL) ]</label><input type="text" className="cyber-input" /></div>
            <div className="input-group" style={{ marginBottom: 0 }}><label className="input-label">[ UREA (MG/DL) ]</label><input type="text" className="cyber-input" /></div>
            <div className="input-group" style={{ marginBottom: 0 }}></div>
          </div>
        </div>

        {/* SUBMIT BUTTON */}
        <TouchableOpacity style={{ width: '100%', marginTop: 10 }}>
          <div style={{ 
            background: 'linear-gradient(180deg, #10B981 0%, #047857 100%)', 
            borderRadius: 12, 
            padding: '20px', 
            textAlign: 'center', 
            boxShadow: '0 10px 30px rgba(16,185,129,0.4), inset 0 2px 5px rgba(255,255,255,0.5)',
            border: '1px solid #34D399',
            animation: 'float3DCard 3s ease-in-out infinite'
          }}>
            <span style={{ color: '#FFF', fontSize: 18, fontWeight: '900', letterSpacing: 2, textShadow: '0 2px 5px rgba(0,0,0,0.5)' }}>
              TRANSMIT DIAGNOSTIC VITALS
            </span>
          </div>
        </TouchableOpacity>

      </div>
    </ScrollView>
  );
}
"""
with open('src/app/labs.tsx', 'w', encoding='utf-8') as f:
    f.write(code)
print("labs.tsx written")
