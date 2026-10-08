import React, { useEffect, useState } from 'react';
import { ScrollView, TouchableOpacity } from 'react-native';
import { useRouter } from 'expo-router';

const GlassCapsuleTube = require('../../assets/images/GlassCapsuleTube.png');

const getUri = (source: any): string => {
  if (!source) return '';
  if (typeof source === 'string') return source;
  if (typeof source === 'object') return source.uri || source.default || '';
  return String(source);
};

export default function Dashboard() {
  const router = useRouter();
  const [labData, setLabData] = useState<any>(null);

  useEffect(() => {
    fetch('https://vaayu-backend-ulzh.onrender.com/api/labs/VAAYU-77572')
      .then(r => r.json())
      .then(data => setLabData(data))
      .catch(e => console.error(e));
  }, []);

  const bloodInventory = [
    { type: 'A+', count: 112, percent: 80 },
    { type: 'A-', count: 45, percent: 65 },
    { type: 'B+', count: 98, percent: 72 },
    { type: 'B-', count: 31, percent: 58 },
    { type: 'O+', count: 145, percent: 91 },
    { type: 'O-', count: 28, percent: 40 },
    { type: 'AB+', count: 67, percent: 68 },
    { type: 'AB-', count: 19, percent: 35 },
  ];

  return (
    <ScrollView contentContainerStyle={{ flexGrow: 1, backgroundColor: '#050B14', padding: 40 }}>
      <style>{`
        * { box-sizing: border-box; }
        @keyframes liquidWave {
          0%, 100% { transform: translateY(0px) scaleY(1); }
          50% { transform: translateY(-4px) scaleY(1.03); }
        }
        @keyframes bubbleRise {
          0% { transform: translateY(0px) scale(0.8); opacity: 0.8; }
          100% { transform: translateY(-80px) scale(1.2); opacity: 0; }
        }
        .hud-border {
          background: rgba(15,23,42,0.6);
          border: 1px solid rgba(0,229,255,0.2);
          box-shadow: 0 0 20px rgba(0,0,0,0.8), inset 0 0 15px rgba(0,229,255,0.05);
          border-radius: 12px;
          padding: 25px;
        }
        .hud-header {
          color: #FFF; font-size: 14px; font-weight: 900; letter-spacing: 1px; margin-top: 0; margin-bottom: 20px;
        }
        .slider-track {
          height: 6px; background: #1E293B; border-radius: 3px; position: relative; width: 100%; box-shadow: inset 0 0 5px rgba(0,0,0,0.5);
        }
        .slider-fill {
          height: 100%; background: #00E5FF; border-radius: 3px; box-shadow: 0 0 10px #00E5FF; position: relative;
        }
        .slider-knob {
          width: 14px; height: 14px; border-radius: 7px; background: #FFF; position: absolute; right: -7px; top: -4px; box-shadow: 0 0 8px #00E5FF;
        }
        .capsule-box {
          display: flex; flex-direction: column; align-items: center; width: 110px;
        }
        .capsule-tube {
          width: 110px; height: 250px; border-radius: 55px; position: relative; overflow: hidden; background: transparent;
          display: flex; justify-content: center; align-items: center;
        }
        .green-btn {
          background: linear-gradient(180deg, rgba(16,185,129,0.2) 0%, rgba(5,150,105,0.6) 100%);
          border: 1px solid #10B981; border-radius: 20px; padding: 6px 12px; color: #FFF; font-size: 11px; font-weight: 900;
          display: flex; align-items: center; gap: 5px; box-shadow: 0 0 15px rgba(16,185,129,0.3);
        }
      `}</style>

      {/* HEADER */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 25, maxWidth: 1400, margin: '0 auto', width: '100%' }}>
        <div>
          <h1 style={{ margin: 0, color: '#FFF', fontSize: 26, fontWeight: '900', letterSpacing: 1, textShadow: '0 0 10px #FFF' }}>CLINIC ANALYTICS & LAB DIAGNOSTICS DASHBOARD</h1>
          <p style={{ margin: '5px 0 0 0', color: '#94A3B8', fontSize: 12, letterSpacing: 1 }}>DATE / 03/23 | 08:30 / TIME</p>
        </div>
        <div style={{ display: 'flex', gap: 10 }}>
          <div style={{ width: 40, height: 40, borderRadius: 8, border: '1px solid #334155', display: 'flex', justifyContent: 'center', alignItems: 'center' }}><span style={{ color: '#00E5FF' }}>⛶</span></div>
          <div style={{ width: 40, height: 40, borderRadius: 8, border: '1px solid #00E5FF', background: 'rgba(0,229,255,0.1)', display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px rgba(0,229,255,0.3)' }}><span style={{ color: '#00E5FF' }}>🔔</span></div>
          <div style={{ width: 40, height: 40, borderRadius: 8, border: '1px solid #334155', display: 'flex', justifyContent: 'center', alignItems: 'center' }}><span style={{ color: '#00E5FF' }}>⚙</span></div>
        </div>
      </div>

      <div style={{ display: 'flex', flexDirection: 'row', gap: 20, maxWidth: 1400, margin: '0 auto', width: '100%' }}>
        
        {/* LEFT PANEL: BLOOD INVENTORY */}
        <div className="hud-border" style={{ flex: 1.2, display: 'flex', flexDirection: 'column' }}>
          <h2 className="hud-header">BLOOD INVENTORY <span style={{ float: 'right', color: '#94A3B8', cursor: 'pointer' }}>✕</span></h2>
          
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '40px 24px', justifyItems: 'center', marginTop: 10 }}>
            {bloodInventory.map((item, idx) => (
              <div key={idx} className="capsule-box" style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: 16 }}>
                
                {/* 1. THE OUTER 3D GLASS CYLINDER */}
                <div style={{
                  position: 'relative',
                  width: 100, 
                  height: 240,
                  borderRadius: 50,
                  background: 'linear-gradient(145deg, rgba(15,23,42,0.5), rgba(2,6,23,0.8))',
                  border: '2px solid rgba(255,255,255,0.15)',
                  boxShadow: 'inset -12px 0 20px rgba(0,0,0,0.8), inset 12px 0 20px rgba(255,255,255,0.15), 0 0 25px rgba(225,29,72,0.2)',
                  overflow: 'hidden'
                }}>
                  
                  {/* 2. THE GLOWING RED LIQUID (Anchored to bottom) */}
                  <div style={{
                    position: 'absolute', 
                    bottom: 0, left: 0, right: 0,
                    height: `${item.percent}%`,
                    background: 'linear-gradient(180deg, #FF1E56 0%, #9F1239 100%)',
                    boxShadow: '0 0 40px rgba(255,30,86,0.6)',
                    borderBottomLeftRadius: 50, 
                    borderBottomRightRadius: 50,
                    transition: 'height 1.5s ease-in-out'
                  }}>
                    {/* 3. THE 3D LIQUID SURFACE (Meniscus / Oval Top) */}
                    <div style={{
                      position: 'absolute', 
                      top: -12, left: 0, right: 0, 
                      height: 24,
                      borderRadius: '50%',
                      background: 'linear-gradient(180deg, #FF718D 0%, #FF1E56 100%)',
                      boxShadow: 'inset 0 2px 6px rgba(255,255,255,0.6)'
                    }} />
                    {/* Bubbles */}
                    {[0,1,2].map(bi => (
                      <div key={bi} style={{ position: 'absolute', bottom: `${10 + bi*20}%`, left: `${25 + (bi*15)%40}%`, width: 6, height: 6, background: 'rgba(255,200,220,0.6)', borderRadius: '50%', animation: `bubbleRise ${2 + bi*0.5}s infinite ${bi*0.3}s` }} />
                    ))}
                  </div>

                  {/* 4. THE 3D GLASS GLARE (Left-side curved reflection) */}
                  <div style={{
                    position: 'absolute', 
                    top: 15, left: 12, 
                    width: 15, bottom: 25,
                    borderRadius: 10,
                    background: 'linear-gradient(90deg, rgba(255,255,255,0.0), rgba(255,255,255,0.25), rgba(255,255,255,0.0))',
                    filter: 'blur(2px)',
                    pointerEvents: 'none'
                  }} />

                  {/* 5. FLOATING DATA OVERLAY */}
                  <div style={{
                    position: 'absolute', top: 0, left: 0, right: 0, bottom: 0,
                    display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
                    zIndex: 10
                  }}>
                    <span style={{ fontSize: 48, fontWeight: '900', color: '#FFFFFF', textShadow: '0 4px 20px rgba(0,0,0,0.9), 0 0 15px rgba(255,255,255,0.4)', letterSpacing: 2 }}>
                      {item.type}
                    </span>
                    <span style={{ fontSize: 15, fontWeight: '700', color: '#F1F5F9', textTransform: 'uppercase', letterSpacing: 1.5, marginTop: 4, textShadow: '0 2px 8px rgba(0,0,0,0.9)' }}>
                      {item.count} Units
                    </span>
                  </div>
                </div>

                {/* 6. BOTTOM PROGRESS / STATUS BAR */}
                <div style={{ width: 100, display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 8 }}>
                  <div style={{ flex: 1, height: 4, background: '#1E293B', borderRadius: 2 }}>
                    <div style={{ width: `${item.percent}%`, height: '100%', background: '#00E5FF', borderRadius: 2, boxShadow: '0 0 10px #00E5FF' }} />
                  </div>
                  <span style={{ color: '#00E5FF', fontSize: 13, fontWeight: 'bold' }}>{item.percent}%</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* RIGHT PANEL */}
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 20 }}>
          
          {/* NEARBY BLOOD BANK */}
          <div className="hud-border" style={{ flex: 1 }}>
            <h2 className="hud-header">NEARBY BLOOD BANK DIRECTORY</h2>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 15 }}>
              {[
                { n: 'City Central Hospital', d: '0.8 mi' }, { n: 'Red Cross Center', d: '1.4 mi' },
                { n: 'St. Jude Lab', d: '2.1 mi' }, { n: 'Metro Blood Bank', d: '3.5 mi' },
                { n: 'Unity Health Center', d: '4.9 mi' }
              ].map(b => (
                <div key={b.n} style={{ background: 'linear-gradient(180deg, rgba(30,41,59,0.8), rgba(15,23,42,0.9))', border: '1px solid #334155', borderRadius: 12, padding: 15 }}>
                  <h4 style={{ margin: '0 0 5px 0', color: '#FFF', fontSize: 13, fontWeight: 'bold' }}>{b.n}</h4>
                  <p style={{ margin: '0 0 10px 0', color: '#94A3B8', fontSize: 11 }}>{b.d}</p>
                  <p style={{ margin: '0 0 5px 0', color: '#10B981', fontSize: 10, fontWeight: 'bold' }}>1-TAP CALL</p>
                  <button className="green-btn">📞 CALL NOW</button>
                </div>
              ))}
            </div>
          </div>

          {/* LAB INPUT PODS */}
          <div className="hud-border" style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 12 }}>
            <h2 className="hud-header">LAB INPUT PODS: PATIENT VITALS</h2>
            
            <div style={{ display: 'flex', gap: 15, height: '100%' }}>
              {/* Left Column of Vitals */}
              <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 12 }}>
                <div style={{ background: 'rgba(30,41,59,0.5)', border: '1px solid #334155', borderRadius: 10, padding: 15 }}>
                  <p style={{ margin: '0 0 5px 0', color: '#00E5FF', fontSize: 11 }}>[PATIENT NAME:</p>
                  <h3 style={{ margin: 0, color: '#FFF', fontSize: 16 }}>{labData?.patient_name || 'Alisha Chen'}</h3>
                </div>
                <div style={{ background: 'rgba(30,41,59,0.5)', border: '1px solid #334155', borderRadius: 10, padding: 15, flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'space-between' }}>
                  <p style={{ margin: 0, color: '#E2E8F0', fontSize: 13, fontWeight: 'bold' }}>2. [TEMP: 98.6 °F]</p>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 15 }}>
                    <div style={{ width: 50, height: 50, borderRadius: 25, border: '2px solid #10B981', display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 15px rgba(16,185,129,0.4)' }}>
                      <span style={{ color: '#10B981', fontSize: 24 }}>📞</span>
                    </div>
                    <div style={{ flex: 1 }}><div className="slider-track"><div className="slider-fill" style={{ width: '40%' }}><div className="slider-knob" /></div></div></div>
                  </div>
                </div>
              </div>

              {/* Right Column of Vitals */}
              <div style={{ flex: 1.2, display: 'flex', flexDirection: 'column', gap: 12 }}>
                <div style={{ background: 'rgba(30,41,59,0.5)', border: '1px solid #334155', borderRadius: 10, padding: 15 }}>
                  <p style={{ margin: '0 0 10px 0', color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>2. [TEMP: 98.6 °F]</p>
                  <div className="slider-track"><div className="slider-fill" style={{ width: '60%' }}><div className="slider-knob" /></div></div>
                </div>
                <div style={{ background: 'rgba(30,41,59,0.5)', border: '1px solid #334155', borderRadius: 10, padding: 15 }}>
                  <p style={{ margin: '0 0 10px 0', color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>3. [BLOOD PRESSURE: 120/80 mmHg]</p>
                  <div style={{ display: 'flex', gap: 10, alignItems: 'center' }}>
                     <div style={{ border: '1px solid #334155', borderRadius: 6, padding: '4px 10px', color: '#FFF' }}>120</div>
                     <span style={{ color: '#94A3B8' }}>/</span>
                     <div style={{ border: '1px solid #334155', borderRadius: 6, padding: '4px 10px', color: '#FFF' }}>80 <span style={{ color: '#94A3B8', fontSize: 10 }}>mmHg</span></div>
                  </div>
                </div>
                <div style={{ background: 'rgba(30,41,59,0.5)', border: '1px solid #334155', borderRadius: 10, padding: 15 }}>
                  <p style={{ margin: '0 0 10px 0', color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>4. [HEART RATE: 72 BPM] <span style={{ color: '#00E5FF', float: 'right' }}>❤</span></p>
                  <div style={{ display: 'flex', gap: 4 }}>
                    {[...Array(30)].map((_, i) => <div key={i} style={{ width: 3, height: 10, background: i < 20 ? '#00E5FF' : '#1E293B', borderRadius: 1 }} />)}
                  </div>
                </div>
                <div style={{ background: 'rgba(30,41,59,0.5)', border: '1px solid #334155', borderRadius: 10, padding: 15 }}>
                  <p style={{ margin: '0 0 10px 0', color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>5. [O2 SAT: 99 %]</p>
                  <svg width="100%" height="25" viewBox="0 0 100 25" preserveAspectRatio="none">
                     <polyline points="0,15 15,15 20,5 25,25 30,15 50,15 55,5 60,25 65,15 100,15" fill="none" stroke="#00E5FF" strokeWidth="1.5" strokeLinejoin="round" />
                  </svg>
                </div>
              </div>
            </div>
            
          </div>
        </div>

      </div>
    </ScrollView>
  );
}
