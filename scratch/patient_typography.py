import os
import re

with open('src/app/patient.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# Smart Pharmacy Timer
old_timer = "<span style={{ color: '#EF4444', fontSize: 16, fontWeight: '900', fontFamily: 'monospace', letterSpacing: 2, animation: 'flashTimer 1s infinite' }}>01:45:20</span>"
new_timer = "<span style={{ color: '#EF4444', fontSize: 24, fontWeight: 'bold', fontFamily: 'monospace', letterSpacing: 4, animation: 'flashTimer 1s infinite' }}>01:45:20</span>"
content = content.replace(old_timer, new_timer)

# Vaayu NutriMed Menu
# Food titles
content = content.replace(
    "<span style={{ color: '#FFF', fontSize: 13, fontWeight: '900' }}>{item.title}</span>",
    "<span style={{ fontSize: 16, fontWeight: 'bold', color: '#F8FAFC' }}>{item.title}</span>"
)
# Macro details
content = content.replace(
    "<span style={{ color: '#64748B', fontSize: 9, fontWeight: 'bold' }}>{item.macros}</span>",
    "<span style={{ fontSize: 12, color: '#64748B', marginTop: 4, letterSpacing: 0.5 }}>{item.macros}</span>"
)

# AI Nutrient Absorption (Ensuring alignment and styles)
old_nutrient_1 = """<div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6 }}>
                      <span style={{ color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Iron Clearance Rate</span>
                      <span style={{ color: '#38BDF8', fontSize: 10, fontWeight: '900' }}>+14% Faster than baseline</span>
                    </div>"""
new_nutrient_1 = """<div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 6 }}>
                      <span style={{ color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Iron Clearance Rate</span>
                      <span style={{ color: '#38BDF8', fontSize: 10, fontWeight: '900' }}>+14% Faster than baseline</span>
                    </div>"""
content = content.replace(old_nutrient_1, new_nutrient_1)

old_nutrient_2 = """<div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: 6 }}>
                      <span style={{ color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Vitamin D Synthesis</span>
                      <span style={{ color: '#FBBF24', fontSize: 10, fontWeight: '900' }}>82% Optimal Absorption</span>
                    </div>"""
new_nutrient_2 = """<div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: 6 }}>
                      <span style={{ color: '#E2E8F0', fontSize: 11, fontWeight: 'bold' }}>Vitamin D Synthesis</span>
                      <span style={{ color: '#FBBF24', fontSize: 10, fontWeight: '900' }}>82% Optimal Absorption</span>
                    </div>"""
content = content.replace(old_nutrient_2, new_nutrient_2)

with open('src/app/patient.tsx', 'w', encoding='utf-8') as f:
    f.write(content)

print("patient.tsx typography updated")
