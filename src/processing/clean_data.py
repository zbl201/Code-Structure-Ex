import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # do something
    
    # drop nulls
    df = df.dropna(axis=0,ignore_index=True)

    return df