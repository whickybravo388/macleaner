import os
import shutil
from utils import get_size, format_size, confirm

TRASH_PATHS = [
    os.path.expanduser('~/.Trash'),
]

def clean_trash(force=False):
    print("🗑️ Emptying Trash...")
    total_freed = 0
    
    for path in TRASH_PATHS:
        if os.path.exists(path):
            size = get_size(path)
            print(f"  {path}: {format_size(size)}")
            
            if force or confirm("Empty Trash?"):
                for item in os.listdir(path):
                    item_path = os.path.join(path, item)
                    try:
                        if os.path.isdir(item_path):
                            shutil.rmtree(item_path)
                        else:
                            os.remove(item_path)
                        print(f"    Removed: {item}")
                        total_freed += get_size(item_path)
                    except Exception as e:
                        print(f"    Error: {e}")
    
    print(f"\n✅ Total freed: {format_size(total_freed)}")
