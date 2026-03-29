import pandas as pd
from src.db.connection import get_engine
from src.utils.utils import testprint

def load_sql_file(path):
    with open(path, "r") as f:
        return f.read()

def fetch_dataframe(sql_file):
    engine = get_engine()
    query = load_sql_file(sql_file)
    df = pd.read_sql(query, engine)
    return df