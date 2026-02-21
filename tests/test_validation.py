# tests: data validation

from src.ingestion.load_data import fetch_dataframe

def test_amount_positive():

    df = fetch_dataframe("sql/test_query.sql")

    assert (df["SEASON"] >= 0).all()