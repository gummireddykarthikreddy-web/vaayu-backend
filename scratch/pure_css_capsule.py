import os

with open('src/app/dashboard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_str = "{bloodInventory.map((item, idx) => ("
end_str = "              ))}\n            </div>\n          </div>"

start_idx = content.find(start_str)
end_idx = content.find("              ))}") + len("              ))}")

new_map = """{bloodInventory.map((item, idx) => (
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
                    <span style={{ fontSize: 44, fontWeight: '900', color: '#FFF', textShadow: '0 4px 15px rgba(0,0,0,0.9), 0 0 10px rgba(255,30,86,0.5)' }}>
                      {item.type}
                    </span>
                    <span style={{ fontSize: 16, fontWeight: '700', color: '#E2E8F0', marginTop: 8, textShadow: '0 2px 8px rgba(0,0,0,0.9)' }}>
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
            ))}"""

content = content[:start_idx] + new_map + content[end_idx:]

with open('src/app/dashboard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("dashboard.tsx updated with pure CSS sci-fi pillars")
