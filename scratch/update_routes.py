import os

with open('src/app/index.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("router.push('/patient')", "router.push('/patient-login')")
content = content.replace("router.push('/explore')", "router.push('/doctor-login')")

with open('src/app/index.tsx', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.tsx routes")
