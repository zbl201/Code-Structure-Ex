import os
import shutil
import pandas as pd
import json
import inspect


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
        
        
        
def testprint(df: pd.DataFrame, filetype: str = '.txt'):
    """
    Flexible test printing for intra-pipeline and intra-processing df checks. 
    """
    valid_filetypes = ['.txt','.csv']
    if filetype not in valid_filetypes:
        raise Exception('Invalid filetype.')
    
    ## Logic for getting module name and function name ## Make its own function
    # frame = inspect.currentframe().f_back  # go one frame back to the caller
    # func_name = frame.f_code.co_name
    # module = inspect.getmodule(frame)
    # module_name = module.__name__ if module else "<unknown module>"
    # print(f"In module: {module_name}, in function: {func_name}")
    
    ## Logic for getting proper output path name
    
    ## Filepath changing logic?
    
    if filetype== '.txt':
        with open(f'data/checks/file.txt','w') as file:
            file.write(df.to_string())
            
    if filetype=='.csv':
        df.to_csv('data/checks/file.csv',index=False)


def testprint_dict(d: dict, filetype: str = '.txt'):
    """
    Flexible test printing for intra-pipeline and intra-processing dictionary checks. 
    """
    pass