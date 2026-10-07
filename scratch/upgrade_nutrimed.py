import os

with open('src/app/patient.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

start_str = "{/* NUTRIMED DELIVERY */}"
end_str = "{/* HAZARD MATRIX */}"

start_idx = content.find(start_str)
end_idx = content.find(end_str)

new_nutrimed = """{/* NUTRIMED DELIVERY */}
          <div className="bento-card" style={{ flex: 1, padding: 0, overflow: 'hidden', display: 'flex', flexDirection: 'column', position: 'relative' }}>
            <div style={{ padding: '25px 25px 15px 25px', zIndex: 10, background: '#131C2D' }}>
              <h2 className="bento-title" style={{ marginBottom: 0 }}>Vaayu NutriMed Delivery</h2>
            </div>
            
            <div className="nutrimed-scroll" style={{ flex: 1, overflowY: 'auto', padding: '0 25px 100px 25px' }}>
              <style>{`
                .nutrimed-scroll::-webkit-scrollbar { display: none; }
                .nutrimed-scroll { -ms-overflow-style: none; scrollbar-width: none; }
              `}</style>

              {/* TOP BANNER */}
              <div style={{ width: '100%', height: 80, borderRadius: 12, overflow: 'hidden', position: 'relative', marginBottom: 20, boxShadow: '0 10px 20px rgba(0,0,0,0.5)' }}>
                <img src={getUri(GoldTreasureCard)} style={{ width: '100%', height: '100%', objectFit: 'cover', opacity: 0.8 }} />
                <div style={{ position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', padding: 15, display: 'flex', flexDirection: 'column', justifyContent: 'center', background: 'linear-gradient(90deg, rgba(0,0,0,0.8) 0%, rgba(0,0,0,0.2) 100%)' }}>
                  <h3 style={{ margin: 0, color: '#FDE047', fontSize: 14, fontWeight: '900', textShadow: '0 2px 4px rgba(0,0,0,0.8)' }}>Vaayu Seva Golden Balance: Active</h3>
                  <p style={{ margin: '4px 0 0 0', color: '#FFF', fontSize: 11, fontWeight: 'bold', letterSpacing: 1 }}>Free Clinical Delivery Applied</p>
                </div>
              </div>

              {/* MENU ITEMS */}
              {[
                { 
                  title: 'Sun-Dried Mushroom Detox Bowl', price: '₹240', 
                  badge: '☀️ Targets Low Vitamin D', badgeCol: '#FDE047',
                  desc: 'Rich in Vitamin D2, aiding in optimal calcium absorption and bone recovery post-surgery.', 
                  macros: '280 kcal | 14g Protein', icon: '🥗' 
                },
                { 
                  title: 'Low-Iron Pearl Millet Khichdi', price: '₹120', 
                  badge: '🩸 Balances High Iron', badgeCol: '#FF2A5F',
                  desc: 'Curated to provide sustained energy without excess iron accumulation.', 
                  macros: '320 kcal | 12g Protein', icon: '🍲' 
                },
                { 
                  title: 'Immunity Citrus Cold-Press', price: '₹180', 
                  badge: '🛡️ Enhances Recovery', badgeCol: '#10B981',
                  desc: 'High concentration of Vitamin C and antioxidants to reduce oxidative stress.', 
                  macros: '110 kcal | 2g Protein', icon: '🥤' 
                }
              ].map((item, i) => (
                <div key={i} style={{ background: 'linear-gradient(145deg, rgba(30,41,59,0.7), rgba(15,23,42,0.9))', border: '1px solid rgba(255,255,255,0.1)', borderRadius: 16, padding: 12, marginBottom: 15, display: 'flex', flexDirection: 'row', alignItems: 'center', gap: 15, boxShadow: '0 5px 15px rgba(0,0,0,0.3)' }}>
                  
                  {/* Left Icon */}
                  <div style={{ minWidth: 70, width: 70, height: 70, borderRadius: 35, background: '#0F172A', display: 'flex', justifyContent: 'center', alignItems: 'center', border: '1px solid rgba(255,255,255,0.1)', boxShadow: 'inset 0 0 15px rgba(255,255,255,0.05)', fontSize: 32 }}>
                    {item.icon}
                  </div>
                  
                  {/* Middle Details */}
                  <div style={{ flex: 1, display: 'flex', flexDirection: 'column', gap: 4 }}>
                    <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                      <span style={{ color: '#FFF', fontSize: 13, fontWeight: '900' }}>{item.title}</span>
                      <span style={{ color: '#E2E8F0', fontSize: 13, fontWeight: 'bold' }}>{item.price}</span>
                    </div>
                    
                    <div style={{ alignSelf: 'flex-start', background: item.badgeCol + '20', border: '1px solid ' + item.badgeCol, borderRadius: 10, padding: '2px 8px', display: 'inline-block' }}>
                      <span style={{ color: item.badgeCol, fontSize: 9, fontWeight: 'bold' }}>{item.badge}</span>
                    </div>
                    
                    <span style={{ color: '#94A3B8', fontSize: 10, lineHeight: 1.3 }}>{item.desc}</span>
                    <span style={{ color: '#64748B', fontSize: 9, fontWeight: 'bold' }}>{item.macros}</span>
                  </div>
                  
                  {/* Right Button */}
                  <div style={{ background: 'linear-gradient(180deg, #10B981, #059669)', borderRadius: 10, padding: '8px 12px', boxShadow: '0 4px 10px rgba(16,185,129,0.4)', cursor: 'pointer', whiteSpace: 'nowrap' }}>
                    <span style={{ color: '#FFF', fontSize: 11, fontWeight: '900' }}>+ ADD</span>
                  </div>
                </div>
              ))}
            </div>
            
            {/* CHECKOUT BAR */}
            <div style={{ position: 'absolute', bottom: 0, left: 0, width: '100%', padding: '15px 25px', background: 'linear-gradient(0deg, #131C2D 70%, rgba(19,28,45,0) 100%)', zIndex: 20 }}>
              <div style={{ width: '100%', background: 'linear-gradient(180deg, #10B981, #059669)', borderRadius: 12, padding: 15, display: 'flex', justifyContent: 'center', alignItems: 'center', boxShadow: '0 0 20px rgba(16,185,129,0.5)', cursor: 'pointer', border: '1px solid #34D399' }}>
                <span style={{ color: '#FFF', fontSize: 14, fontWeight: '900', letterSpacing: 1, textShadow: '0 2px 4px rgba(0,0,0,0.5)' }}>PLACE CLINICAL ORDER</span>
              </div>
            </div>
          </div>

          """

new_content = content[:start_idx] + new_nutrimed + content[end_idx:]

with open('src/app/patient.tsx', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("patient.tsx NutriMed updated successfully")
