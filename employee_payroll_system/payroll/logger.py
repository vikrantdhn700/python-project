"""Payroll and error logging functions."""

import logging
from pathlib import Path

log_file_path = Path(__file__).resolve().parent.parent

PAYROLL_LOGGER_NAME = "payroll_operations"
ERROR_LOGGER_NAME = "payroll_errors"

PAYROLL_LOGGER = log_file_path / "payroll.log"
ERROR_LOGGER = log_file_path / "error.log"


def create_logger(
    name,
    filename,
    level
):
    """Create and configure a logger."""

    logger = logging.getLogger(name)

    logger.setLevel(level)

    logger.propagate = False

    if not logger.handlers:

        handler = logging.FileHandler(
            filename,
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s - "
            "%(levelname)s - "
            "%(message)s"
        )

        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger


def log_payroll(message):
    """Log successful payroll operations."""

    logger = create_logger(
        PAYROLL_LOGGER_NAME,
        PAYROLL_LOGGER,
        logging.INFO
    )

    logger.info(message)


def log_error(message):
    """Log errors."""

    logger = create_logger(
        ERROR_LOGGER_NAME,
        ERROR_LOGGER,
        logging.ERROR
    )

    logger.error(message)
