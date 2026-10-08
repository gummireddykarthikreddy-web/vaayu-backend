import os
import glob

# Files to update
files = glob.glob('src/**/*.tsx', recursive=True) + glob.glob('src/**/*.ts', recursive=True)

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'http://127.0.0.1:8000' in content or 'http://localhost:10000' in content or 'http://127.0.0.1:10000' in content:
        content = content.replace('http://127.0.0.1:8000', 'https://vaayu-backend-ulzh.onrender.com')
        content = content.replace('http://localhost:10000', 'https://vaayu-backend-ulzh.onrender.com')
        content = content.replace('http://127.0.0.1:10000', 'https://vaayu-backend-ulzh.onrender.com')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")

print("Replacement complete.")
