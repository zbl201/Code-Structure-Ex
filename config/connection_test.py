from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.getenv("DB_URI"))

with engine.connect() as conn:
    print("Connected!")