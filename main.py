from src.ingestion.load_data import fetch_dataframe
from src.processing.clean_data import clean_data
from src.analysis.analyze import summarize_amount
from src.utils.logger import get_logger
from src.utils.utils import clear_pycache

logger = get_logger()

def main():

    logger.info("Loading data...")
    df = fetch_dataframe("sql/test_query.sql")

    logger.info("Cleaning data...")
    df_clean = clean_data(df)

    logger.info("Running analysis...")
    summary = summarize_amount(df_clean)

    logger.info(summary)

if __name__ == "__main__":
    main()
    clear_pycache(root_dir=".", dry_run=False)