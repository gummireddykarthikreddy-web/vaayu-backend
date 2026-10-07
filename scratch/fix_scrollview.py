import os

files = ['src/app/patient-login.tsx', 'src/app/doctor-login.tsx', 'src/app/doctor-patient-select.tsx']

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove ScrollView import
    content = content.replace("import { ScrollView } from 'react-native';\n", "")
    
    # Replace <ScrollView contentContainerStyle=...> with <div style=...>
    content = content.replace("<ScrollView contentContainerStyle=", "<div style=")
    
    # Replace </ScrollView> with </div>
    content = content.replace("</ScrollView>", "</div>")
    
    # Also add overflow: auto to the div style
    content = content.replace("backgroundColor: '#020617' }", "backgroundColor: '#020617', overflowY: 'auto' }")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Removed ScrollView from all new pages")
