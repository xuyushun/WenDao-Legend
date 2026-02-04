import os
import re

drafts_dir = 'drafts/volume_01'
files = sorted([f for f in os.listdir(drafts_dir) if f.endswith('.md')])

# Pattern for "(第X章·完)" or similar
end_pattern = re.compile(r'（.*第.*章.*[完].*）', re.MULTILINE)

print(f"{'Filename':<35} | {'Analysis'}")
print("-" * 80)

for filename in files:
    if 'outline' in filename or 'chapter_list' in filename or 'chapter_status' in filename:
        continue
        
    filepath = os.path.join(drafts_dir, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = list(end_pattern.finditer(content))
    if matches:
        last_match = matches[-1]
        end_pos = last_match.end()
        remaining_content = content[end_pos:].strip()
        
        if remaining_content:
            snippet = remaining_content[:50].replace('\n', ' ')
            print(f"{filename:<35} | FOUND END MARKER + EXTRA CONTENT")
            print(f"{' ':<35} | Marker: {last_match.group()}")
            print(f"{' ':<35} | Extra: {snippet}...")
            
            # Check if headers exist in the extra content, implying a merged chapter
            if '#' in remaining_content:
                 print(f"{' ':<35} | WARNING: Headers found in extra content!")
        else:
             print(f"{filename:<35} | Clean end.")
    else:
        print(f"{filename:<35} | No end marker found.")
