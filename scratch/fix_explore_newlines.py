import os

with open('src/app/explore.tsx', 'r', encoding='utf-8') as f:
    code = f.read()

code = code.replace("Pain\\nManagement", "Pain Management")
code = code.replace("Pain\nManagement", "Pain Management")

code = code.replace("Anti-\\ninflammatory", "Anti-inflammatory")
code = code.replace("Anti-\ninflammatory", "Anti-inflammatory")

code = code.replace("Recovery\\nAids", "Recovery Aids")
code = code.replace("Recovery\nAids", "Recovery Aids")

code = code.replace("Specialized\\nMedication", "Specialized Medication")
code = code.replace("Specialized\nMedication", "Specialized Medication")

with open('src/app/explore.tsx', 'w', encoding='utf-8') as f:
    f.write(code)

print("Fixed newlines in explore.tsx")
