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