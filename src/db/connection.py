from sqlalchemy import create_engine
from config.settings import DB_URI

def get_engine():
    return create_engine(DB_URI)