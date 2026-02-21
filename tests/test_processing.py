# tests: data processing

import pandas as pd
from src.processing.clean_data import clean_data

def test_clean_removes_null_ids():
    df = pd.DataFrame({
        "id": [1, None],
        "amount": [10, 20]
    })

    cleaned = clean_data(df)

    assert cleaned["id"].isnull().sum() == 0