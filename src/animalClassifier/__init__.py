import logging.handlers
import os
import sys
import logging

#This file will create loggings for all processes
logging_str="[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir="logs"
#Creating the path for saving the log file
log_filepath=os.path.join(log_dir,"running_logs.log")
#create logs file for running_logs file
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        #printing log in the file
        logging.FileHandler(log_filepath),
        #printing log in the terminal
        logging.StreamHandler(sys.stdout)
    ]
)


logger=logging.getLogger("AnimalClassificationLogger")