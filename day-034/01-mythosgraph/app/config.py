from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
DB_PATH=ROOT/"data"/"mythosgraph.db"
MEMORY_LIMIT=12
MIN_RELEVANCE=0.08