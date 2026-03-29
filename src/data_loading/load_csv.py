import pandas as pd
from pathlib import Path


def load_csv_file(file_path):
    df = pd.read_csv(file_path)
    return df



def load_india_commodity_prices():
    '''
    Loading all csv files in data/raw/inidia_commodity_prices directory
    '''
    raw_path = 'data/raw/india_commodity_prices'
    dir = Path(raw_path)
    
    if dir.is_dir():
        ## Grabbing CSV files
        csv_files = dir.glob('*.csv')
        df_list = [pd.read_csv(f).assign(Source_File=f.name) for f in csv_files]
        
        ## Concatenating with pd.concat
        if df_list:
            combined_df = pd.concat(df_list, ignore_index=True)
            print(f"Successfully concatenated {len(df_list)} files.")
            return combined_df
        else: 
            print("No CSV files found in the directory.")
            return pd.DataFrame()
        
    else:
        print(f'Data path {raw_path} does not exist.')
        return pd.DataFrame()
    