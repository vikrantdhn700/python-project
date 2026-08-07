import logging
from pathlib import Path

log_file_path = Path(__file__).resolve().parent.parent

log_file = log_file_path / "student.log"

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename= log_file,
    filemode='w'
  )

def log_message(message, type="debug"):
  if type=="debug":
    logging.debug(message)
  elif type=="info":
    logging.info(message)
  elif type=="warning":
      logging.warning(message)
  elif type=="error":
      logging.error(message)
  elif type=="critical":
      logging.critical(message)