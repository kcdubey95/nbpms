import logging
import os
from logging.handlers import TimedRotatingFileHandler
from datetime import datetime

# Ensure the logs directory exists
if not os.path.exists("logs"):
    os.makedirs("logs")

# Get today's date for the initial filename
current_date = datetime.now().strftime("%Y-%m-%d")
log_filename = f"logs/daily_log.{current_date}.log"

# Define the logger
logger = logging.getLogger("DailyLogger")
logger.setLevel(logging.DEBUG)

# Define log format
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# Create a TimedRotatingFileHandler
log_handler = TimedRotatingFileHandler(
    log_filename,      # Initial log file name
    when="midnight",   # Rotate at midnight
    interval=1,        # Rotate every day
    backupCount=7      # Keep the last 7 log files
)

# Add a timestamp to the rotated filenames
log_handler.suffix = "%Y-%m-%d.log"

# Set the formatter
log_handler.setFormatter(formatter)

# Add handler to the logger
logger.addHandler(log_handler)



# Flush logs to ensure all are written immediately
for handler in logger.handlers:
    handler.flush()
