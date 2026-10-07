import os

with open('src/app/patient.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Mojibake safely if it exists (but we will just rewrite the file content if possible, wait, I can just replace specific strings, actually it's easier to just use standard replacements).
# I won't worry too much about Mojibake right now if the app compiles, but I'll fix the currency symbol.
content = content.replace(",1", "₹")
content = content.replace(",149", "₹49")
content = content.replace(",1240", "₹240")
content = content.replace(",1120", "₹120")
content = content.replace(",1180", "₹180")
content = content.replace("dY\"", "📦")
content = content.replace("dY\"o", "📜")

# 1. Add keyframes
new_styles = """
        * { box-sizing: border-box; }
        @keyframes ecgPulse {
          0% { stroke-dashoffset: 200; opacity: 0.2; }
          50% { opacity: 1; filter: drop-shadow(0 0 8px #00E5FF); }
          100% { stroke-dashoffset: 0; opacity: 0.2; }
        }
        @keyframes flashTimer {
          0%, 100% { opacity: 1; text-shadow: 0 0 15px rgba(239,68,68,0.8); }
          50% { opacity: 0.6; text-shadow: 0 0 5px rgba(239,68,68,0.3); }
        }
"""
content = content.replace("* { box-sizing: border-box; }", new_styles)


# 2. Add AI Smart Pharmacy Module
pharmacy_module = """
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
                <span style={{ color: '#EF4444', fontSize: 16, fontWeight: '900', fontFamily: 'monospace', letterSpacing: 2, animation: 'flashTimer 1s infinite' }}>01:45:20</span>
              </div>
            </div>

            {/* Nurse Button */}
            <div style={{ width: '100%', background: 'linear-gradient(180deg, #EF4444, #B91C1C)', borderRadius: 12, padding: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 20px rgba(239,68,68,0.5)', cursor: 'pointer', border: '1px solid #F87171' }}>
              <span style={{ color: '#FFF', fontSize: 14, fontWeight: '900', letterSpacing: 1, textShadow: '0 2px 4px rgba(0,0,0,0.5)' }}>🏥 REQUEST NURSE ASSISTANCE</span>
            </div>
          </div>
"""

# We need to find the end of the left column.
# Let's locate "{/* RIGHT COLUMN */}" and insert pharmacy_module right before its preceding </div>.
idx = content.find("{/* RIGHT COLUMN */}")
if idx != -1:
    # go back to find the closing div of the left column
    pre_text = content[:idx]
    post_text = content[idx:]
    
    # Actually, the structure is:
    #       </div>
    #     </div>
    # 
    #   </div>
    # 
    #   {/* RIGHT COLUMN */}
    # 
    # Let's just do a manual replace matching the exact whitespace near {/* RIGHT COLUMN */}
    
    search_str = "        </div>\n\n        {/* RIGHT COLUMN */}"
    replace_str = pharmacy_module + "\n        </div>\n\n        {/* RIGHT COLUMN */}"
    content = content.replace(search_str, replace_str)


with open('src/app/patient.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("patient.tsx left column telemetry and keyframes added successfully")
