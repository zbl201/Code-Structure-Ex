import os
import shutil
import pandas as pd
import json



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
                #print(f"Removed: {pycache_path}")
            
            pycache_count += 1

    if dry_run:
        print(f"\nTotal __pycache__ folders found: {pycache_count}")
    else: 
        print(f"\nTotal __pycache__ folders removed: {pycache_count}")
        
        
        
def testprint(df: pd.DataFrame, filename = 'test', filetype: str = '.txt'):
    """
    Flexible test printing for intra-pipeline and intra-processing dataframe checks. 
    """
    valid_filetypes = ['.txt','.csv']
    if filetype not in valid_filetypes:
        raise Exception('Invalid filetype.')
    
    if filetype== '.txt':
        with open(f'data/test/{filename}.txt','w') as file:
            file.write(df.to_string(index=False))
            
    if filetype=='.csv':
        df.to_csv(f'data/test/{filename}.csv',index=False)


def testprint_dict(data: dict, filename = 'test_dict'):
    """
    Flexible test printing for intra-pipeline and intra-processing dictionary checks. 
    """
    with open(f'data/test/{filename}.txt','w') as f:
        json.dump(data, f, indent=4)