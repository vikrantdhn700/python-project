""" Logger module for the library management system. """

import logging
from pathlib import Path

log_file_path = Path(__file__).resolve().parent.parent

log_file = log_file_path / "library.log"

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=log_file,
    filemode='w'
)


def log_message(message: any, level: str = "debug") -> None:
    """Log a message at the specified logging level."""
    if level == "debug":
        logging.debug(message)
    elif level == "info":
        logging.info(message)
    elif level == "warning":
        logging.warning(message)
    elif level == "error":
        logging.error(message)
    elif level == "critical":
        logging.critical(message)
