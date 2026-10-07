import os

with open('src/app/explore.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_core = """{/* Center Dark Core */}
            <div style={{ width: 130, height: 130, borderRadius: '50%', background: 'radial-gradient(circle, #061326 65%, #0284C7 100%)', border: '2px solid #38BDF8', boxShadow: '0 0 30px #00E5FF, inset 0 0 20px #00E5FF', zIndex: 10, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
              <span style={{ color: '#FFF', fontSize: 32, fontWeight: 'bold' }}>{patientData?.recovery_insights?.recovery_rate || 83.5}%</span>
              <span style={{ color: '#38BDF8', fontSize: 12, fontWeight: 'bold', textTransform: 'uppercase', textAlign: 'center' }}>Recovery<br/>Index</span>
            </div>"""

new_core = """{/* Center Dark Core (Now Transparent) */}
            <div style={{ zIndex: 10, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
              <span style={{ fontSize: 48, fontWeight: '900', color: '#FFF', textShadow: '0 4px 15px rgba(0,0,0,0.9), 0 0 20px rgba(0, 229, 255, 0.6)' }}>{patientData?.recovery_insights?.recovery_rate || 83.5}%</span>
              <span style={{ fontSize: 14, fontWeight: 'bold', color: '#38BDF8', textTransform: 'uppercase', letterSpacing: 2, marginTop: 4, textShadow: '0 2px 10px rgba(0,0,0,0.9)', textAlign: 'center' }}>Recovery<br/>Index</span>
            </div>"""

content = content.replace(old_core, new_core)

with open('src/app/explore.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("explore.tsx dark core removed")
