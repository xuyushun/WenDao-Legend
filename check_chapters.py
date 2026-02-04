import os
import re

drafts_dir = 'drafts/volume_01'

files = sorted([f for f in os.listdir(drafts_dir) if f.endswith('.md')])

header_pattern = re.compile(r'^#\s+第.*章.*', re.MULTILINE)

for filename in files:
    filepath = os.path.join(drafts_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    headers = header_pattern.findall(content)
    if len(headers) > 1:
        print(f"File: {filename} has {len(headers)} headers:")
        for h in headers:
            print(f"  {h.strip()}")
            
    if len(headers) == 0:
        print(f"File: {filename} has NO headers.")
