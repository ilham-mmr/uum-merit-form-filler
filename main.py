from dotenv import load_dotenv
import os
from functions import run_flow

if __name__ == '__main__':
    load_dotenv(override=True)
    username = os.getenv('USERNAME')
    password = os.getenv('PASSWORD')
    run_flow(username,password,'attendance.csv','ContentPlaceHolder1_gw1_ImageButton20_4')
