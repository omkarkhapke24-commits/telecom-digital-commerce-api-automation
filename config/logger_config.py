import logging
import os

# Create Logger object
logger = logging.getLogger() #hire manager

# Set minimum logging level
logger.setLevel(logging.INFO)  #instructs manager what to record

# Create logs directory if it doesn't exist
log_directory = "logs"  # cupboard to keep the register
os.makedirs(log_directory, exist_ok=True) #check if cupboard is already there. if not, make one.

# Build log file path
log_file_path = os.path.join(log_directory, "execution.log") #keeping the register into cupboard

# Create FileHandler
file_handler = logging.FileHandler(log_file_path) #assigning a writer to write into the register

# Create Formatter  
formatter = logging.Formatter( #training 'how to write (format) the logs'
    "%(asctime)s - %(levelname)s - %(message)s"  #format string
)

# Attach Formatter to FileHandler
file_handler.setFormatter(formatter) #asking writer to obey to trained format

# Attach FileHandler to Logger (only once)
if not logger.handlers:
    logger.addHandler(file_handler) #linking up manager and writer if they aint linked earlier
