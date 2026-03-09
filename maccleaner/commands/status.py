import os
import shutil
from utils import get_size, format_size

def show_status():
    print("💾 Disk Usage Status\n")
    
    usage = shutil.disk_usage('/')
    total = usage.total
    used = usage.used
    free = usage.free
    
    print(f"Total:     {format_size(total)}")
    print(f"Used:      {format_size(used)}")
    print(f"Free:      {format_size(free)}")
    print(f"Usage:     {(used/total)*100:.1f}%\n")
    
    paths = [
        ('Home', os.path.expanduser('~')),
        ('Downloads', os.path.expanduser('~/Downloads')),
        ('Desktop', os.path.expanduser('~/Desktop')),
        ('Documents', os.path.expanduser('~/Documents')),
        ('Caches', os.path.expanduser('~/Library/Caches')),
        ('Logs', os.path.expanduser('~/Library/Logs')),
    ]
    
    print("Top directories in home:")
    sizes = []
    for name, path in paths:
        if os.path.exists(path):
            size = get_size(path)
            sizes.append((name, size, path))
    
    sizes.sort(key=lambda x: x[1], reverse=True)
    for name, size, path in sizes:
        print(f"  {name:15} {format_size(size):>10}")
