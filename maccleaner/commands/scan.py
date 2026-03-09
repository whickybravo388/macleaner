import os
from utils import get_size, format_size

CATEGORIES = {
    'Caches': [
        os.path.expanduser('~/Library/Caches'),
        '/Library/Caches',
    ],
    'Logs': [
        os.path.expanduser('~/Library/Logs'),
        '/var/log',
    ],
    'Xcode DerivedData': [
        os.path.expanduser('~/Library/Developer/Xcode/DerivedData'),
    ],
    'Xcode Archives': [
        os.path.expanduser('~/Library/Developer/Xcode/Archives'),
    ],
    'Trash': [
        os.path.expanduser('~/.Trash'),
    ],
}

def scan_system():
    print("🔍 Scanning system for cleanable files...\n")
    
    total = 0
    for category, paths in CATEGORIES.items():
        cat_size = 0
        for path in paths:
            if os.path.exists(path):
                cat_size += get_size(path)
        
        if cat_size > 0:
            print(f"  {category:20} {format_size(cat_size):>10}")
            total += cat_size
    
    print(f"\n{'='*35}")
    print(f"  Total cleanable:    {format_size(total)}")
    print(f"\nRun 'maccleaner clean <category>' to clean")
    print(f"Run 'maccleaner clean all' to clean everything")
