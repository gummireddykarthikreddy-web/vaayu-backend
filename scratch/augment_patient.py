import os

with open('src/app/patient.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add Budget Box
budget_box = """
              {/* BUDGET BOX */}
              <div style={{ background: 'linear-gradient(145deg, rgba(180,83,9,0.25), rgba(120,53,15,0.75))', border: '1px solid rgba(251,191,36,0.4)', borderRadius: 16, padding: 14, marginBottom: 16, display: 'flex', alignItems: 'center', gap: 15, boxShadow: '0 5px 15px rgba(0,0,0,0.3)' }}>
                <div style={{ fontSize: 32, textShadow: '0 0 10px rgba(251,191,36,0.8)' }}>📦</div>
                <div style={{ flex: 1 }}>
                  <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 4 }}>
                    <span style={{ color: '#FFF', fontSize: 14, fontWeight: '900' }}>₹49 Compact Clinical Budget Box</span>
                    <span style={{ background: 'rgba(251,191,36,0.2)', color: '#FBBF24', fontSize: 9, fontWeight: 'bold', padding: '2px 8px', borderRadius: 10, border: '1px solid #FBBF24' }}>💛 Subsidized Seva Tier</span>
                  </div>
                  <span style={{ color: '#E2E8F0', fontSize: 10 }}>Standardized daily macros (600 kcal | 20g Protein) for accessible healing.</span>
                </div>
                <div style={{ background: 'linear-gradient(180deg, #F59E0B, #B45309)', borderRadius: 10, padding: '8px 16px', boxShadow: '0 4px 10px rgba(245,158,11,0.4)', cursor: 'pointer' }}>
                  <span style={{ color: '#FFF', fontSize: 12, fontWeight: '900' }}>+ ADD</span>
                </div>
              </div>
"""

top_banner_end = "Free Clinical Delivery Applied</p>\n                </div>\n              </div>"
content = content.replace(top_banner_end, top_banner_end + "\n" + budget_box)


# 2. Update Checkout Bar
old_checkout = """<div style={{ width: '100%', background: 'linear-gradient(180deg, #10B981, #059669)', borderRadius: 12, padding: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 20px rgba(16,185,129,0.5)', cursor: 'pointer', border: '1px solid #34D399' }}>
                <span style={{ color: '#FFF', fontSize: 14, fontWeight: '900', letterSpacing: 1, textShadow: '0 2px 4px rgba(0,0,0,0.5)' }}>PLACE CLINICAL ORDER</span>
              </div>"""

new_checkout = """<div style={{ display: 'flex', gap: 12, width: '100%' }}>
                <div style={{ flex: 1, background: 'linear-gradient(180deg, #10B981, #059669)', borderRadius: 12, padding: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 20px rgba(16,185,129,0.5)', cursor: 'pointer', border: '1px solid #34D399' }}>
                  <span style={{ color: '#FFF', fontSize: 13, fontWeight: '900', letterSpacing: 1, textShadow: '0 2px 4px rgba(0,0,0,0.5)' }}>PLACE CLINICAL ORDER</span>
                </div>
                <div style={{ flex: 1, background: 'linear-gradient(145deg, #1E293B, #0F172A)', borderRadius: 12, padding: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', border: '1px solid rgba(255,255,255,0.2)', cursor: 'pointer', boxShadow: '0 4px 10px rgba(0,0,0,0.5)' }}>
                  <span style={{ color: '#94A3B8', fontSize: 11, fontWeight: '900', letterSpacing: 1 }}>📜 VIEW FULL CLINICAL MENU</span>
                </div>
              </div>"""

content = content.replace(old_checkout, new_checkout)


# 3. Add AI Analysis Module
analysis_module = """
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
                  <div style={{ width: '100%', height: 8, background: '#0F172A', borderRadius: 4, overflow: 'hidden', border: '1px solid rgba(56,189,248,0.2)' }}>
                    <div style={{ width: '75%', height: '100%', background: 'linear-gradient(90deg, #0369A1, #38BDF8)', boxShadow: '0 0 10px rgba(56,189,248,0.8)' }} />
                  </div>
                </div>

                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6 }}>
                    <span style={{ color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Vitamin D Synthesis</span>
                    <span style={{ color: '#FBBF24', fontSize: 10, fontWeight: '900' }}>82% Optimal Absorption</span>
                  </div>
                  <div style={{ width: '100%', height: 8, background: '#0F172A', borderRadius: 4, overflow: 'hidden', border: '1px solid rgba(251,191,36,0.2)' }}>
                    <div style={{ width: '82%', height: '100%', background: 'linear-gradient(90deg, #B45309, #FBBF24)', boxShadow: '0 0 10px rgba(251,191,36,0.8)' }} />
                  </div>
                </div>

                <div>
                  <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6 }}>
                    <span style={{ color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Cellular Regeneration</span>
                    <span style={{ color: '#4ADE80', fontSize: 10, fontWeight: '900' }}>91% Tissue Repair</span>
                  </div>
                  <div style={{ width: '100%', height: 8, background: '#0F172A', borderRadius: 4, overflow: 'hidden', border: '1px solid rgba(74,222,128,0.2)' }}>
                    <div style={{ width: '91%', height: '100%', background: 'linear-gradient(90deg, #166534, #4ADE80)', boxShadow: '0 0 10px rgba(74,222,128,0.8)' }} />
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
                  <span style={{ color: '#FFF', fontSize: 12, fontWeight: '900', textShadow: '0 0 5px rgba(56,189,248,0.5)' }}>[⚡] Intensive Nutrient Loading (Day 7)</span>
                </div>
                <div style={{ display: 'flex', alignItems: 'center', gap: 12 }}>
                  <div style={{ minWidth: 12, width: 12, height: 12, borderRadius: 6, border: '2px solid #475569', background: 'transparent' }} />
                  <span style={{ color: '#475569', fontSize: 12, fontWeight: 'bold' }}>[⏳] Target Peak Immunity (Day 14)</span>
                </div>
              </div>

            </div>
          </div>
"""

hazard_matrix_end = """</div>\n          </div>"""
# Replace the very last occurrence of the hazard matrix end block inside the right column.
# The hazard matrix is the last block in that column.
# Let's find the hazard matrix bento card end.
last_bento_end = content.rfind("</div>\n          </div>")
if last_bento_end != -1:
    content = content[:last_bento_end] + "</div>\n          </div>\n" + analysis_module + content[last_bento_end+len("</div>\n          </div>"):]

with open('src/app/patient.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("patient.tsx augmented with new analysis and budget box successfully")
