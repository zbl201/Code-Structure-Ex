from src.data_loading.load_sql import fetch_dataframe
from src.data_loading.load_csv import load_india_commodity_prices
from src.data_processing.clean_data import clean_data
from src.data_analysis.analyze import analyze
from src.utils.logger import get_logger
from src.utils.utils import clear_pycache, testprint

logger = get_logger()


def pipeline_01_test():
    """
    Self learning pipeline
    """
    logger.info("Loading data...")
    df = fetch_dataframe("sql/nba_analysis/bulls_query.sql")

    logger.info("Cleaning data...")
    df_clean = clean_data(df)

    logger.info("Running analysis...")
    summary = analyze(df_clean)

    logger.info("Test printing...")
    testprint(df_clean, filename='bulls_roster', filetype='.txt')


def pipeline_02_india_commodity_prices():
    """
    Analysis of Indial Commodity Prices Kaggle dataset.
    https://www.kaggle.com/datasets/khandelwalmanas/daily-commodity-prices-india/data
    """
    logger.info("Loading all files...")
    df = load_india_commodity_prices()
    
    logger.info(f'{len(df)} rows.')
    testprint(df.head(20), filename='india_commodities_head', filetype='.txt')


if __name__ == "__main__":
    pipeline_02_india_commodity_prices()
    clear_pycache(root_dir=".", dry_run=False)