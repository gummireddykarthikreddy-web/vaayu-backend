import React, { useEffect, useState } from 'react';
import { ScrollView, TouchableOpacity } from 'react-native';
import { useRouter } from 'expo-router';

const GoldMicrochipImg = require('../../assets/images/GoldMicrochip.png');
const BurningBlueFireOrb = require('../../assets/images/BurningBlueFireOrb.png');
const GoldTreasureCard = require('../../assets/images/GoldTreasureCard.png');

const getUri = (source: any): string => {
  if (!source) return '';
  if (typeof source === 'string') return source;
  if (typeof source === 'object') return source.uri || source.default || '';
  return String(source);
};

export default function PatientPortal() {
  const router = useRouter();
  const [patientData, setPatientData] = useState<any>(null);

  useEffect(() => {
    fetch('https://vaayu-backend-ulzh.onrender.com/api/patient/VAAYU-77572')
      .then(res => res.json())
      .then(data => setPatientData(data))
      .catch(err => console.error(err));
  }, []);

  const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=VAAYU-77572&color=0F172A&bgcolor=E2E8F0`;

  return (
    <ScrollView contentContainerStyle={{ flexGrow: 1, backgroundColor: '#09111E', padding: 40, alignItems: 'center' }}>
      <style>{`
        
        * { box-sizing: border-box; }

        @keyframes drawRing {
          0% { stroke-dasharray: 0, 100; }
          100% { stroke-dasharray: 75, 100; }
        }
        @keyframes pulseLive {
          0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
          70% { box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }
          100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }
        @keyframes ecgPulse {
          0% { stroke-dashoffset: 200; opacity: 0.2; }
          50% { opacity: 1; filter: drop-shadow(0 0 8px #00E5FF); }
          100% { stroke-dashoffset: 0; opacity: 0.2; }
        }
        @keyframes flashTimer {
          0%, 100% { opacity: 1; text-shadow: 0 0 15px rgba(239,68,68,0.8); }
          50% { opacity: 0.6; text-shadow: 0 0 5px rgba(239,68,68,0.3); }
        }

        @keyframes fireSpin {
          0% { transform: rotate(0deg) scale(1); filter: brightness(1.2) contrast(1.3); }
          50% { transform: rotate(180deg) scale(1.05); filter: brightness(1.5) contrast(1.5); }
          100% { transform: rotate(360deg) scale(1); filter: brightness(1.2) contrast(1.3); }
        }
        .bento-card {
          background: #131C2D; border: 1px solid rgba(255,255,255,0.05); border-radius: 20px; padding: 25px;
          box-shadow: 0 10px 30px rgba(0,0,0,0.5); display: flex; flex-direction: column;
        }
        .bento-title {
          color: #FFF; font-size: 18px; font-weight: 900; margin-top: 0; margin-bottom: 20px;
        }
        .neon-pill {
          background: #0A101C; border: 2px solid; border-radius: 25px; padding: 10px 0; text-align: center; font-weight: 900; font-size: 14px;
        }
        .fire-orb-container {
          position: relative; width: 100%; height: 300px; display: flex; justify-content: center; align-items: center;
        }
        .fire-img {
          position: absolute; width: 450px; height: 450px; object-fit: contain; pointer-events: none; mix-blend-mode: screen;
          animation: fireSpin 12s linear infinite;
        }
      `}</style>

      {/* HEADER */}
      <div style={{ width: '100%', maxWidth: 1300, display: 'flex', justifyContent: 'flex-start', marginBottom: 20 }}>
        <TouchableOpacity onPress={() => router.back()}>
          <div style={{ background: 'rgba(0,229,255,0.1)', border: '1px solid #00E5FF', borderRadius: 8, padding: '8px 15px', color: '#00E5FF', fontWeight: 'bold' }}>
            ← BACK TO HUB
          </div>
        </TouchableOpacity>
      </div>

      <div style={{ width: '100%', maxWidth: 1300, display: 'flex', flexDirection: 'row', gap: 30 }}>
        
        {/* LEFT COLUMN */}
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 30 }}>
          
          {/* VAAYU HEALTH PASS */}
          <div className="bento-card" style={{ padding: 0, overflow: 'hidden' }}>
            {/* Top Silver Area */}
            <div style={{ background: 'linear-gradient(135deg, #F8FAFC 0%, #CBD5E1 50%, #94A3B8 100%)', padding: 30, display: 'flex', justifyContent: 'space-between' }}>
              <div style={{ flex: 1 }}>
                <h2 style={{ margin: 0, color: '#0F172A', fontSize: 24, fontWeight: '900', letterSpacing: -0.5 }}>Vaayu Health Pass</h2>
                <p style={{ margin: '5px 0 25px 0', color: '#475569', fontSize: 13, fontWeight: 'bold' }}>Titanium Smart Card</p>
                <img src={getUri(GoldMicrochipImg)} style={{ width: 64, height: 48, borderRadius: 8, objectFit: 'cover', boxShadow: '0 4px 10px rgba(0,0,0,0.3)', marginBottom: 25 }} />
                
                <p style={{ margin: '0 0 5px 0', color: '#0F172A', fontSize: 12, fontWeight: '900' }}>PATIENT: {(patientData?.patient_info?.name || 'ANNA CHEN').toUpperCase()}</p>
                <p style={{ margin: '0 0 5px 0', color: '#0F172A', fontSize: 12, fontWeight: '900' }}>DOB: 12 OCT 1991</p>
                <p style={{ margin: '0 0 5px 0', color: '#0F172A', fontSize: 12, fontWeight: '900' }}>MEMBER ID: {patientData?.patient_info?.id || 'VHP-88390'}</p>
                <p style={{ margin: 0, color: '#059669', fontSize: 12, fontWeight: '900' }}>STATUS: ACTIVE</p>
              </div>
              
              <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                <div style={{ background: '#E2E8F0', padding: 15, borderRadius: 20, boxShadow: 'inset 0 4px 8px rgba(255,255,255,0.8), 0 10px 20px rgba(0,0,0,0.4)', position: 'relative' }}>
                  <img src={qrUrl} style={{ width: 140, height: 140, borderRadius: 8 }} />
                </div>
                <div style={{ width: 0, height: 0, borderLeft: '15px solid transparent', borderRight: '15px solid transparent', borderTop: '15px solid #E2E8F0', marginTop: -1 }} />
              </div>
            </div>
            {/* Bottom Dark Area */}
            <div style={{ background: '#1E293B', padding: 20, display: 'flex', gap: 20, alignItems: 'center' }}>
              <div style={{ flex: 1, height: 12, background: 'linear-gradient(90deg, #F59E0B, #FDE047 80%, rgba(253,224,71,0))', borderRadius: 6, boxShadow: '0 0 12px rgba(245₹58₹1,0.5)' }} />
              <div style={{ background: 'linear-gradient(180deg, #E2E8F0, #94A3B8)', padding: '10px 20px', borderRadius: 8, color: '#0F172A', fontWeight: '900', fontSize: 12, boxShadow: '0 4px 10px rgba(0,0,0,0.5), inset 0 1px 2px #FFF', cursor: 'pointer' }} onClick={() => window.print()}>
                🖨️ PRINT PHYSICAL CARD
              </div>
            </div>
          </div>

          {/* 11-LANGUAGE AI CARE PLAN */}
          <div className="bento-card">
            <h2 className="bento-title">11-Language AI Care Plan</h2>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 15, marginBottom: 25 }}>
              {[
                { c: 'ENG', col: '#38BDF8' }, { c: 'ESP', col: '#F97316' }, { c: 'FRA', col: '#38BDF8' }, { c: 'DEU', col: '#FDE047' },
                { c: 'RAT', col: '#4ADE80' }, { c: '中文', col: '#FDE047' }, { c: '日本語', col: '#E879F9' }, { c: '한국어', col: '#4ADE80' },
                { c: 'العربية', col: '#4ADE80' }, { c: 'हिन्दी', col: '#F97316' }, { c: 'PYC', col: '#38BDF8' }, { c: 'POR', col: '#F97316' }
              ].map(x => (
                <div key={x.c} className="neon-pill" style={{ borderColor: x.col, color: x.col, boxShadow: `0 0 15px ${x.col}40, inset 0 0 8px ${x.col}30` }}>{x.c}</div>
              ))}
            </div>

            <div style={{ display: 'flex', gap: 15, marginBottom: 20 }}>
              <div style={{ flex: 1, background: '#1C2538', border: '1px solid #334155', borderRadius: 12, padding: 15, display: 'flex', alignItems: 'center' }}>
                <div style={{ width: 36, height: 36, background: '#F97316', borderRadius: 8, display: 'flex', justifyContent: 'center', alignItems: 'center', marginRight: 15, fontSize: 18 }}>🍴</div>
                <div>
                  <p style={{ margin: '0 0 5px 0', color: '#FFF', fontSize: 14, fontWeight: '900' }}>DIET</p>
                  <p style={{ margin: 0, color: '#94A3B8', fontSize: 11, fontWeight: 'bold' }}>VEGAN • HIGH PROTEIN</p>
                </div>
              </div>
              <div style={{ flex: 1, background: '#1C2538', border: '1px solid #334155', borderRadius: 12, padding: 15, display: 'flex', alignItems: 'center' }}>
                <div style={{ width: 36, height: 36, background: '#10B981', borderRadius: 8, display: 'flex', justifyContent: 'center', alignItems: 'center', marginRight: 15, fontSize: 18 }}>🏃</div>
                <div>
                  <p style={{ margin: '0 0 5px 0', color: '#FFF', fontSize: 14, fontWeight: '900' }}>EXERCISE</p>
                  <p style={{ margin: 0, color: '#94A3B8', fontSize: 11, fontWeight: 'bold' }}>45 MIN CARDIO • 3X WEEK</p>
                </div>
              </div>
            </div>

            {/* ALERT & LABS */}
            <div style={{ display: 'flex', gap: 15 }}>
              <div style={{ flex: 1, background: 'linear-gradient(145deg, rgba(127,29,29,0.4), rgba(40,5₹5,0.9))', border: '2px solid #FF2A5F', borderRadius: 12, padding: 25, display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 25px rgba(255,42,95,0.4), inset 0 0 15px rgba(255,42,95,0.2)', textAlign: 'center' }}>
                <span style={{ fontSize: 32, marginBottom: 10 }}>⚠️</span>
                <h3 style={{ margin: 0, color: '#FF2A5F', fontSize: 18, fontWeight: '900', lineHeight: 1.3 }}>UPCOMING<br/>MEDICATION<br/>ALERT</h3>
              </div>
              <div style={{ flex: 1.2, background: '#1C2538', border: '1px solid #334155', borderRadius: 12, padding: 20 }}>
                <p style={{ margin: '0 0 15px 0', color: '#94A3B8', fontSize: 11, fontWeight: 'bold', letterSpacing: 1 }}>RECENT LAB RESULTS</p>
                {[
                  { n: 'IRON LEVELS', v: 'HIGH', c: '#FF2A5F', i: '⚠️' },
                  { n: 'VITAMIN DLS', v: 'LOW', c: '#FF2A5F', i: '⚠️' },
                  { n: 'VITAMIN D', v: 'LOW', c: '#FF2A5F', i: '⚠️' },
                  { n: 'CHOLESTEROL', v: 'NORMAL', c: '#4ADE80', i: '✔' },
                  { n: 'CHOLESTEROL', v: 'NORMAL', c: '#4ADE80', i: '✔' },
                ].map((l, i) => (
                  <div key={i} style={{ display: 'flex', justifyContent: 'space-between', paddingBottom: 8, marginBottom: 8, borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
                    <span style={{ color: '#94A3B8', fontSize: 11, fontWeight: 'bold' }}>{l.n}</span>
                    <div style={{ display: 'flex', gap: 10 }}>
                      <span style={{ color: l.c, fontSize: 11, fontWeight: 'bold' }}>- {l.v}</span>
                      <span style={{ color: l.c, fontSize: 11 }}>{l.i}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>


          {/* AI SMART PHARMACY & BIOMETRIC TELEMETRY */}
          <div className="bento-card" style={{ border: '1px solid rgba(139, 92, 246, 0.3)', padding: 25, marginTop: 20 }}>
            <h2 className="bento-title" style={{ fontSize: 16, color: '#A78BFA' }}>AI SMART PHARMACY & BIOMETRIC TELEMETRY</h2>
            
            {/* Live Vitals */}
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 20, background: '#0A101C', padding: 15, borderRadius: 12, border: '1px solid rgba(255,255,255,0.05)' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                <span style={{ fontSize: 18 }}>❤️</span>
                <div>
                  <div style={{ color: '#F87171', fontSize: 14, fontWeight: '900' }}>72 BPM</div>
                  <div style={{ color: '#94A3B8', fontSize: 9, fontWeight: 'bold' }}>HEART RATE</div>
                </div>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 10, borderLeft: '1px solid #334155', paddingLeft: 15 }}>
                <span style={{ fontSize: 18 }}>🫁</span>
                <div>
                  <div style={{ color: '#60A5FA', fontSize: 14, fontWeight: '900' }}>99% SpO2</div>
                  <div style={{ color: '#94A3B8', fontSize: 9, fontWeight: 'bold' }}>OXYGEN</div>
                </div>
              </div>
              <div style={{ display: 'flex', alignItems: 'center', gap: 10, borderLeft: '1px solid #334155', paddingLeft: 15 }}>
                <span style={{ fontSize: 18 }}>🩸</span>
                <div>
                  <div style={{ color: '#C084FC', fontSize: 14, fontWeight: '900' }}>120/80</div>
                  <div style={{ color: '#94A3B8', fontSize: 9, fontWeight: 'bold' }}>BLOOD PRESSURE</div>
                </div>
              </div>
            </div>

            {/* ECG Monitor */}
            <div style={{ height: 60, background: '#020617', boxShadow: 'inset 0 0 15px rgba(0,0,0,0.8)', borderRadius: 12, marginBottom: 20, position: 'relative', overflow: 'hidden', display: 'flex', alignItems: 'center' }}>
              <svg width="100%" height="100%" viewBox="0 0 400 60" preserveAspectRatio="none">
                <path d="M0,30 L50,30 L60,10 L70,50 L80,30 L400,30" fill="none" stroke="#00E5FF" strokeWidth="2" strokeDasharray="200" style={{ animation: 'ecgPulse 2.5s linear infinite' }} />
              </svg>
            </div>

            {/* Pharmacy Pod */}
            <div style={{ background: 'linear-gradient(145deg, rgba(30,41,59,0.7), rgba(15,23,42,0.9))', borderRadius: 12, padding: 15, display: 'flex', alignItems: 'center', gap: 15, border: '1px solid rgba(255,255,255,0.1)', marginBottom: 20, boxShadow: '0 5px 15px rgba(0,0,0,0.3)' }}>
              <div style={{ width: 40, height: 40, background: 'linear-gradient(135deg, #EF4444 50%, #FFFFFF 50%)', borderRadius: 20, transform: 'rotate(45deg)', border: '2px solid rgba(255,255,255,0.2)', boxShadow: '0 0 10px rgba(239,68,68,0.5)' }} />
              <div style={{ flex: 1 }}>
                <div style={{ color: '#94A3B8', fontSize: 10, fontWeight: 'bold', letterSpacing: 1 }}>NEXT SCHEDULED DOSE</div>
                <div style={{ color: '#FFF', fontSize: 13, fontWeight: '900' }}>Post-Op Antibiotic (500mg)</div>
              </div>
              <div style={{ background: '#020617', padding: '8px 12px', borderRadius: 8, border: '1px solid rgba(239,68,68,0.3)' }}>
                <span style={{ color: '#EF4444', fontSize: 24, fontWeight: 'bold', fontFamily: 'monospace', letterSpacing: 4, animation: 'flashTimer 1s infinite' }}>01:45:20</span>
              </div>
            </div>

            {/* Nurse Button */}
            <div style={{ width: '100%', background: 'linear-gradient(180deg, #EF4444, #B91C1C)', borderRadius: 12, padding: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 20px rgba(239,68,68,0.5)', cursor: 'pointer', border: '1px solid #F87171' }}>
              <span style={{ color: '#FFF', fontSize: 14, fontWeight: '900', letterSpacing: 1, textShadow: '0 2px 4px rgba(0,0,0,0.5)' }}>🏥 REQUEST NURSE ASSISTANCE</span>
            </div>
          </div>


          {/* AI POST-OP MOBILITY & REHAB TRACKER */}
          <div style={{ background: 'linear-gradient(145deg, rgba(15,23,42,0.6), rgba(8,14,33,0.85))', border: '1px solid rgba(56, 189, 248, 0.3)', borderRadius: 24, padding: 20, marginTop: 24 }}>
            <h2 className="bento-title" style={{ fontSize: 16, color: '#38BDF8', marginBottom: 15 }}>AI POST-OP MOBILITY & REHAB</h2>
            <div style={{ display: 'flex', alignItems: 'center', gap: 20 }}>
              
              {/* Left: 3D Progress Ring */}
              <div style={{ position: 'relative', width: 80, height: 80, display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                <svg viewBox="0 0 36 36" style={{ width: 80, height: 80, filter: 'drop-shadow(0 0 8px #38BDF8)', transform: 'rotate(-90deg)' }}>
                  <circle cx="18" cy="18" r="15.915" fill="none" stroke="#1E293B" strokeWidth="3" />
                  <circle cx="18" cy="18" r="15.915" fill="none" stroke="#38BDF8" strokeWidth="3" strokeDasharray="75, 100" style={{ animation: 'drawRing 2s ease-out forwards' }} strokeLinecap="round" />
                </svg>
                <div style={{ position: 'absolute', color: '#FFF', fontSize: 18, fontWeight: '900', textShadow: '0 0 5px rgba(56,189,248,0.8)' }}>75%</div>
              </div>

              {/* Right: PT Checklist */}
              <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 8 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                  <span style={{ color: '#4ADE80', fontWeight: 'bold' }}>[✔]</span>
                  <span style={{ color: '#4ADE80', fontSize: 12, fontWeight: 'bold' }}>10 Min Assisted Walk</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                  <span style={{ color: '#4ADE80', fontWeight: 'bold' }}>[✔]</span>
                  <span style={{ color: '#4ADE80', fontSize: 12, fontWeight: 'bold' }}>Joint Flexion (Set 1)</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
                  <span style={{ color: '#475569', fontWeight: 'bold' }}>[⏳]</span>
                  <span style={{ color: '#FBBF24', fontSize: 12, fontWeight: 'bold' }}>Joint Flexion (Set 2)</span>
                </div>
              </div>

            </div>
          </div>

          {/* CARE TEAM & SECURE TELE-CONSULT */}
          <div style={{ flexGrow: 1, background: 'linear-gradient(145deg, rgba(15,23,42,0.6), rgba(4,10,24,0.85))', border: '1px solid rgba(74, 222, 128, 0.3)', borderRadius: 24, padding: 20, marginTop: 24, display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: 15 }}>
                <div style={{ width: 50, height: 50, borderRadius: 25, background: '#1E293B', border: '2px solid #94A3B8', boxShadow: '0 0 10px rgba(148,163,184,0.5)', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>
                  <span style={{ fontSize: 24 }}>👨‍⚕️</span>
                </div>
                <div style={{ display: 'flex', flexDirection: 'column' }}>
                  <span style={{ color: '#FFF', fontSize: 16, fontWeight: 'bold' }}>Dr. S. Rao</span>
                  <span style={{ color: '#94A3B8', fontSize: 12 }}>Lead Orthopedic Surgeon</span>
                </div>
              </div>
              <div style={{ width: 12, height: 12, borderRadius: 6, background: '#10B981', animation: 'pulseLive 2s infinite' }} />
            </div>

            <div style={{ width: '100%', background: 'linear-gradient(180deg, #0284C7 0%, #0369A1 100%)', boxShadow: '0 8px 25px rgba(2,132,199,0.5), inset 0 2px 4px rgba(255,255,255,0.4)', borderRadius: 12, padding: 14, marginTop: 16, color: 'white', fontWeight: 'bold', textAlign: 'center', cursor: 'pointer' }}>
              <span style={{ fontSize: 14, letterSpacing: 1, textShadow: '0 2px 4px rgba(0,0,0,0.5)' }}>📹 JOIN SECURE VIDEO CONSULT</span>
            </div>
          </div>

        </div>

        {/* RIGHT COLUMN */}
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 30 }}>
          
          {/* RECOVERY ENGINE */}
          <div className="bento-card">
            <h2 className="bento-title">Cellular Recovery Engine</h2>
            
            <div className="fire-orb-container">
              <img src={getUri(BurningBlueFireOrb)} className="fire-img" />
              <div style={{ zIndex: 10, textAlign: 'center' }}>
                <h3 style={{ margin: 0, color: '#FFF', fontSize: 48, fontWeight: '900', textShadow: '0 0 20px #00E5FF' }}>{patientData?.recovery_insights?.recovery_rate || '83.5'}%</h3>
                <p style={{ margin: '5px 0 0 0', color: '#E2E8F0', fontSize: 14, fontWeight: 'bold', letterSpacing: 1 }}>RECOVERY</p>
              </div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 15, marginTop: 20 }}>
              {[
                { i: '💧', c: '#38BDF8', n: 'HYDRATION STATUS', v: '88%' },
                { i: '⚡', c: '#FDE047', n: 'ENERGY LEVELS', v: '72%' },
                { i: '💪', c: '#F43F5E', n: 'MUSCLE TONE', v: '91%' },
                { i: '🛡️', c: '#10B981', n: 'IMMUNE RESPONSE', v: '64%' }
              ].map(s => (
                <div key={s.n} style={{ background: '#1C2538', border: '1px solid #334155', borderRadius: 12, padding: 15, display: 'flex', alignItems: 'center' }}>
                  <div style={{ width: 36, height: 36, background: s.c+'30', borderRadius: 8, display: 'flex', justifyContent: 'center', alignItems: 'center', marginRight: 12, fontSize: 18 }}>{s.i}</div>
                  <div>
                    <p style={{ margin: '0 0 5px 0', color: '#94A3B8', fontSize: 10, fontWeight: 'bold' }}>{s.n}</p>
                    <p style={{ margin: 0, color: '#FFF', fontSize: 18, fontWeight: '900' }}>{s.v}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* NUTRIMED DELIVERY */}
          <div className="bento-card" style={{ flex: 1, padding: 0, overflow: 'hidden', display: 'flex', flexDirection: 'column', position: 'relative' }}>
            <div style={{ padding: '25px 25px 15px 25px', zIndex: 10, background: '#131C2D' }}>
              <h2 className="bento-title" style={{ marginBottom: 0 }}>Vaayu NutriMed Delivery</h2>
            </div>
            
            <div className="nutrimed-scroll" style={{ flex: 1, overflowY: 'auto', padding: '0 25px 100px 25px' }}>
              <style>{`
                .nutrimed-scroll::-webkit-scrollbar { display: none; }
                .nutrimed-scroll { -ms-overflow-style: none; scrollbar-width: none; }
              `}</style>

              {/* TOP BANNER */}
              <div style={{ width: '100%', height: 80, borderRadius: 12, overflow: 'hidden', position: 'relative', marginBottom: 20, boxShadow: '0 10px 20px rgba(0,0,0,0.5)' }}>
                <img src={getUri(GoldTreasureCard)} style={{ width: '100%', height: '100%', objectFit: 'cover', opacity: 0.8 }} />
                <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', padding: 15, display: 'flex', flexDirection: 'column', justifyContent: 'center', background: 'linear-gradient(90deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.2) 100%)' }}>
                  <h3 style={{ margin: 0, color: '#FDE047', fontSize: 14, fontWeight: '900', textShadow: '0 2px 4px rgba(0,0,0,0.8)' }}>Vaayu Seva Golden Balance: Active</h3>
                  <p style={{ margin: '4px 0 0 0', color: '#FFF', fontSize: 11, fontWeight: 'bold', letterSpacing: 1 }}>Free Clinical Delivery Applied</p>
                </div>
              </div>

              {/* BUDGET BOX */}
              <div style={{ background: 'linear-gradient(145deg, rgba(180,83,9,0.25), rgba(120,53₹5,0.75))', border: '1px solid rgba(251₹91,36,0.4)', borderRadius: 16, padding: 14, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 15, boxShadow: '0 5px 15px rgba(0,0,0,0.3)' }}>
                <div style={{ fontSize: 32, textShadow: '0 0 10px rgba(251₹91,36,0.8)' }}>📦</div>
                <div style={{ flex: 1 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 4 }}>
                    <span style={{ color: '#FFF', fontSize: 14, fontWeight: '900' }}>₹49 Compact Clinical Budget Box</span>
                    <span style={{ background: 'rgba(251₹91,36,0.2)', color: '#FBBF24', fontSize: 9, fontWeight: 'bold', padding: '2px 8px', borderRadius: 10, border: '1px solid #FBBF24' }}>💛 Subsidized Seva Tier</span>
                  </div>
                  <span style={{ color: '#E2E8F0', fontSize: 10 }}>Standardized daily macros (600 kcal | 20g Protein) for accessible healing.</span>
                </div>
                <div style={{ background: 'linear-gradient(180deg, #F59E0B, #B45309)', borderRadius: 10, padding: '8px 16px', boxShadow: '0 4px 10px rgba(245₹58₹1,0.4)', cursor: 'pointer' }}>
                  <span style={{ color: '#FFF', fontSize: 12, fontWeight: '900' }}>+ ADD</span>
                </div>
              </div>


              {/* MENU ITEMS */}
              {[
                { 
                  title: 'Sun-Dried Mushroom Detox Bowl', price: '₹240', 
                  badge: '☀️ Targets Low Vitamin D', badgeCol: '#FDE047',
                  desc: 'Rich in Vitamin D2, aiding in optimal calcium absorption and bone recovery post-surgery.', 
                  macros: '280 kcal | 14g Protein', icon: '🥗' 
                },
                { 
                  title: 'Low-Iron Pearl Millet Khichdi', price: '₹120', 
                  badge: '🩸 Balances High Iron', badgeCol: '#FF2A5F',
                  desc: 'Curated to provide sustained energy without excess iron accumulation.', 
                  macros: '320 kcal | 12g Protein', icon: '🍲' 
                },
                { 
                  title: 'Immunity Citrus Cold-Press', price: '₹180', 
                  badge: '🛡️ Enhances Recovery', badgeCol: '#10B981',
                  desc: 'High concentration of Vitamin C and antioxidants to reduce oxidative stress.', 
                  macros: '110 kcal | 2g Protein', icon: '🥤' 
                }
              ].map((item, i) => (
                <div key={i} style={{ background: 'linear-gradient(145deg, rgba(30,41,59,0.7), rgba(15,23,42,0.9))', border: '1px solid rgba(255,255,255,0.1)', borderRadius: 16, padding: 12, marginBottom: 15, display: 'flex', flexDirection: 'row', alignItems: 'center', gap: 15, boxShadow: '0 5px 15px rgba(0,0,0,0.3)' }}>
                  
                  {/* Left Icon */}
                  <div style={{ minWidth: 70, width: 70, height: 70, borderRadius: 35, background: '#0F172A', display: 'flex', justifyContent: 'center', alignItems: 'center', border: '1px solid rgba(255,255,255,0.1)', boxShadow: 'inset 0 0 15px rgba(255,255,255,0.05)', fontSize: 32 }}>
                    {item.icon}
                  </div>
                  
                  {/* Middle Details */}
                  <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 4 }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ fontSize: 16, fontWeight: 'bold', color: '#F8FAFC' }}>{item.title}</span>
                      <span style={{ color: '#E2E8F0', fontSize: 13, fontWeight: 'bold' }}>{item.price}</span>
                    </div>
                    
                    <div style={{ alignSelf: 'flex-start', background: item.badgeCol + '20', border: '1px solid ' + item.badgeCol, borderRadius: 10, padding: '2px 8px', display: 'inline-block' }}>
                      <span style={{ color: item.badgeCol, fontSize: 9, fontWeight: 'bold' }}>{item.badge}</span>
                    </div>
                    
                    <span style={{ color: '#94A3B8', fontSize: 10, lineHeight: 1.3 }}>{item.desc}</span>
                    <span style={{ fontSize: 12, color: '#64748B', marginTop: 4, letterSpacing: 0.5 }}>{item.macros}</span>
                  </div>
                  
                  {/* Right Button */}
                  <div style={{ background: 'linear-gradient(180deg, #10B981, #059669)', borderRadius: 10, padding: '8px 12px', boxShadow: '0 4px 10px rgba(16₹85₹29,0.4)', cursor: 'pointer', whiteSpace: 'nowrap' }}>
                    <span style={{ color: '#FFF', fontSize: 11, fontWeight: '900' }}>+ ADD</span>
                  </div>
                </div>
              ))}
            </div>
            
            {/* CHECKOUT BAR */}
            <div style={{ position: 'absolute', bottom: 0, left: 0, width: '100%', padding: '15px 25px', background: 'linear-gradient(0deg, #131C2D 70%, rgba(19,28,45,0) 100%)', zIndex: 20 }}>
              <div style={{ display: 'flex', gap: 12, width: '100%' }}>
                <div style={{ flex: 1, background: 'linear-gradient(180deg, #10B981, #059669)', borderRadius: 12, padding: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 20px rgba(16₹85₹29,0.5)', cursor: 'pointer', border: '1px solid #34D399' }}>
                  <span style={{ color: '#FFF', fontSize: 13, fontWeight: '900', letterSpacing: 1, textShadow: '0 2px 4px rgba(0,0,0,0.5)' }}>PLACE CLINICAL ORDER</span>
                </div>
                <div style={{ flex: 1, background: 'linear-gradient(145deg, #1E293B, #0F172A)', borderRadius: 12, padding: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', border: '1px solid rgba(255,255,255,0.2)', cursor: 'pointer', boxShadow: '0 4px 10px rgba(0,0,0,0.5)' }}>
                  <span style={{ color: '#94A3B8', fontSize: 11, fontWeight: '900', letterSpacing: 1 }}>📜 VIEW FULL CLINICAL MENU</span>
                </div>
              </div>
            </div>
          </div>

          {/* HAZARD MATRIX */}
          <div className="bento-card">
            <h2 className="bento-title">AI LAB ASSISTANT HAZARD MATRIX</h2>
            <div style={{ border: '1px solid #334155', borderRadius: 12, overflow: 'hidden' }}>
              {[
                { p: 'IRON LEVELS', v: 'HIGH', h: true, a: 'ADJUST DIET', i: '🍽️' },
                { p: 'VITAMIN DLS', v: 'LOW', h: true, a: 'INCREASE SUNLIGHT', i: '☀️' },
                { p: 'VITAMIN D', v: 'LOW', h: true, a: 'MAINTAIN CURRENT REGIMEN', i: '⏳' },
                { p: 'CHOLESTEROL', v: 'NORMAL', h: false, a: 'MAINTAIN CURRENT REGIMEN', i: '⏳' },
                { p: 'CHOLESTEROL', v: 'NORMAL', h: false, a: 'ADJUST DIET', i: '🍽️' }
              ].map((r, i) => (
                <div key={i} style={{ display: 'flex', borderBottom: i < 4 ? '1px solid #334155' : 'none' }}>
                  <div style={{ flex: 1, padding: 12, background: '#0A101C', borderRight: '1px solid #334155', display: 'flex', justifyContent: 'space-between' }}>
                    <span style={{ color: '#94A3B8', fontSize: 11, fontWeight: 'bold' }}>{r.p}</span>
                    <div style={{ display: 'flex', gap: 10 }}>
                      <span style={{ color: r.h ? '#FF2A5F' : '#4ADE80', fontSize: 11, fontWeight: 'bold' }}>- {r.v}</span>
                      <span style={{ color: r.h ? '#FF2A5F' : '#4ADE80', fontSize: 11 }}>{r.h ? '⚠️' : '✔'}</span>
                    </div>
                  </div>
                  <div style={{ flex: 1.2, padding: 12, background: '#131C2D' }}>
                    <span style={{ color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>{r.i}  {r.a}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>

          {/* AI NUTRIENT ABSORPTION & RECOVERY VELOCITY */}
          <div style={{ background: 'linear-gradient(145deg, rgba(15,23,42,0.5), rgba(2,6,23,0.8))', border: '1px solid rgba(0, 229, 255, 0.15)', borderRadius: 24, padding: 24, marginTop: 24 }}>
            <h2 className="bento-title" style={{ fontSize: 16, marginBottom: 15, color: '#00E5FF' }}>AI NUTRIENT ABSORPTION & RECOVERY VELOCITY</h2>
            <div style={{ display: 'flex', gap: 24 }}>
              
              {/* Left Side: Micro-Nutrient Synthesis */}
              <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 16 }}>
                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6 }}>
                    <span style={{ color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Iron Clearance Rate</span>
                    <span style={{ color: '#38BDF8', fontSize: 10, fontWeight: '900' }}>+14% Faster than baseline</span>
                  </div>
                  <div style={{ width: '100%', height: 8, background: '#0F172A', borderRadius: 4, overflow: 'hidden', border: '1px solid rgba(56₹89,248,0.2)' }}>
                    <div style={{ width: '75%', height: '100%', background: 'linear-gradient(90deg, #0369A1, #38BDF8)', boxShadow: '0 0 10px rgba(56₹89,248,0.8)' }} />
                  </div>
                </div>

                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6 }}>
                    <span style={{ color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Vitamin D Synthesis</span>
                    <span style={{ color: '#FBBF24', fontSize: 10, fontWeight: '900' }}>82% Optimal Absorption</span>
                  </div>
                  <div style={{ width: '100%', height: 8, background: '#0F172A', borderRadius: 4, overflow: 'hidden', border: '1px solid rgba(251₹91,36,0.2)' }}>
                    <div style={{ width: '82%', height: '100%', background: 'linear-gradient(90deg, #B45309, #FBBF24)', boxShadow: '0 0 10px rgba(251₹91,36,0.8)' }} />
                  </div>
                </div>

                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6 }}>
                    <span style={{ color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Cellular Regeneration</span>
                    <span style={{ color: '#4ADE80', fontSize: 10, fontWeight: '900' }}>91% Tissue Repair</span>
                  </div>
                  <div style={{ width: '100%', height: 8, background: '#0F172A', borderRadius: 4, overflow: 'hidden', border: '1px solid rgba(74,222₹28,0.2)' }}>
                    <div style={{ width: '91%', height: '100%', background: 'linear-gradient(90deg, #166534, #4ADE80)', boxShadow: '0 0 10px rgba(74,222₹28,0.8)' }} />
                  </div>
                </div>
              </div>

              {/* Right Side: Predictive Healing Timeline */}
              <div style={{ flex: 1, borderLeft: '1px solid rgba(255,255,255,0.1)', paddingLeft: 24, display: 'flex', flexDirection: 'column', justifyContent: 'center', gap: 15 }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                  <div style={{ minWidth: 12, width: 12, height: 12, borderRadius: 6, background: '#4ADE80', boxShadow: '0 0 8px #4ADE80' }} />
                  <span style={{ color: '#94A3B8', fontSize: 12, fontWeight: 'bold' }}>[✔] Post-Op Stability Reached (Day 3)</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                  <div style={{ minWidth: 12, width: 12, height: 12, borderRadius: 6, background: '#38BDF8', boxShadow: '0 0 12px #38BDF8', animation: 'pulseOrb 2s infinite' }} />
                  <span style={{ color: '#FFF', fontSize: 12, fontWeight: '900', textShadow: '0 0 5px rgba(56₹89,248,0.5)' }}>[⚡] Intensive Nutrient Loading (Day 7)</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                  <div style={{ minWidth: 12, width: 12, height: 12, borderRadius: 6, border: '2px solid #475569', background: 'transparent' }} />
                  <span style={{ color: '#475569', fontSize: 12, fontWeight: 'bold' }}>[⏳] Target Peak Immunity (Day 14)</span>
                </div>
              </div>

            </div>
          </div>


        </div>

      </div>
    </ScrollView>
  );
}
