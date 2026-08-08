""" Logging module for the Expense Tracker application. """

import logging
from pathlib import Path

log_file_path = Path(__file__).resolve().parent.parent

LOG_FILE = log_file_path / "expense.log"


logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_info(message):
    """Log successful operations."""
    logging.info(message)


def log_error(message):
    """Log errors."""
    logging.error(message)


def log_warning(message):
    """Log warnings."""
    logging.warning(message)
