import os

with open('src/app/dashboard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Locate the block to replace
start_str = "{/* 1. Main Transparent Wrapper */}"
end_str = "{/* Bottom Bar */}"

start_idx = content.find(start_str)
end_idx = content.find(end_str)

new_capsule = """{/* 1. Main Transparent Wrapper */}
                <div style={{ position: 'relative', width: 110, height: 250, display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', backgroundColor: 'transparent' }}>
                  
                  {/* 1. BULLETPROOF SVG GEOMETRIC LIQUID MASK */}
                  <svg width="110" height="250" viewBox="0 0 110 250" style={{ position: 'absolute', top: 0, left: 0 }}>
                    <defs>
                      {/* The Pill Shape Mask */}
                      <clipPath id={`capsule-clip-${idx}`}>
                        <rect x="0" y="0" width="110" height="250" rx="55" ry="55" />
                      </clipPath>
                      {/* The 3D Liquid Gradient */}
                      <linearGradient id={`bloodGrad-${idx}`} x1="0" y1="0" x2="0" y2="1">
                        <stop offset="0%" stopColor="#FF1E56" />
                        <stop offset="40%" stopColor="#E11D48" />
                        <stop offset="100%" stopColor="#7F1D1D" />
                      </linearGradient>
                    </defs>
                    
                    <g clipPath={`url(#capsule-clip-${idx})`}>
                      {/* The Dynamic Liquid Fill */}
                      <rect 
                        x="0" 
                        y={250 - (250 * item.percent / 100)} 
                        width="110" 
                        height={250 * item.percent / 100} 
                        fill={`url(#bloodGrad-${idx})`} 
                      />
                      {/* The 3D Surface Meniscus (Elliptical top of the liquid) */}
                      <ellipse 
                        cx="55" 
                        cy={250 - (250 * item.percent / 100)} 
                        rx="55" 
                        ry="12" 
                        fill="#FF4D6D" 
                      />
                      {/* Bubbles */}
                      {[0,1,2].map(bi => (
                        <circle 
                          key={bi} 
                          cx={25 + (bi*15)%40} 
                          cy={250 - ((250 * item.percent / 100) * (10 + bi*20) / 100)} 
                          r="3" 
                          fill="rgba(255,200,220,0.6)" 
                          style={{ animation: `bubbleRise ${2 + bi*0.5}s infinite ${bi*0.3}s` }} 
                        />
                      ))}
                    </g>
                  </svg>

                  {/* 2. The 3D Glass Reflection Overlay (Placed OVER the SVG) */}
                  <img 
                    src={getUri(GlassCapsuleTube)} 
                    style={{ position: 'absolute', top: 0, left: 0, width: 110, height: 250, objectFit: 'fill', mixBlendMode: 'screen', opacity: 0.95, pointerEvents: 'none' }} 
                    alt="Glass Tube"
                  />

                  {/* 3. The Text Data (Centered on top of everything) */}
                  <div style={{ position: 'absolute', zIndex: 10, textAlign: 'center', textShadow: '0 4px 15px rgba(0,0,0,0.8)' }}>
                     <div style={{ fontSize: 42, fontWeight: '900', color: '#FFF' }}>{item.type}</div>
                     <div style={{ fontSize: 16, color: '#FFF', marginTop: 4 }}>{item.count} Units</div>
                     <div style={{ fontSize: 16, color: '#FFF', fontWeight: 'bold' }}>{item.percent}%</div>
                  </div>
                </div>

                """

content = content[:start_idx] + new_capsule + content[end_idx:]

with open('src/app/dashboard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("dashboard.tsx replaced with SVG capsule code")
