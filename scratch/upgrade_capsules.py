import os

with open('src/app/dashboard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS styles for .capsule-box and .capsule-tube
old_css = """        .capsule-box {
          display: flex; flex-direction: column; align-items: center; width: 90px;
        }
        .capsule-tube {
          width: 70px; height: 170px; border-radius: 35px; background: #0A1220; position: relative; overflow: hidden;
          border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 15px 30px rgba(255,42,95,0.2);
          display: flex; justify-content: center; align-items: center;
        }"""

new_css = """        .capsule-box {
          display: flex; flex-direction: column; align-items: center; width: 110px;
        }
        .capsule-tube {
          width: 110px; height: 250px; border-radius: 55px; background: #0A1220; position: relative; overflow: hidden;
          border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 0 40px rgba(225, 29, 72, 0.4);
          display: flex; justify-content: center; align-items: center;
        }"""

content = content.replace(old_css, new_css)

# 2. Extract and replace the entire grid
start_str = "<div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '30px 20px', justifyItems: 'center', marginTop: 10 }}>"
end_str = "          </div>\n        </div>\n\n        {/* RIGHT PANEL */}"

start_idx = content.find(start_str)
end_idx = content.find(end_str)

new_grid = """<div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '40px 24px', justifyItems: 'center', marginTop: 10 }}>
            {bloodInventory.map((item, idx) => (
              <div key={idx} className="capsule-box">
                <div className="capsule-tube">
                  {/* Liquid Fill */}
                  <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, height: `${item.percent}%`, background: 'linear-gradient(180deg, #FF1E56 0%, #E11D48 40%, #7F1D1D 100%)', borderBottomLeftRadius: 55, borderBottomRightRadius: 55 }}>
                    {/* The Meniscus */}
                    <div style={{ position: 'absolute', top: -12, left: 0, width: '100%', height: 24, borderRadius: '50%', background: 'linear-gradient(180deg, #FF4D6D 0%, #FF1E56 100%)', boxShadow: '0 -4px 15px rgba(255, 77, 109, 0.8), inset 0 2px 5px rgba(255,255,255,0.5)', animation: 'liquidWave 3s ease-in-out infinite' }} />
                    {[0,1,2].map(bi => (
                      <div key={bi} style={{ position: 'absolute', bottom: `${10 + bi*20}%`, left: `${25 + (bi*15)%40}%`, width: 6, height: 6, background: 'rgba(255,200,220,0.6)', borderRadius: '50%', animation: `bubbleRise ${2 + bi*0.5}s infinite ${bi*0.3}s` }} />
                    ))}
                  </div>
                  
                  {/* Transparent Capsule Image Overlay */}
                  <img src={getUri(GlassCapsuleTube)} style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', objectFit: 'stretch', mixBlendMode: 'screen', opacity: 0.9, pointerEvents: 'none', zIndex: 5 }} />
                  
                  {/* Text Overlay */}
                  <div style={{ zIndex: 10, textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100%' }}>
                    <h3 style={{ margin: 0, color: '#FFF', fontSize: 42, fontWeight: '900', textShadow: '0 4px 15px rgba(0,0,0,0.6)' }}>{item.type}</h3>
                    <p style={{ margin: '5px 0 0 0', color: '#FFF', fontSize: 16, fontWeight: 'bold', textShadow: '0 2px 5px rgba(0,0,0,0.8)' }}>{item.count}</p>
                    <p style={{ margin: 0, color: '#E2E8F0', fontSize: 12, textShadow: '0 2px 5px rgba(0,0,0,0.8)' }}>Units</p>
                    <p style={{ margin: '4px 0 0 0', color: '#FFF', fontSize: 16, fontWeight: 'bold', textShadow: '0 2px 5px rgba(0,0,0,0.8)' }}>{item.percent}%</p>
                  </div>
                </div>

                {/* Bottom Bar */}
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', width: '110px', marginTop: 16 }}>
                  <span style={{ color: '#00E5FF', fontSize: 12, fontWeight: 'bold', textShadow: '0 0 5px rgba(0,229,255,0.5)' }}>{item.type}</span>
                  <div style={{ flex: 1, margin: '0 10px', height: 4, background: '#1E293B', borderRadius: 2 }}>
                    <div style={{ width: `${item.percent}%`, height: '100%', background: '#00E5FF', borderRadius: 2, boxShadow: '0 0 8px #00E5FF' }} />
                  </div>
                  <span style={{ color: '#00E5FF', fontSize: 12, fontWeight: 'bold', textShadow: '0 0 5px rgba(0,229,255,0.5)' }}>{item.percent}%</span>
                </div>
              </div>
            ))}
"""
content = content[:start_idx] + new_grid + content[end_idx:]

with open('src/app/dashboard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("dashboard.tsx capsules enlarged successfully")
