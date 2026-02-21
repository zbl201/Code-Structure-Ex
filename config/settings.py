# database + global config
from dotenv import load_dotenv
import os

load_dotenv()

DB_URI = os.getenv("DB_URI")

DATA_RAW_PATH = "data/raw/"
DATA_PROCESSED_PATH = "data/processed/"
OUTPUT_PATH = "data/outputs/"