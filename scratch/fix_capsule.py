import os

with open('src/app/dashboard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Strip styling from capsule-tube CSS
old_css = """        .capsule-tube {
          width: 110px; height: 250px; border-radius: 55px; background: #0A1220; position: relative; overflow: hidden;
          border: 1px solid rgba(255,255,255,0.1); box-shadow: 0 0 40px rgba(225, 29, 72, 0.4);
          display: flex; justify-content: center; align-items: center;
        }"""
new_css = """        .capsule-tube {
          width: 110px; height: 250px; border-radius: 55px; position: relative; overflow: hidden; background: transparent;
          display: flex; justify-content: center; align-items: center;
        }"""

content = content.replace(old_css, new_css)


# 2. Extract and replace the rendering of the capsule
old_capsule = """                  <div className="capsule-tube">
                    {/* Liquid Fill */}
                    <div style={{ position: 'absolute', bottom: 0, left: 0, right: 0, height: `${item.percent}%`, background: 'linear-gradient(180deg, #FF1E56 0%, #E11D48 40%, #7F1D1D 100%)', borderBottomLeftRadius: 55, borderBottomRightRadius: 55 }}>
                      {/* The Meniscus */}
                      <div style={{ position: 'absolute', top: -12, left: 0, width: '100%', height: 24, borderRadius: '50%', background: 'linear-gradient(180deg, #FF4D6D 0%, #FF1E56 100%)', boxShadow: '0 -4px 15px rgba(255, 77, 109, 0.8), inset 0 2px 5px rgba(255,255,255,0.5)', animation: 'liquidWave 3s ease-in-out infinite' }} />
                      {[0,1,2].map(bi => (
                        <div key={bi} style={{ position: 'absolute', bottom: `${10 + bi*20}%`, left: `${25 + (bi*15)%40}%`, width: 6, height: 6, background: 'rgba(255,200,220,0.6)', borderRadius: '50%', animation: `bubbleRise ${2 + bi*0.5}s infinite ${bi*0.3}s` }} />
                      ))}
                    </div>
                    
                    {/* Transparent Capsule Image Overlay */}
                    <img src={getUri(GlassCapsuleTube)} style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', objectFit: 'fill', mixBlendMode: 'screen', opacity: 0.9, pointerEvents: 'none', zIndex: 5 }} />
                    
                    {/* Text Overlay */}
                    <div style={{ zIndex: 10, textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100%' }}>
                      <h3 style={{ margin: 0, color: '#FFF', fontSize: 42, fontWeight: '900', textShadow: '0 4px 15px rgba(0,0,0,0.6)' }}>{item.type}</h3>
                      <p style={{ margin: '5px 0 0 0', color: '#FFF', fontSize: 16, fontWeight: 'bold', textShadow: '0 2px 5px rgba(0,0,0,0.8)' }}>{item.count}</p>
                      <p style={{ margin: 0, color: '#E2E8F0', fontSize: 12, textShadow: '0 2px 5px rgba(0,0,0,0.8)' }}>Units</p>
                      <p style={{ margin: '4px 0 0 0', color: '#FFF', fontSize: 16, fontWeight: 'bold', textShadow: '0 2px 5px rgba(0,0,0,0.8)' }}>{item.percent}%</p>
                    </div>
                  </div>"""

new_capsule = """                  <div style={{ width: 110, height: 250, borderRadius: 55, overflow: 'hidden', position: 'relative', backgroundColor: 'transparent' }}>
                    {/* Liquid Fill */}
                    <div style={{ position: 'absolute', bottom: 0, left: 0, width: '100%', height: `${item.percent}%`, background: 'linear-gradient(180deg, #FF1E56 0%, #E11D48 40%, #7F1D1D 100%)' }}>
                      {/* The Meniscus */}
                      <div style={{ position: 'absolute', top: -12, left: 0, width: '100%', height: 24, borderRadius: '50%', background: 'linear-gradient(180deg, #FF4D6D 0%, #FF1E56 100%)', boxShadow: '0 -4px 15px rgba(255, 77, 109, 0.8), inset 0 2px 5px rgba(255,255,255,0.5)', animation: 'liquidWave 3s ease-in-out infinite' }} />
                      {[0,1,2].map(bi => (
                        <div key={bi} style={{ position: 'absolute', bottom: `${10 + bi*20}%`, left: `${25 + (bi*15)%40}%`, width: 6, height: 6, background: 'rgba(255,200,220,0.6)', borderRadius: '50%', animation: `bubbleRise ${2 + bi*0.5}s infinite ${bi*0.3}s` }} />
                      ))}
                    </div>
                    
                    {/* Transparent Capsule Image Overlay */}
                    <img src={getUri(GlassCapsuleTube)} style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', objectFit: 'fill', mixBlendMode: 'screen', opacity: 0.9, pointerEvents: 'none' }} />
                    
                    {/* Text Overlay */}
                    <div style={{ position: 'absolute', zIndex: 10, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', width: '100%', height: '100%' }}>
                      <h3 style={{ margin: 0, color: '#FFF', fontSize: 42, fontWeight: '900', textShadow: '0 4px 15px rgba(0,0,0,0.6)' }}>{item.type}</h3>
                      <p style={{ margin: '5px 0 0 0', color: '#FFF', fontSize: 16, fontWeight: 'bold', textShadow: '0 2px 5px rgba(0,0,0,0.8)' }}>{item.count}</p>
                      <p style={{ margin: 0, color: '#E2E8F0', fontSize: 12, textShadow: '0 2px 5px rgba(0,0,0,0.8)' }}>Units</p>
                      <p style={{ margin: '4px 0 0 0', color: '#FFF', fontSize: 16, fontWeight: 'bold', textShadow: '0 2px 5px rgba(0,0,0,0.8)' }}>{item.percent}%</p>
                    </div>
                  </div>"""

content = content.replace(old_capsule, new_capsule)

with open('src/app/dashboard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("dashboard.tsx outer boxes removed successfully")
