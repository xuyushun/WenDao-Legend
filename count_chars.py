import os
import glob

def count_chars_in_volume(volume_path):
    total_chars = 0
    file_count = 0
    files = glob.glob(os.path.join(volume_path, "ch*.md"))
    
    print(f"Found {len(files)} files in {volume_path}")
    
    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Basic character count, including punctuation and whitespace
            # For Chinese novels, typically all characters are counted.
            total_chars += len(content)
            file_count += 1
            
    return total_chars, file_count

volume_2_path = "/workspaces/WenDao-Legend/drafts/volume_02"
chars, count = count_chars_in_volume(volume_2_path)

print(f"Total files: {count}")
print(f"Total characters: {chars}")
