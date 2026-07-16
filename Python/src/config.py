"""
RetailIQ Configuration

Loads environment variables
used across the RetailIQ project.
"""

from pathlib import Path

from dotenv import load_dotenv
import os

# Project root directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Load environment variables from .env
load_dotenv(PROJECT_ROOT / ".env")

# Database Configuration
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


# ==========================================
# Date Dimension Configuration
# ==========================================

DATE_START = "2022-01-01"
DATE_END = "2026-12-31"



# ==========================================
# Orders Configuration
# ==========================================

NUM_ORDERS = 10000

ORDER_STATUSES = [
    "Completed",
    "Pending",
    "Cancelled",
    "Returned"
]

PAYMENT_METHODS = [
    "Cash",
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking"
]


SALES_CHANNELS = [
    "Store",
    "Online",
    "Mobile App"
]