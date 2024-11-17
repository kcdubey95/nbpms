import logging
from logging.handlers import TimedRotatingFileHandler

# Define the logger
logger = logging.getLogger("DailyLogger")
logger.setLevel(logging.DEBUG)

# Create a TimedRotatingFileHandler
log_handler = TimedRotatingFileHandler(
    "logs/daily_log",  # Base filename (no extension)
    when="midnight",   # Rotate at midnight
    interval=1,        # Rotate every day
    backupCount=7      # Keep the last 7 log files
)

# Add a timestamp to the filename
log_handler.suffix = "%Y-%m-%d.log"

# Define log format
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
log_handler.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(log_handler)