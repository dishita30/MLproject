## purpose : any execution that probably happens, we should be able to log all the information , execution in some files
## we will be able to track if there are errors
import logging
import os
from datetime import datetime

# creating log file

LOG_File = f"{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path = os.path.join(os.getcwd(), "logs",LOG_File) #current working directory (cwd) and Logs folder
os.makedirs(logs_path,exist_ok=True) #create the logs folder if it does not exist

LOG_FILE_PATH = os.path.join(logs_path,LOG_File) #create the log file path

logging.basicConfig(

    filename=LOG_FILE_PATH,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s", #ideal format for logging (timestamp, name of the logger, level of the logger, message)
    level = logging.INFO, #logging level
)

if __name__ == "__main__":
    logging.info("Logging started") #log the message