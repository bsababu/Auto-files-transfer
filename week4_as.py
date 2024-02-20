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
