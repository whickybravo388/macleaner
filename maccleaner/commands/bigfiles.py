import os
from utils import get_size, format_size

def find_bigfiles(min_size_mb=100):
    print(f"🔍 Searching for files larger than {min_size_mb}MB...")
    min_size = min_size_mb * 1024 * 1024
    results = []
    
    search_paths = [
        os.path.expanduser('~'),
        '/Users/Shared',
    ]
    
    for base_path in search_paths:
        if not os.path.exists(base_path):
            continue
            
        for root, dirs, files in os.walk(base_path):
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            
            for f in files:
                try:
                    fp = os.path.join(root, f)
                    size = os.path.getsize(fp)
                    if size >= min_size:
                        results.append((fp, size))
                except:
                    pass
    
    results.sort(key=lambda x: x[1], reverse=True)
    
    print(f"\nFound {len(results)} large files:\n")
    for path, size in results[:20]:
        print(f"  {format_size(size)} - {path}")
