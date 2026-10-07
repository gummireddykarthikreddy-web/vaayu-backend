import os

with open('src/app/dashboard.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

old_type = "<span style={{ fontSize: 44, fontWeight: '900', color: '#FFF', textShadow: '0 4px 15px rgba(0,0,0,0.9), 0 0 10px rgba(255,30,86,0.5)' }}>\n                      {item.type}\n                    </span>"
new_type = "<span style={{ fontSize: 48, fontWeight: '900', color: '#FFFFFF', textShadow: '0 4px 20px rgba(0,0,0,0.9), 0 0 15px rgba(255,255,255,0.4)', letterSpacing: 2 }}>\n                      {item.type}\n                    </span>"
content = content.replace(old_type, new_type)

old_units = "<span style={{ fontSize: 16, fontWeight: '700', color: '#E2E8F0', marginTop: 8, textShadow: '0 2px 8px rgba(0,0,0,0.9)' }}>\n                      {item.count} Units\n                    </span>"
new_units = "<span style={{ fontSize: 15, fontWeight: '700', color: '#F1F5F9', textTransform: 'uppercase', letterSpacing: 1.5, marginTop: 4, textShadow: '0 2px 8px rgba(0,0,0,0.9)' }}>\n                      {item.count} Units\n                    </span>"
content = content.replace(old_units, new_units)

with open('src/app/dashboard.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("dashboard.tsx updated")
