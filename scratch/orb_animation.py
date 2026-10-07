import os

with open('src/app/explore.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

keyframes = """<style>{`
        @keyframes fireSpinOuter {
          0% { transform: scale(1.25) rotate(0deg); filter: brightness(1.35) contrast(1.45) drop-shadow(0 0 25px #00E5FF); }
          50% { transform: scale(1.38) rotate(180deg); filter: brightness(1.65) contrast(1.6) drop-shadow(0 0 45px #00E5FF); }
          100% { transform: scale(1.25) rotate(360deg); filter: brightness(1.35) contrast(1.45) drop-shadow(0 0 25px #00E5FF); }
        }
        @keyframes fireCrownUp {
          0%, 100% { transform: translateY(-16px) scaleX(1.15) scaleY(1.4) rotate(0deg); opacity: 0.9; }
          50% { transform: translateY(-30px) scaleX(1.28) scaleY(1.6) rotate(-18deg); opacity: 1; filter: brightness(1.8) drop-shadow(0 -20px 35px #38BDF8); }
        }
        .orb-mask {
          mix-blend-mode: screen;
          -webkit-mask-image: radial-gradient(circle, rgba(0,0,0,1) 38%, rgba(0,0,0,0.6) 54%, rgba(0,0,0,0) 68%);
          mask-image: radial-gradient(circle, rgba(0,0,0,1) 38%, rgba(0,0,0,0.6) 54%, rgba(0,0,0,0) 68%);
        }
        .glass-tablet {"""

content = content.replace("<style>{`\n        .glass-tablet {", keyframes)


old_quadrant_3 = """{/* QUADRANT 3: 3D Blue Flame Recovery Orb */}
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
        </div>"""

new_quadrant_3 = """{/* QUADRANT 3: 3D Blue Flame Recovery Orb */}
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
          <div style={{ position: 'relative', width: 300, height: 300, display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto' }}>
            {/* Layer 1: Spinning Ring */}
            <img 
              src={getUri(BurningBlueFireOrb)} 
              className="orb-mask" 
              style={{ position: 'absolute', width: 260, height: 260, objectFit: 'contain', animation: 'fireSpinOuter 10s linear infinite', pointerEvents: 'none' }} 
              alt="Spinning Flame"
            />
            {/* Layer 2: Roaring Upward Crown */}
            <img 
              src={getUri(BurningBlueFireOrb)} 
              className="orb-mask" 
              style={{ position: 'absolute', width: 260, height: 260, objectFit: 'contain', animation: 'fireCrownUp 4s ease-in-out infinite', pointerEvents: 'none' }} 
              alt="Roaring Flame"
            />

            {/* Center Dark Core */}
            <div style={{ width: 130, height: 130, borderRadius: '50%', background: 'radial-gradient(circle, #061326 65%, #0284C7 100%)', border: '2px solid #38BDF8', boxShadow: '0 0 30px #00E5FF, inset 0 0 20px #00E5FF', zIndex: 10, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
              <span style={{ color: '#FFF', fontSize: 32, fontWeight: 'bold' }}>{patientData?.recovery_insights?.recovery_rate || 83.5}%</span>
              <span style={{ color: '#38BDF8', fontSize: 12, fontWeight: 'bold', textTransform: 'uppercase', textAlign: 'center' }}>Recovery<br/>Index</span>
            </div>

            <div style={{ position: 'absolute', top: 0, left: -40, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'left', fontWeight: 'bold' }}>Post-Op Vital<br/>Monitoring</div>
            <div style={{ position: 'absolute', top: 0, right: -40, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'right', fontWeight: 'bold' }}>Cellular<br/>Status</div>
            <div style={{ position: 'absolute', bottom: 0, left: -40, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'left', fontWeight: 'bold' }}>Neurological<br/>Feedback</div>
            <div style={{ position: 'absolute', bottom: 0, right: -40, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'right', fontWeight: 'bold' }}>Healing<br/>Progress</div>
          </div>
        </div>"""

content = content.replace(old_quadrant_3, new_quadrant_3)

with open('src/app/explore.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("explore.tsx animations restored")
