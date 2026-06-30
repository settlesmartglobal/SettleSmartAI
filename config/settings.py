"""
SettleSmart AI
Configuration Settings
"""

from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Folders
DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"
RESUME_DIR = BASE_DIR / "resumes"

# App Details
APP_NAME = "SettleSmart AI"
VERSION = "1.0.0"

# Default Country
DEFAULT_COUNTRY = "UAE"

# Default City
DEFAULT_CITY = "Dubai"