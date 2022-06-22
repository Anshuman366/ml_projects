import logging
import os
from datetime import date, datetime



#creating logging directory
log_dir="Housing_log"


current_time_stamp= f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

#making log file with the name of time and date of creation log
log_file=f"log_{current_time_stamp}.log"

#making directory , if already exist then do nothing otherwise create the directory
os.makedirs(log_dir,exist_ok=True)

#joining the file path with directory by using os module
file_path= os.path.join(log_dir,log_file)


logging.basicConfig(filename=file_path,
filemode="w",
format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
level=logging.INFO
   
    )
