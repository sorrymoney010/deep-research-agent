from pathlib import Path

PROJECT_ROOT = Path(__file__).parent
DB_PATH = PROJECT_ROOT / "research.db"
REPORT_DIR = PROJECT_ROOT / "reports"

CONFIDENCE_WEIGHTS = {
    "primary": 0.70,
    "secondary": 0.50,
    "interpretation": 0.25,
    "speculation": 0.05,
}
