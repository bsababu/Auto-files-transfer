''' 
You work at a company that receives daily data files from external partners. These files need to be processed and analyzed,
but first, they need to be transferred to the company's internal network.The goal of this project is to automate 
the process of transferring the files from an external FTP server to the company's internal network.

Here are the steps you can take to automate this process:
    Use the ftplib library to connect to the external FTP server and list the files in the directory.

    Use the os library to check for the existence of a local directory where the files will be stored.

    Use a for loop to iterate through the files on the FTP server and download them to the local directory using the ftplib.retrbinary() method.

    Use the shutil library to move the files from the local directory to the internal network.

    Use the schedule library to schedule the script to run daily at a specific time.

    You can also set up a log file to keep track of the files that have been transferred and any errors that 
    may have occurred during the transfer process. 
    '''

import os
from ftplib import FTP
import logging
import shutil
import schedule

url_path = '/assignment w4/downloaded'
    
def index():
    ftp = FTP()
    
    try:
        ftp.connect("ftp.server.de" )
        ftp.login('usename','passwd')
        #ftp.cwd('') #change the DR
        
        if not os.path.exists(url_path):
            os.makedirs(url_path)

        files = ftp.retrlines() #list all files
        for fl in files:
            file_local = os.path.join(url_path, os.path.basename(fl))
            with open(file_local, 'wb') as f:
                ftp.retrbinary('RETR ' + fl, f.write)
                logging.info(f"File '{fl}' downloaded ⚡️⚡️⚡️")

        for fl in os.listdir(url_path):
            shutil.move(os.path.join(url_path, fl), '/assignment w4/internal')
            logging.info(f"File '{fl}' transferred to internal n/w")

    except OSError as err:
        print(err)
    ftp.quit()

def main():
    schedule.every().day.at("00:01").do(index)
    while True:
        schedule.run_pending()
