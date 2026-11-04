"""Runtime configuration loaded from environment variables."""
import os

DB_PATH = os.getenv("CAREEROS_DB", "careeros.db")
LLM_BASE_URL = os.getenv("LLM_BASE_URL", "").rstrip("/")
LLM_API_KEY = os.getenv("LLM_API_KEY", "")
LLM_MODEL = os.getenv("LLM_MODEL", "")
APP_NAME = "CareerOS"
VERSION = "1.0.0"
