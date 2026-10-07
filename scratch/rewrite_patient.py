import os

code = """import React, { useEffect, useState } from 'react';
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
    fetch('http://127.0.0.1:8000/api/patient/VAAYU-77572')
      .then(res => res.json())
      .then(data => setPatientData(data))
      .catch(err => console.error(err));
  }, []);

  const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=VAAYU-77572&color=0F172A&bgcolor=E2E8F0`;

  return (
    <ScrollView contentContainerStyle={{ flexGrow: 1, backgroundColor: '#09111E', padding: 40, alignItems: 'center' }}>
      <style>{`
        * { box-sizing: border-box; }
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
              <div style={{ flex: 1, height: 12, background: 'linear-gradient(90deg, #F59E0B, #FDE047 80%, rgba(253,224,71,0))', borderRadius: 6, boxShadow: '0 0 12px rgba(245,158,11,0.5)' }} />
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
              <div style={{ flex: 1, background: 'linear-gradient(145deg, rgba(127,29,29,0.4), rgba(40,5,15,0.9))', border: '2px solid #FF2A5F', borderRadius: 12, padding: 25, display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 25px rgba(255,42,95,0.4), inset 0 0 15px rgba(255,42,95,0.2)', textAlign: 'center' }}>
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
          <div className="bento-card">
            <h2 className="bento-title">Vaayu NutriMed Delivery</h2>
            <div style={{ display: 'flex', gap: 20 }}>
              <div style={{ flex: 1, borderRadius: 12, overflow: 'hidden', position: 'relative', height: 130 }}>
                <img src={getUri(GoldTreasureCard)} style={{ width: '100%', height: '100%', objectFit: 'cover' }} />
                <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', padding: 20, display: 'flex', flexDirection: 'column', justifyContent: 'space-between', background: 'rgba(0,0,0,0.2)' }}>
                  <h3 style={{ margin: 0, color: '#FFF', fontSize: 16, fontWeight: '900', textShadow: '0 2px 4px rgba(0,0,0,0.8)' }}>Golden<br/>Treasure Card</h3>
                  <p style={{ margin: 0, color: '#FDE047', fontSize: 10, fontWeight: 'bold', letterSpacing: 1 }}>DELIVERY TRACKING</p>
                </div>
              </div>
              <div style={{ flex: 1.2, display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                <p style={{ margin: 0, color: '#94A3B8', fontSize: 10, fontWeight: 'bold', letterSpacing: 1 }}>MEAL SELECTOR TILES</p>
                <div style={{ display: 'flex', gap: 10 }}>
                  <div style={{ flex: 1, background: '#0A101C', border: '1px solid #334155', borderRadius: 8, padding: 8, textAlign: 'center' }}>
                    <div style={{ width: 36, height: 36, borderRadius: 18, background: '#1E293B', margin: '0 auto 8px auto', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>🥗</div>
                    <p style={{ margin: 0, color: '#E2E8F0', fontSize: 9, fontWeight: 'bold' }}>PROTEIN BOWL</p>
                  </div>
                  <div style={{ flex: 1, background: '#0A101C', border: '1px solid #334155', borderRadius: 8, padding: 8, textAlign: 'center' }}>
                    <div style={{ width: 36, height: 36, borderRadius: 18, background: '#1E293B', margin: '0 auto 8px auto', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>🥤</div>
                    <p style={{ margin: 0, color: '#E2E8F0', fontSize: 9, fontWeight: 'bold' }}>SMOOTHIE PACK</p>
                  </div>
                  <div style={{ flex: 1, background: '#0A101C', border: '1px solid #334155', borderRadius: 8, padding: 8, textAlign: 'center' }}>
                    <div style={{ width: 36, height: 36, borderRadius: 18, background: '#1E293B', margin: '0 auto 8px auto', display: 'flex', justifyContent: 'center', alignItems: 'center' }}>🥙</div>
                    <p style={{ margin: 0, color: '#E2E8F0', fontSize: 9, fontWeight: 'bold' }}>DETOX SALAD</p>
                  </div>
                </div>
                <div style={{ display: 'flex', gap: 10, height: 44 }}>
                  <div style={{ width: 44, background: '#1C2538', borderRadius: 8, border: '1px solid #334155', display: 'flex', justifyContent: 'center', alignItems: 'center', color: '#FFF' }}>{'<'}</div>
                  <div style={{ width: 44, background: '#1C2538', borderRadius: 8, border: '1px solid #334155', display: 'flex', justifyContent: 'center', alignItems: 'center', color: '#FFF' }}>{'>'}</div>
                  <div style={{ flex: 1, background: 'linear-gradient(180deg, #10B981, #059669)', borderRadius: 8, display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 15px rgba(16,185,129,0.5)', cursor: 'pointer' }}>
                    <span style={{ color: '#FFF', fontWeight: '900', fontSize: 13, letterSpacing: 1 }}>PLACE ORDER</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          {/* HAZARD MATRIX */}
          <div className="bento-card">
            <h2 className="bento-title">AI LAB ASSISTANT HAZARD MATRIX</h2>
            <div style={{ border: '1px solid #334155', borderRadius: 12, overflow: 'hidden' }}>
              {[
                { p: 'IRON LEVELS', v: 'HIGH', h: True, a: 'ADJUST DIET', i: '🍽️' },
                { p: 'VITAMIN DLS', v: 'LOW', h: True, a: 'INCREASE SUNLIGHT', i: '☀️' },
                { p: 'VITAMIN D', v: 'LOW', h: True, a: 'MAINTAIN CURRENT REGIMEN', i: '⏳' },
                { p: 'CHOLESTEROL', v: 'NORMAL', h: False, a: 'MAINTAIN CURRENT REGIMEN', i: '⏳' },
                { p: 'CHOLESTEROL', v: 'NORMAL', h: False, a: 'ADJUST DIET', i: '🍽️' }
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

        </div>

      </div>
    </ScrollView>
  );
}
"""

with open('src/app/patient.tsx', 'w', encoding='utf-8') as f:
    f.write(code.replace("True", "true").replace("False", "false"))
print("patient.tsx written")
