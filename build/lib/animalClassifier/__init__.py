import logging.handlers
import os
import sys
import logging

#This file will create loggings for all processes
logging_str="[%(ascitime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir="logs"
#Creating the path for saving the log file
log_filepath=os.path.join(log_dir,"running_logs.log")

logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        #printing log in the file
        logging.FileHandler(logging_str),
        #printing log in the terminal
        logging.StreamHandler(sys.stdout)
    ]
)


logger=logging.getLogger("AnimalClassificationLogger")