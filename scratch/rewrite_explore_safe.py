import os

code = """import React, { useEffect, useState } from 'react';
import { ScrollView, TouchableOpacity } from 'react-native';
import { useRouter } from 'expo-router';

const CrimsonGlassSlab = require('../../assets/images/CrimsonGlassSlab.png');
const ObsidianGoldSlab = require('../../assets/images/ObsidianGoldSlab.png');
const BurningBlueFireOrb = require('../../assets/images/BurningBlueFireOrb.png');
const GlassCardSlab = require('../../assets/images/GlassCardSlab.png');

const getUri = (source: any): string => {
  if (!source) return '';
  if (typeof source === 'string') return source;
  if (typeof source === 'object') return source.uri || source.default || '';
  return String(source);
};

export default function DoctorVaultScreen() {
  const router = useRouter();
  const [patientData, setPatientData] = useState<any>(null);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/api/patient/VAAYU-77572')
      .then(r => r.json())
      .then(data => setPatientData(data))
      .catch(e => console.error(e));
  }, []);

  return (
    <ScrollView contentContainerStyle={{ flexGrow: 1, backgroundColor: '#050B14', padding: 40, alignItems: 'center' }}>
      <style>{`
        * { box-sizing: border-box; }
        @keyframes fireSpin {
          0% { transform: rotate(0deg) scale(1); filter: brightness(1.2) contrast(1.3); }
          50% { transform: rotate(180deg) scale(1.05); filter: brightness(1.5) contrast(1.5); }
          100% { transform: rotate(360deg) scale(1); filter: brightness(1.2) contrast(1.3); }
        }
        @keyframes pulseOrb {
          0%, 100% { transform: scale(1); opacity: 0.8; }
          50% { transform: scale(1.05); opacity: 1; }
        }
        .slab-crimson {
          transform: perspective(1000px) rotateY(12deg) rotateX(8deg);
          box-shadow: -20px 20px 40px rgba(255,42,95,0.3);
          border-radius: 20px;
        }
        .slab-obsidian {
          transform: perspective(1000px) rotateY(-12deg) rotateX(8deg);
          box-shadow: 20px 20px 40px rgba(245,158,11,0.2);
          border-radius: 20px;
        }
        .gauge-circle {
          width: 50px; height: 50px; border-radius: 25px; border: 3px solid rgba(255,100,100,0.5);
          display: flex; justify-content: center; align-items: center; box-shadow: inset 0 0 10px rgba(255,42,95,0.5);
        }
        .check-item {
          display: flex; align-items: center; background: rgba(0,0,0,0.4); padding: 12px 15px; border-radius: 8px; border: 1px solid rgba(245,158,11,0.3); margin-bottom: 12px;
        }
        .ai-panel {
          background: rgba(30,41,59,0.7); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 20px;
          backdrop-filter: blur(15px); margin-bottom: 20px;
        }
        .fire-orb-container {
          position: relative; width: 340px; height: 340px; border-radius: 170px;
          background: radial-gradient(circle, rgba(0,229,255,0.2) 0%, rgba(0,0,0,0) 70%);
          display: flex; justify-content: center; align-items: center;
        }
        .fire-img {
          position: absolute; width: 450px; height: 450px; object-fit: contain; mix-blend-mode: screen; pointer-events: none;
          mask-image: radial-gradient(circle at center, black 40%, transparent 65%);
          -webkit-mask-image: radial-gradient(circle at center, black 40%, transparent 65%);
          animation: fireSpin 8s linear infinite;
        }
      `}</style>

      <div style={{ width: '100%', maxWidth: 1200, display: 'flex', flexDirection: 'column', gap: 60 }}>
        
        {/* ROW 1 */}
        <div style={{ display: 'flex', flexDirection: 'row', gap: 60 }}>
          
          {/* TOP LEFT: 3D Crimson Glass */}
          <div style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <h2 style={{ color: '#FFF', fontSize: 18, marginBottom: 30, letterSpacing: 1 }}>3D Crimson Glass</h2>
            
            <div className="slab-crimson" style={{ position: 'relative', width: 400, height: 480, display: 'flex', flexDirection: 'column', padding: 35, background: 'linear-gradient(135deg, rgba(255,42,95,0.2), rgba(15,23,42,0.9))', border: '1px solid rgba(255,42,95,0.4)' }}>
              <img src={getUri(CrimsonGlassSlab)} style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', objectFit: 'cover', opacity: 0.3, mixBlendMode: 'screen', borderRadius: 20 }} />
              
              <div style={{ zIndex: 10, flex: 1, display: 'flex', flexDirection: 'column' }}>
                <h3 style={{ color: '#FFF', fontSize: 24, fontWeight: '900', lineHeight: 1.2, textShadow: '0 0 10px #FF2A5F', marginBottom: 25 }}>Pre-Surgery Safety &<br/>Infection Shield</h3>
                
                <p style={{ margin: '0 0 10px 0', color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>Infection Risks</p>
                <div style={{ display: 'flex', justifyContent: 'space-between', padding: '15px 20px', background: 'rgba(0,0,0,0.3)', borderRadius: 12, border: '1px solid rgba(255,42,95,0.2)', marginBottom: 20 }}>
                  <div className="gauge-circle"><span style={{ color: '#FFF', fontSize: 13, fontWeight: 'bold' }}>85%</span></div>
                  <div className="gauge-circle"><span style={{ color: '#FFF', fontSize: 13, fontWeight: 'bold' }}>85%</span></div>
                  <div className="gauge-circle"><span style={{ color: '#FFF', fontSize: 13, fontWeight: 'bold' }}>85%</span></div>
                </div>

                <div style={{ display: 'flex', gap: 15, flex: 1 }}>
                  <div style={{ flex: 1, background: 'rgba(0,0,0,0.3)', borderRadius: 12, padding: 15, border: '1px solid rgba(255,42,95,0.2)' }}>
                    <p style={{ margin: '0 0 10px 0', color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Safety Protocols</p>
                    <div style={{ width: '80%', height: 6, background: '#334155', borderRadius: 3, marginBottom: 10 }}><div style={{ width: '60%', height: '100%', background: '#E2E8F0', borderRadius: 3 }} /></div>
                    <div style={{ width: '80%', height: 6, background: '#334155', borderRadius: 3 }}><div style={{ width: '40%', height: '100%', background: '#E2E8F0', borderRadius: 3 }} /></div>
                  </div>
                  <div style={{ flex: 1, background: 'rgba(0,0,0,0.3)', borderRadius: 12, padding: 15, border: '1px solid rgba(255,42,95,0.2)' }}>
                    <p style={{ margin: '0 0 10px 0', color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Patient Vitals</p>
                    <div style={{ width: '100%', height: 6, background: '#334155', borderRadius: 3, marginBottom: 10 }}><div style={{ width: '80%', height: '100%', background: '#FF2A5F', borderRadius: 3 }} /></div>
                    <div style={{ width: '100%', height: 6, background: '#334155', borderRadius: 3 }}><div style={{ width: '50%', height: '100%', background: '#00E5FF', borderRadius: 3 }} /></div>
                  </div>
                </div>

                <div style={{ background: 'rgba(255,42,95,0.1)', padding: '10px 15px', borderRadius: 8, border: '1px solid rgba(255,42,95,0.3)', marginTop: 20 }}>
                  <span style={{ color: '#FF2A5F', fontSize: 14, fontWeight: 'bold' }}>Alert Status: High ⚠️</span>
                </div>
              </div>
            </div>
          </div>

          {/* TOP RIGHT: 3D Obsidian & Gold checklist */}
          <div style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <h2 style={{ color: '#FFF', fontSize: 18, marginBottom: 30, letterSpacing: 1 }}>3D Obsidian & Gold checklist</h2>
            
            <div className="slab-obsidian" style={{ position: 'relative', width: 400, height: 480, display: 'flex', flexDirection: 'column', padding: 35, background: 'linear-gradient(135deg, rgba(30,41,59,0.9), rgba(5,11,20,0.95))', border: '1px solid rgba(245,158,11,0.4)' }}>
              <img src={getUri(ObsidianGoldSlab)} style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', objectFit: 'cover', opacity: 0.3, mixBlendMode: 'screen', borderRadius: 20 }} />
              
              <div style={{ zIndex: 10, flex: 1, display: 'flex', flexDirection: 'column' }}>
                <h3 style={{ color: '#FFF', fontSize: 22, fontWeight: '900', lineHeight: 1.3, textAlign: 'center', marginBottom: 25 }}>Doctor's Pre-Surgery<br/>Preventive Measures</h3>
                
                <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
                  <div className="check-item"><div style={{ width: 18, height: 18, borderRadius: 9, background: 'radial-gradient(circle, #FDE047, #F59E0B)', marginRight: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px #F59E0B' }}><span style={{ color: '#000', fontSize: 10, fontWeight: 'bold' }}>✓</span></div><span style={{ color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>Verify Patient Identity</span></div>
                  <div className="check-item"><div style={{ width: 18, height: 18, borderRadius: 9, background: 'radial-gradient(circle, #FDE047, #F59E0B)', marginRight: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px #F59E0B' }}><span style={{ color: '#000', fontSize: 10, fontWeight: 'bold' }}>✓</span></div><span style={{ color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>Confirm Surgical Site</span></div>
                  <div className="check-item"><div style={{ width: 18, height: 18, borderRadius: 9, background: 'radial-gradient(circle, #FDE047, #F59E0B)', marginRight: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px #F59E0B' }}><span style={{ color: '#000', fontSize: 10, fontWeight: 'bold' }}>✓</span></div><span style={{ color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>Review Medical History</span></div>
                  <div className="check-item"><div style={{ width: 18, height: 18, borderRadius: 9, background: 'radial-gradient(circle, #FDE047, #F59E0B)', marginRight: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px #F59E0B' }}><span style={{ color: '#000', fontSize: 10, fontWeight: 'bold' }}>✓</span></div><span style={{ color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>Administer Prophylactic Antibiotics</span></div>
                  <div className="check-item"><div style={{ width: 18, height: 18, borderRadius: 9, background: 'radial-gradient(circle, #FDE047, #F59E0B)', marginRight: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px #F59E0B' }}><span style={{ color: '#000', fontSize: 10, fontWeight: 'bold' }}>✓</span></div><span style={{ color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>Check Equipment Functionality</span></div>
                </div>

                <div style={{ width: '100%', height: 6, background: '#1E293B', borderRadius: 3, marginTop: 10, position: 'relative' }}>
                  <div style={{ width: '80%', height: '100%', background: '#F59E0B', borderRadius: 3, boxShadow: '0 0 10px #F59E0B' }} />
                  <span style={{ position: 'absolute', right: 0, top: 15, color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>80%</span>
                </div>
              </div>
            </div>
          </div>

        </div>

        {/* ROW 2 */}
        <div style={{ display: 'flex', flexDirection: 'row', gap: 60, marginTop: 20 }}>
          
          {/* BOTTOM LEFT: 3D Blue Flame Recovery Orb */}
          <div style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <div className="fire-orb-container">
              <img src={getUri(BurningBlueFireOrb)} className="fire-img" />
              
              <div style={{ zIndex: 10, textAlign: 'center', background: 'rgba(0,0,0,0.5)', padding: 30, borderRadius: '50%', boxShadow: '0 0 20px rgba(0,229,255,0.2)' }}>
                <h3 style={{ margin: 0, color: '#FFF', fontSize: 56, fontWeight: '900', textShadow: '0 0 20px #00E5FF' }}>{patientData?.recovery_insights?.recovery_rate || 92}%</h3>
                <p style={{ margin: '5px 0 0 0', color: '#E2E8F0', fontSize: 13, letterSpacing: 1, fontWeight: 'bold' }}>Recovery Index</p>
              </div>

              <span style={{ position: 'absolute', top: -10, left: -20, color: '#94A3B8', fontSize: 12, width: 100 }}>Post-Op Vital<br/>Monitoring</span>
              <span style={{ position: 'absolute', top: -10, right: -20, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'right' }}>Healing Orb<br/>Steness</span>
              <span style={{ position: 'absolute', bottom: -10, left: -20, color: '#94A3B8', fontSize: 12, width: 100 }}>Post-Op Vital<br/>Monitoring</span>
              <span style={{ position: 'absolute', bottom: -10, right: -20, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'right' }}>Healing<br/>Progress</span>
            </div>
            <h2 style={{ color: '#FFF', fontSize: 18, marginTop: 40, letterSpacing: 1 }}>3D Blue Flame Recovery Orb</h2>
          </div>

          {/* BOTTOM RIGHT: AI Summary */}
          <div style={{ flex: 1, display: 'flex', flexDirection: 'column', position: 'relative' }}>
            <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', zIndex: 0 }}>
              <img src={getUri(GlassCardSlab)} style={{ width: '100%', height: '100%', objectFit: 'cover', opacity: 0.1, borderRadius: 20 }} />
            </div>

            <div style={{ zIndex: 10, width: '100%' }}>
              <div className="ai-panel">
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 15 }}>
                  <h3 style={{ margin: 0, color: '#FFF', fontSize: 16 }}>AI Clinical Summary</h3>
                  <div style={{ display: 'flex', gap: 10 }}>
                    <span style={{ padding: '4px 10px', background: 'rgba(0,229,255,0.1)', color: '#00E5FF', fontSize: 10, borderRadius: 12 }}>Synthesized</span>
                  </div>
                </div>
                <p style={{ color: '#94A3B8', fontSize: 11, marginBottom: 15 }}>Synthesized key data points for realms and recommendations.</p>
                <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 15 }}>
                  <div>
                    <p style={{ margin: '0 0 5px 0', color: '#E2E8F0', fontSize: 11 }}>• Synthesized key Asta points</p>
                    <p style={{ margin: 0, color: '#E2E8F0', fontSize: 11 }}>• Confirmed Medical History</p>
                  </div>
                  <div>
                    <p style={{ margin: '0 0 5px 0', color: '#E2E8F0', fontSize: 11 }}>• Recommendations preserving</p>
                    <p style={{ margin: 0, color: '#E2E8F0', fontSize: 11 }}>• Recommendations recovery</p>
                  </div>
                </div>
              </div>

              <div className="ai-panel">
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 20 }}>
                  <h3 style={{ margin: 0, color: '#FFF', fontSize: 16 }}>3D Prescription Composer</h3>
                  <span style={{ color: '#94A3B8', fontSize: 11, background: 'rgba(255,255,255,0.1)', padding: '4px 10px', borderRadius: 12 }}>Select category</span>
                </div>
                
                <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 25 }}>
                  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
                    <div style={{ width: 44, height: 44, borderRadius: 12, background: '#F43F5E20', border: '1px solid #F43F5E', display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: 8, boxShadow: '0 0 10px #F43F5E40' }}><span style={{ fontSize: 20 }}>💊</span></div>
                    <span style={{ color: '#94A3B8', fontSize: 10 }}>Pain<br/>Management</span>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
                    <div style={{ width: 44, height: 44, borderRadius: 12, background: '#3B82F620', border: '1px solid #3B82F6', display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: 8, boxShadow: '0 0 10px #3B82F640' }}><span style={{ fontSize: 20 }}>💊</span></div>
                    <span style={{ color: '#94A3B8', fontSize: 10 }}>Antibiotics</span>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
                    <div style={{ width: 44, height: 44, borderRadius: 12, background: '#F9731620', border: '1px solid #F97316', display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: 8, boxShadow: '0 0 10px #F9731640' }}><span style={{ fontSize: 20 }}>💊</span></div>
                    <span style={{ color: '#94A3B8', fontSize: 10 }}>Anti-<br/>inflammatory</span>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
                    <div style={{ width: 44, height: 44, borderRadius: 12, background: '#10B98120', border: '1px solid #10B981', display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: 8, boxShadow: '0 0 10px #10B98140' }}><span style={{ fontSize: 20 }}>💊</span></div>
                    <span style={{ color: '#94A3B8', fontSize: 10 }}>Recovery<br/>Aids</span>
                  </div>
                  <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
                    <div style={{ width: 44, height: 44, borderRadius: 12, background: '#8B5CF620', border: '1px solid #8B5CF6', display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: 8, boxShadow: '0 0 10px #8B5CF640' }}><span style={{ fontSize: 20 }}>💊</span></div>
                    <span style={{ color: '#94A3B8', fontSize: 10 }}>Specialized<br/>Medication</span>
                  </div>
                </div>

                <div style={{ background: 'rgba(0,0,0,0.5)', padding: 25, borderRadius: 12, textAlign: 'center', border: '1px solid rgba(255,255,255,0.05)' }}>
                  <h4 style={{ margin: '0 0 5px 0', color: '#FFF', fontSize: 14 }}>Vault Composer</h4>
                  <p style={{ margin: 0, color: '#94A3B8', fontSize: 11 }}>Drag and drop items into a central area to build a comprehensive plan.</p>
                </div>
              </div>
            </div>
            
            <h2 style={{ color: '#FFF', fontSize: 18, marginTop: 20, letterSpacing: 1, textAlign: 'center' }}>AI Clinical Summary + 5-Category<br/>3D Prescription & Vault Composer</h2>
          </div>

        </div>
      </div>
    </ScrollView>
  );
}
"""

with open('src/app/explore.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("explore.tsx fully overwritten safely")
