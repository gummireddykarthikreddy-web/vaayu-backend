import os

with open('src/app/explore.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "return ("
end_marker = ");"

start_idx = content.find(start_marker)
end_idx = content.rfind(end_marker) + len(end_marker)

new_return = """return (
    <ScrollView style={{ flex: 1, backgroundColor: '#020617' }}>
      <style>{`
        .glass-tablet {
          transform: perspective(1000px) rotateY(15deg) rotateX(5deg);
          box-shadow: -20px 20px 40px rgba(225,29,72,0.2);
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
        .ai-panel {
          background: rgba(30,41,59,0.7); border: 1px solid rgba(255,255,255,0.1); border-radius: 16px; padding: 20px;
          backdrop-filter: blur(15px); margin-bottom: 20px;
        }
      `}</style>
      
      {/* PERFECT 2x2 GRID */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '40px', padding: '40px', backgroundColor: '#020617', minHeight: '100vh' }}>
        
        {/* QUADRANT 1: Pre-Surgery Safety & Infection Shield (Crimson Glass Tablet) */}
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
          <div className="glass-tablet" style={{ position: 'relative', width: 400, height: 480, display: 'flex', flexDirection: 'column', padding: 35, background: 'linear-gradient(135deg, rgba(30,41,59,0.8), rgba(15,23,42,0.95))', border: '1px solid rgba(255,42,95,0.3)' }}>
            <img src={getUri(GlassCardSlab)} style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', objectFit: 'cover', opacity: 0.1, borderRadius: 20 }} />
            <div style={{ zIndex: 10, flex: 1, display: 'flex', flexDirection: 'column' }}>
              <h3 style={{ textTransform: 'uppercase', letterSpacing: 1.5, color: '#FECDD3', textShadow: '0 0 10px rgba(251,113,133,0.5)', fontSize: 24, fontWeight: '900', lineHeight: 1.2, marginBottom: 25 }}>Pre-Surgery Safety &<br/>Infection Shield</h3>
              <p style={{ margin: '0 0 10px 0', color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>Infection Risks</p>
              <div style={{ display: 'flex', justifyContent: 'space-between', padding: '15px 20px', background: 'rgba(0,0,0,0.3)', borderRadius: 12, border: '1px solid rgba(255,42,95,0.2)', marginBottom: 20 }}>
                <div className="gauge-circle" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}><span style={{ color: '#FFF', fontSize: 28, fontWeight: '900' }}>85%</span></div>
                <div className="gauge-circle" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}><span style={{ color: '#FFF', fontSize: 28, fontWeight: '900' }}>85%</span></div>
                <div className="gauge-circle" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}><span style={{ color: '#FFF', fontSize: 28, fontWeight: '900' }}>85%</span></div>
              </div>
              <div style={{ display: 'flex', gap: 15, flex: 1 }}>
                <div style={{ flex: 1, background: 'rgba(0,0,0,0.3)', borderRadius: 12, padding: 15, border: '1px solid rgba(255,42,95,0.2)' }}>
                  <p style={{ margin: '0 0 10px 0', color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Safety Protocols</p>
                  <ul style={{ margin: 0, paddingLeft: 16, lineHeight: 1.6, color: '#E2E8F0', fontSize: 14 }}>
                    <li>Airflow Isolation</li>
                    <li>Sterilization Lock</li>
                  </ul>
                </div>
                <div style={{ flex: 1, background: 'rgba(0,0,0,0.3)', borderRadius: 12, padding: 15, border: '1px solid rgba(255,42,95,0.2)' }}>
                  <p style={{ margin: '0 0 10px 0', color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Patient Vitals</p>
                  <div style={{ width: '100%', height: 6, background: '#334155', borderRadius: 3, marginBottom: 10 }}><div style={{ width: '80%', height: '100%', background: '#FF2A5F', borderRadius: 3 }} /></div>
                  <div style={{ width: '100%', height: 6, background: '#334155', borderRadius: 3 }}><div style={{ width: '50%', height: '100%', background: '#00E5FF', borderRadius: 3 }} /></div>
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* QUADRANT 2: Doctor's Pre-Surgery Preventive Measures (Obsidian & Gold Tablet) */}
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
          <div className="slab-obsidian" style={{ position: 'relative', width: 400, height: 480, display: 'flex', flexDirection: 'column', padding: 35, background: 'linear-gradient(135deg, rgba(30,41,59,0.9), rgba(5,11,20,0.95))', border: '1px solid rgba(245,158,11,0.4)' }}>
            <img src={getUri(ObsidianGoldSlab)} style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', objectFit: 'cover', opacity: 0.3, mixBlendMode: 'screen', borderRadius: 20 }} />
            <div style={{ zIndex: 10, flex: 1, display: 'flex', flexDirection: 'column' }}>
              <h3 style={{ color: '#FFF', fontSize: 22, fontWeight: '900', lineHeight: 1.3, textAlign: 'center', marginBottom: 25 }}>Doctor's Pre-Surgery<br/>Preventive Measures</h3>
              <div style={{ flex: 1, display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '8px 0', background: 'transparent', border: 'none' }}>
                  <div style={{ width: 18, height: 18, borderRadius: 9, background: 'radial-gradient(circle, #FDE047, #F59E0B)', display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px #F59E0B' }}><span style={{ color: '#000', fontSize: 10, fontWeight: 'bold' }}>✓</span></div>
                  <span style={{ color: '#F8FAFC', fontSize: 15, fontWeight: '600', letterSpacing: 0.5 }}>Verify Patient Identity</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '8px 0', background: 'transparent', border: 'none' }}>
                  <div style={{ width: 18, height: 18, borderRadius: 9, background: 'radial-gradient(circle, #FDE047, #F59E0B)', display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px #F59E0B' }}><span style={{ color: '#000', fontSize: 10, fontWeight: 'bold' }}>✓</span></div>
                  <span style={{ color: '#F8FAFC', fontSize: 15, fontWeight: '600', letterSpacing: 0.5 }}>Confirm Surgical Site</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '8px 0', background: 'transparent', border: 'none' }}>
                  <div style={{ width: 18, height: 18, borderRadius: 9, background: 'radial-gradient(circle, #FDE047, #F59E0B)', display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px #F59E0B' }}><span style={{ color: '#000', fontSize: 10, fontWeight: 'bold' }}>✓</span></div>
                  <span style={{ color: '#F8FAFC', fontSize: 15, fontWeight: '600', letterSpacing: 0.5 }}>Review Medical History</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '8px 0', background: 'transparent', border: 'none' }}>
                  <div style={{ width: 18, height: 18, borderRadius: 9, background: 'radial-gradient(circle, #FDE047, #F59E0B)', display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px #F59E0B' }}><span style={{ color: '#000', fontSize: 10, fontWeight: 'bold' }}>✓</span></div>
                  <span style={{ color: '#F8FAFC', fontSize: 15, fontWeight: '600', letterSpacing: 0.5 }}>Administer Prophylactic Antibiotics</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '8px 0', background: 'transparent', border: 'none' }}>
                  <div style={{ width: 18, height: 18, borderRadius: 9, background: 'radial-gradient(circle, #FDE047, #F59E0B)', display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px #F59E0B' }}><span style={{ color: '#000', fontSize: 10, fontWeight: 'bold' }}>✓</span></div>
                  <span style={{ color: '#F8FAFC', fontSize: 15, fontWeight: '600', letterSpacing: 0.5 }}>Check Equipment Functionality</span>
                </div>
              </div>
              <div style={{ width: '100%', height: 6, background: '#1E293B', borderRadius: 3, marginTop: 10, position: 'relative' }}>
                <div style={{ width: '80%', height: '100%', background: '#F59E0B', borderRadius: 3, boxShadow: '0 0 10px #F59E0B' }} />
                <span style={{ position: 'absolute', right: 0, top: 15, color: '#FACC15', fontWeight: 'bold', textShadow: '0 0 8px #FACC15', fontSize: 14 }}>80%</span>
              </div>
            </div>
          </div>
        </div>

        {/* QUADRANT 3: 3D Blue Flame Recovery Orb */}
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ position: 'relative', width: 300, height: 300, borderRadius: '50%', display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'radial-gradient(circle, rgba(0,229,255,0.1) 0%, rgba(0,0,0,0) 70%)', boxShadow: '0 0 30px rgba(0,229,255,0.1)' }}>
            <img src={getUri(BurningBlueFireOrb)} style={{ position: 'absolute', width: '120%', height: '120%', objectFit: 'contain', pointerEvents: 'none' }} />
            
            <div style={{ zIndex: 10, textAlign: 'center', background: 'rgba(0,0,0,0.6)', padding: 30, borderRadius: '50%', boxShadow: '0 0 20px rgba(0,229,255,0.2)', border: '1px solid rgba(0,229,255,0.3)' }}>
              <div style={{ margin: 0, color: '#FFF', fontSize: 48, fontWeight: '900', textShadow: '0 0 20px #00E5FF' }}>{patientData?.recovery_insights?.recovery_rate || 92}%</div>
              <div style={{ margin: '5px 0 0 0', color: '#E2E8F0', fontSize: 13, letterSpacing: 1, fontWeight: 'bold' }}>Recovery Index</div>
            </div>

            <div style={{ position: 'absolute', top: 0, left: -40, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'left', fontWeight: 'bold' }}>Post-Op Vital<br/>Monitoring</div>
            <div style={{ position: 'absolute', top: 0, right: -40, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'right', fontWeight: 'bold' }}>Cellular<br/>Status</div>
            <div style={{ position: 'absolute', bottom: 0, left: -40, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'left', fontWeight: 'bold' }}>Neurological<br/>Feedback</div>
            <div style={{ position: 'absolute', bottom: 0, right: -40, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'right', fontWeight: 'bold' }}>Healing<br/>Progress</div>
          </div>
        </div>

        {/* QUADRANT 4: AI Clinical Summary + 5-Category Prescription Composer */}
        <div style={{ display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
          <div style={{ background: 'linear-gradient(145deg, rgba(30,41,59,0.7), rgba(15,23,42,0.9))', borderRadius: 24, border: '1px solid rgba(255,255,255,0.1)', padding: 24, boxShadow: '0 10px 30px rgba(0,0,0,0.5)', width: '100%', maxWidth: 450, margin: '0 auto' }}>
            
            <div style={{ fontSize: 18, fontWeight: 'bold', color: '#38BDF8', marginBottom: 12 }}>AI Clinical Summary</div>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 15, marginBottom: 25 }}>
              <div>
                <p style={{ margin: '0 0 10px 0', color: '#94A3B8', fontSize: 12 }}>? Synthesized key points</p>
                <p style={{ margin: '0 0 10px 0', color: '#94A3B8', fontSize: 12 }}>? Confirmed Medical History</p>
              </div>
              <div>
                <p style={{ margin: '0 0 10px 0', color: '#94A3B8', fontSize: 12 }}>? Recommendations preserving</p>
                <p style={{ margin: '0 0 10px 0', color: '#94A3B8', fontSize: 12 }}>? Recommendations recovery</p>
              </div>
            </div>

            <div style={{ fontSize: 18, fontWeight: 'bold', color: '#38BDF8', marginBottom: 16 }}>3D Prescription Composer</div>
            <div style={{ display: 'flex', gap: 12, justifyContent: 'space-between' }}>
              <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
                <div style={{ width: 44, height: 44, borderRadius: 12, background: '#F43F5E20', border: '1px solid #F43F5E', display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: 8, boxShadow: '0 0 10px #F43F5E40' }}><span style={{ fontSize: 20 }}>💊</span></div>
                <span style={{ color: '#94A3B8', fontSize: 10 }}>Pain<br/>Mgmt</span>
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
                <div style={{ width: 44, height: 44, borderRadius: 12, background: '#3B82F620', border: '1px solid #3B82F6', display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: 8, boxShadow: '0 0 10px #3B82F640' }}><span style={{ fontSize: 20 }}>💊</span></div>
                <span style={{ color: '#94A3B8', fontSize: 10 }}>Antibiotics</span>
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
                <div style={{ width: 44, height: 44, borderRadius: 12, background: '#F9731620', border: '1px solid #F97316', display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: 8, boxShadow: '0 0 10px #F9731640' }}><span style={{ fontSize: 20 }}>💊</span></div>
                <span style={{ color: '#94A3B8', fontSize: 10 }}>Anti-inflam</span>
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
                <div style={{ width: 44, height: 44, borderRadius: 12, background: '#10B98120', border: '1px solid #10B981', display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: 8, boxShadow: '0 0 10px #10B98140' }}><span style={{ fontSize: 20 }}>💊</span></div>
                <span style={{ color: '#94A3B8', fontSize: 10 }}>Recovery</span>
              </div>
              <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', textAlign: 'center' }}>
                <div style={{ width: 44, height: 44, borderRadius: 12, background: '#8B5CF620', border: '1px solid #8B5CF6', display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: 8, boxShadow: '0 0 10px #8B5CF640' }}><span style={{ fontSize: 20 }}>💊</span></div>
                <span style={{ color: '#94A3B8', fontSize: 10 }}>Specialized</span>
              </div>
            </div>
            
          </div>
        </div>

      </div>
    </ScrollView>
  );"""

content = content[:start_idx] + new_return + content[end_idx:]

with open('src/app/explore.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("explore.tsx rewritten perfectly as 2x2 grid without markdown.")
