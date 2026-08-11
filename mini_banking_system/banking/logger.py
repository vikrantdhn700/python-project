"""Separate success and error logging functions."""

import logging
from pathlib import Path


PROJECT_FOLDER = Path(__file__).resolve().parent.parent
BANKING_LOG = PROJECT_FOLDER / "banking.log"
ERROR_LOG = PROJECT_FOLDER / "error.log"


def create_logger(name, file_path, level):
    """Create and return a file logger without duplicate handlers."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False
    if not logger.handlers:
        handler = logging.FileHandler(file_path, encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(asctime)s | %(levelname)s | %(message)s"))
        logger.addHandler(handler)
    return logger


def log_transaction(message):
    """Write a successful banking operation to banking.log."""
    create_logger("banking_success", BANKING_LOG, logging.INFO).info(message)


def log_error(message):
    """Write a failed operation or application error to error.log."""
    create_logger("banking_error", ERROR_LOG, logging.ERROR).error(message)


def initialize_logs():
    """Ensure both log files exist, even before the first operation."""
    BANKING_LOG.touch(exist_ok=True)
    ERROR_LOG.touch(exist_ok=True)
