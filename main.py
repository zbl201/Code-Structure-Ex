from src.data_loading.load_data import fetch_dataframe
from src.data_processing.clean_data import clean_data
from src.data_analysis.analyze import summarize_amount
from src.utils.logger import get_logger
from src.utils.utils import clear_pycache, testprint

logger = get_logger()


def pipeline_01_self_learning():
    """
    Self learning pipeline
    """
    logger.info("Loading data...")
    df = fetch_dataframe("sql/test_query.sql")

    logger.info("Cleaning data...")
    df_clean = clean_data(df)

    logger.info("Running analysis...")
    summary = summarize_amount(df_clean)

    logger.info(summary)
    testprint(df_clean, filetype='.txt')


def pipeline_02_tbd():
    """
    Pipeline desc.
    """
    pass


if __name__ == "__main__":
    pipeline_01_self_learning()
    clear_pycache(root_dir=".", dry_run=False)