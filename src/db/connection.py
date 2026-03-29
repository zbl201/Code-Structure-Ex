from sqlalchemy import create_engine
from config.settings import DB_URI

def get_engine():
    if not DB_URI:
        raise ValueError("DB_URI environment variable is not set")
    return create_engine(DB_URI)