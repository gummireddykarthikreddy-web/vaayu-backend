import os

with open('src/app/dashboard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_str = "{bloodInventory.map((item, idx) => ("
end_str = "              ))}
            </div>
          </div>"

start_idx = content.find(start_str)
end_idx = content.find("              ))}") + len("              ))}")

new_map = """{bloodInventory.map((item, idx) => (
              <div key={idx} className="capsule-box">
                {/* 1. Main Transparent Wrapper */}
                <div style={{ position: 'relative', width: 110, height: 250, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
                  
                  {/* 2. STRICT LIQUID CLIPPING MASK (Traps liquid inside the pill shape) */}
                  <div style={{ position: 'absolute', top: 0, left: 0, right: 0, bottom: 0, borderRadius: 55, overflow: 'hidden', transform: 'translateZ(0)' }}>
                     
                     {/* 3. The Red Liquid (Pours strictly inside the mask) */}
                     <div style={{ 
                       position: 'absolute', 
                       bottom: 0, left: 0, width: '100%', 
                       height: `${item.percent}%`, /* Dynamic fill */
                       background: 'linear-gradient(180deg, #FF1E56 0%, #E11D48 40%, #7F1D1D 100%)',
                       animation: 'liquidWave 3s ease-in-out infinite' 
                     }}>
                        {/* Meniscus / Surface of the liquid */}
                        <div style={{ position: 'absolute', top: -12, left: 0, width: '100%', height: 24, borderRadius: '50%', background: 'linear-gradient(180deg, #FF4D6D 0%, #FF1E56 100%)', boxShadow: '0 -4px 15px rgba(255, 77, 109, 0.8)' }} />
                        {/* Bubbles go here */}
                        {[0,1,2].map(bi => (
                          <div key={bi} style={{ position: 'absolute', bottom: `${10 + bi*20}%`, left: `${25 + (bi*15)%40}%`, width: 6, height: 6, background: 'rgba(255,200,220,0.6)', borderRadius: '50%', animation: `bubbleRise ${2 + bi*0.5}s infinite ${bi*0.3}s` }} />
                        ))}
                     </div>
                  </div>

                  {/* 4. The 3D Glass Reflection Overlay (Placed OVER the masked liquid) */}
                  <img 
                    src={getUri(GlassCapsuleTube)} 
                    style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', objectFit: 'fill', mixBlendMode: 'screen', opacity: 0.95, pointerEvents: 'none' }} 
                    alt="Glass Tube"
                  />

                  {/* 5. The Text Data (Centered on top of everything) */}
                  <div style={{ position: 'absolute', zIndex: 10, textAlign: 'center', textShadow: '0 4px 15px rgba(0,0,0,0.8)' }}>
                     <div style={{ fontSize: 42, fontWeight: '900', color: '#FFF' }}>{item.type}</div>
                     <div style={{ fontSize: 16, color: '#FFF', marginTop: 4 }}>{item.count} Units</div>
                     <div style={{ fontSize: 16, color: '#FFF', fontWeight: 'bold' }}>{item.percent}%</div>
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
            ))}"""

content = content[:start_idx] + new_map + content[end_idx:]

with open('src/app/dashboard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("dashboard.tsx strict capsule structure applied successfully")
