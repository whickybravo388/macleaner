import os
import hashlib
from utils import format_size

def find_duplicates():
    print("🔍 Searching for duplicate files (by hash)...")
    hash_map = {}
    duplicates = []
    
    home = os.path.expanduser('~')
    
    for root, dirs, files in os.walk(home):
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for f in files:
            try:
                fp = os.path.join(root, f)
                size = os.path.getsize(fp)
                
                if size < 1024:
                    continue
                    
                with open(fp, 'rb') as fh:
                    h = hashlib.md5(fh.read()).hexdigest()
                    
                key = (size, h)
                if key in hash_map:
                    duplicates.append((fp, hash_map[key]))
                else:
                    hash_map[key] = fp
            except:
                pass
    
    if duplicates:
        total_dup_size = 0
        print(f"\nFound {len(duplicates)} duplicate files:\n")
        for dup, original in duplicates:
            size = os.path.getsize(dup)
            total_dup_size += size
            print(f"  {format_size(size)}")
            print(f"    Original: {original}")
            print(f"    Duplicate: {dup}\n")
        print(f"Total recoverable: {format_size(total_dup_size)}")
    else:
        print("No duplicates found.")
