import os
import re

with open('src/app/explore.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Crimson Glass Tablet Header
old_header = "<h3 style={{ color: '#FFF', fontSize: 24, fontWeight: '900', lineHeight: 1.2, textShadow: '0 0 10px #FF2A5F', marginBottom: 25 }}>Pre-Surgery Safety &<br/>Infection Shield</h3>"
new_header = "<h3 style={{ textTransform: 'uppercase', letterSpacing: 1.5, color: '#FECDD3', textShadow: '0 0 10px rgba(251,113,133,0.5)', fontSize: 24, fontWeight: '900', lineHeight: 1.2, marginBottom: 25 }}>Pre-Surgery Safety &<br/>Infection Shield</h3>"
content = content.replace(old_header, new_header)

# 2. Inside the 3 Risk Rings
old_gauge = """<div className="gauge-circle"><span style={{ color: '#FFF', fontSize: 13, fontWeight: 'bold' }}>85%</span></div>"""
new_gauge = """<div className="gauge-circle" style={{ display: 'flex', alignItems: 'center', justifyContent: 'center' }}><span style={{ color: '#FFF', fontSize: 28, fontWeight: '900' }}>85%</span></div>"""
content = content.replace(old_gauge, new_gauge)

# 3. Safety Protocols list
old_safety = """<div style={{ flex: 1, background: 'rgba(0,0,0,0.3)', borderRadius: 12, padding: 15, border: '1px solid rgba(255,42,95,0.2)' }}>
                      <p style={{ margin: '0 0 10px 0', color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Safety Protocols</p>
                      <div style={{ width: '80%', height: 6, background: '#334155', borderRadius: 3, marginBottom: 10 }}><div style={{ width: '60%', height: '100%', background: '#E2E8F0', borderRadius: 3 }} /></div>
                      <div style={{ width: '80%', height: 6, background: '#334155', borderRadius: 3 }}><div style={{ width: '40%', height: '100%', background: '#E2E8F0', borderRadius: 3 }} /></div>
                    </div>"""
new_safety = """<div style={{ flex: 1, background: 'rgba(0,0,0,0.3)', borderRadius: 12, padding: 15, border: '1px solid rgba(255,42,95,0.2)' }}>
                      <p style={{ margin: '0 0 10px 0', color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Safety Protocols</p>
                      <ul style={{ margin: 0, paddingLeft: 16, lineHeight: 1.6, color: '#E2E8F0', fontSize: 14 }}>
                        <li>Airflow Isolation</li>
                        <li>Sterilization Lock</li>
                      </ul>
                    </div>"""
content = content.replace(old_safety, new_safety)

# 4. Obsidian & Gold Checklist
old_check_item = """<div className="check-item"><div style={{ width: 18, height: 18, borderRadius: 9, background: 'radial-gradient(circle, #FDE047, #F59E0B)', marginRight: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px #F59E0B' }}><span style={{ color: '#000', fontSize: 10, fontWeight: 'bold' }}>✓</span></div><span style={{ color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>"""
new_check_item = """<div className="check-item" style={{ display: 'flex', alignItems: 'center', gap: 12, padding: '8px 0', background: 'transparent', border: 'none', marginBottom: 0 }}><div style={{ width: 18, height: 18, borderRadius: 9, background: 'radial-gradient(circle, #FDE047, #F59E0B)', display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 10px #F59E0B' }}><span style={{ color: '#000', fontSize: 10, fontWeight: 'bold' }}>✓</span></div><span style={{ color: '#F8FAFC', fontSize: 15, fontWeight: '600', letterSpacing: 0.5 }}>"""
content = content.replace(old_check_item, new_check_item)

# 5. The 80% on the progress bar
old_80 = """<span style={{ position: 'absolute', right: 0, top: 15, color: '#E2E8F0', fontSize: 12, fontWeight: 'bold' }}>80%</span>"""
new_80 = """<span style={{ position: 'absolute', right: 0, top: 15, color: '#FACC15', fontWeight: 'bold', textShadow: '0 0 8px #FACC15', fontSize: 14 }}>80%</span>"""
content = content.replace(old_80, new_80)

# 6. AI Clinical Summary
content = content.replace(
    "<p style={{ margin: '0 0 5px 0', color: '#E2E8F0', fontSize: 11 }}>",
    "<p style={{ margin: '0 0 10px 0', color: '#94A3B8', fontSize: 12 }}>"
)
content = content.replace(
    "<p style={{ margin: 0, color: '#E2E8F0', fontSize: 11 }}>",
    "<p style={{ margin: '0 0 10px 0', color: '#94A3B8', fontSize: 12 }}>"
)

with open('src/app/explore.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("explore.tsx updated")
