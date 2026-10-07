import os

with open('src/app/explore.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_keyframes = """@keyframes fireCrownUp {
          0%, 100% { transform: translateY(-16px) scaleX(1.15) scaleY(1.4) rotate(0deg); opacity: 0.9; }
          50% { transform: translateY(-30px) scaleX(1.28) scaleY(1.6) rotate(-18deg); opacity: 1; filter: brightness(1.8) drop-shadow(0 -20px 35px #38BDF8); }
        }"""
new_keyframes = """@keyframes firePulseRound {
          0%, 100% { transform: scale(1.2); opacity: 0.8; filter: brightness(1.5) drop-shadow(0 0 20px #38BDF8); }
          50% { transform: scale(1.35); opacity: 1; filter: brightness(1.8) drop-shadow(0 0 40px #00E5FF); }
        }"""
content = content.replace(old_keyframes, new_keyframes)

old_orb_container = """<div style={{ position: 'relative', width: 300, height: 300, display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto' }}>
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

            {/* Center Dark Core (Now Transparent) */}
            <div style={{ zIndex: 10, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
              <span style={{ fontSize: 48, fontWeight: '900', color: '#FFF', textShadow: '0 4px 15px rgba(0,0,0,0.9), 0 0 20px rgba(0, 229, 255, 0.6)' }}>{patientData?.recovery_insights?.recovery_rate || 83.5}%</span>
              <span style={{ fontSize: 14, fontWeight: 'bold', color: '#38BDF8', textTransform: 'uppercase', letterSpacing: 2, marginTop: 4, textShadow: '0 2px 10px rgba(0,0,0,0.9)', textAlign: 'center' }}>Recovery<br/>Index</span>
            </div>

            <div style={{ position: 'absolute', top: 0, left: -40, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'left', fontWeight: 'bold' }}>Post-Op Vital<br/>Monitoring</div>
            <div style={{ position: 'absolute', top: 0, right: -40, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'right', fontWeight: 'bold' }}>Cellular<br/>Status</div>
            <div style={{ position: 'absolute', bottom: 0, left: -40, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'left', fontWeight: 'bold' }}>Neurological<br/>Feedback</div>
            <div style={{ position: 'absolute', bottom: 0, right: -40, color: '#94A3B8', fontSize: 12, width: 100, textAlign: 'right', fontWeight: 'bold' }}>Healing<br/>Progress</div>
          </div>"""

new_orb_container = """<div style={{ position: 'relative', width: 300, height: 300, minWidth: 300, minHeight: 300, display: 'flex', alignItems: 'center', justifyContent: 'center', margin: 'auto', alignSelf: 'center' }}>
            {/* Layer 1: Spinning Perfect Circle */}
            <img 
              src={getUri(BurningBlueFireOrb)} 
              className="orb-mask" 
              style={{ position: 'absolute', width: 260, height: 260, objectFit: 'contain', animation: 'fireSpinOuter 10s linear infinite', pointerEvents: 'none' }} 
              alt="Spinning Flame"
            />

            {/* Layer 2: Pulsing Perfect Circle (Replaced the elongating crown) */}
            <img 
              src={getUri(BurningBlueFireOrb)} 
              className="orb-mask" 
              style={{ position: 'absolute', width: 260, height: 260, objectFit: 'contain', animation: 'firePulseRound 4s ease-in-out infinite', pointerEvents: 'none' }} 
              alt="Pulsing Flame"
            />

            {/* Floating Text (No Background) */}
            <div style={{ zIndex: 10, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
              <span style={{ fontSize: 48, fontWeight: '900', color: '#FFF', textShadow: '0 4px 15px rgba(0,0,0,0.9), 0 0 20px rgba(0, 229, 255, 0.6)' }}>{patientData?.recovery_insights?.recovery_rate || 83.5}%</span>
              <span style={{ fontSize: 14, fontWeight: 'bold', color: '#38BDF8', textTransform: 'uppercase', letterSpacing: 2, marginTop: 4, textShadow: '0 2px 10px rgba(0,0,0,0.9)' }}>RECOVERY INDEX</span>
            </div>

            {/* Corner Labels */}
            <span style={{ position: 'absolute', top: 0, left: -20, color: '#94A3B8', fontSize: 12, fontWeight: 'bold' }}>Post-Op Vital Monitoring</span>
            <span style={{ position: 'absolute', top: 0, right: -20, color: '#94A3B8', fontSize: 12, fontWeight: 'bold' }}>Cellular Status</span>
            <span style={{ position: 'absolute', bottom: 0, left: -20, color: '#94A3B8', fontSize: 12, fontWeight: 'bold' }}>Neurological Feedback</span>
            <span style={{ position: 'absolute', bottom: 0, right: -20, color: '#94A3B8', fontSize: 12, fontWeight: 'bold' }}>Healing Progress</span>
          </div>"""

# Fallback string replace just in case the previous indentation was slightly different
if old_orb_container not in content:
    # Let's use a regex or replace parts
    pass

content = content.replace(old_orb_container, new_orb_container)

with open('src/app/explore.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("explore.tsx round orb fixed")
