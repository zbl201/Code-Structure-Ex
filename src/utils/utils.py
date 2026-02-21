import os
import shutil

def clear_pycache(root_dir: str, dry_run: bool = False):
    """
    Recursively delete all __pycache__ directories under root_dir.
    """
    pycache_count = 0

    for dirpath, dirnames, filenames in os.walk(root_dir):
        if "__pycache__" in dirnames:
            pycache_path = os.path.join(dirpath, "__pycache__")
            
            if dry_run:
                print(f"[DRY RUN] Would remove: {pycache_path}")
            else: 
                shutil.rmtree(pycache_path)
                print(f"Removed: {pycache_path}")
            
            pycache_count += 1

    if dry_run:
        print(f"\nTotal __pycache__ folders found: {pycache_count}")
    else: 
        print(f"\nTotal __pycache__ folders removed: {pycache_count}")
        
