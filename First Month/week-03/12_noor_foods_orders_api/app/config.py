import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
DEFAULT_DATABASE_URL = "sqlite:///./noor_foods.db"

DATABASE_URL = os.getenv("DATABASE_URL", DEFAULT_DATABASE_URL)
APP_TITLE = os.getenv("APP_TITLE", "Noor Foods Orders API")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", "8000"))
