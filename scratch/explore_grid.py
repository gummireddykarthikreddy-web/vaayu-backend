import os
import re

with open('src/app/explore.tsx', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Grid structure replacement
old_container = "<div style={{ padding: 40, backgroundColor: '#020617', minHeight: '100vh', display: 'flex', flexDirection: 'column' }}>"
new_container = "<div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '40px', padding: '40px', backgroundColor: '#020617', minHeight: '100vh' }}>"
content = content.replace(old_container, new_container)

# Remove row wrappers
content = content.replace("{/* ROW 1 */}", "")
content = content.replace("<div style={{ display: 'flex', flexDirection: 'row', gap: 60 }}>", "")
content = content.replace("{/* ROW 2 */}", "")
content = content.replace("<div style={{ display: 'flex', flexDirection: 'row', gap: 60, marginTop: 20 }}>", "")
# We need to remove the closing </div> for ROW 1 and ROW 2.
# We will do this via regex or manual search since there are multiple closing divs.
# Actually, rebuilding the return statement is safer. Let's do that.

