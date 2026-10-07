import os

with open('src/app/patient.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add animations to <style>
new_styles = """
        @keyframes drawRing {
          0% { stroke-dasharray: 0, 100; }
          100% { stroke-dasharray: 75, 100; }
        }
        @keyframes pulseLive {
          0% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0.7); }
          70% { box-shadow: 0 0 0 10px rgba(16, 185, 129, 0); }
          100% { box-shadow: 0 0 0 0 rgba(16, 185, 129, 0); }
        }
"""
content = content.replace("        @keyframes ecgPulse {", new_styles + "        @keyframes ecgPulse {")


# 2. Add Feature 1 & 2
new_modules = """
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
"""

search_str = "        </div>\n\n        {/* RIGHT COLUMN */}"
content = content.replace(search_str, new_modules + "\n        </div>\n\n        {/* RIGHT COLUMN */}")

with open('src/app/patient.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("patient.tsx final left column features added successfully")
