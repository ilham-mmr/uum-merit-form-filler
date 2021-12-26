from selenium import webdriver
import time
from dotenv import load_dotenv
import os
import csv

load_dotenv(override=True)
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get('https://portal5.uum.edu.my/SAMS/AktivitiHEP/projek/proj_laporan.aspx')
time.sleep(1)
    
def login() :
    username_field = driver.find_element(By.XPATH,'//*[@id="title"]/span/input[1]')
    username_field.send_keys(username)

    password_field = driver.find_element(By.XPATH,'//*[@id="title"]/span/input[2]')
    password_field.send_keys(password)

    submit = driver.find_element(By.XPATH,'//*[@id="login"]')
    submit.click()

login()

# driver.get('https://portal5.uum.edu.my/SAMS/AktivitiHEP/projek/list_projekstud.aspx')
# time.sleep(1)

activity = driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_gw1_ImageButton20_4"]')
activity.click()
time.sleep(1)

# first open add button
add_participant = driver.find_element(By.ID,'ContentPlaceHolder1_btn_ajk0')
add_participant.click()

def save_participant(matric):
    matric_field = driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_txtstud2"]')
    matric_field.send_keys(matric)
    save_btn = driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_Button6"]')
    save_btn.click()
    time.sleep(0.2)
    

with open('attandance.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        matric = row[0]
        if matric.isnumeric():
            save_participant(matric)

close_modal = driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_btnCancel3"]')
close_modal.click()

save_form = driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_Button1"]')
save_form.click()
driver.close()



# username
# password
# which club activiy
# csv file
