from selenium import webdriver
import time
import csv

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.maximize_window()
    
def login(username, password) :
    username_field = driver.find_element(By.XPATH,'//*[@id="title"]/span/input[1]')
    username_field.send_keys(username)

    password_field = driver.find_element(By.XPATH,'//*[@id="title"]/span/input[2]')
    password_field.send_keys(password)

    submit = driver.find_element(By.XPATH,'//*[@id="login"]')
    submit.click()
    
def save_participant(matric):
    matric_field = driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_txtstud2"]')
    matric_field.send_keys(matric)
    save_btn = driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_Button6"]')
    save_btn.click()
    time.sleep(0.2)
    
def run_attandance(attendance):
    with open(attendance, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            matric = row[0]
            if matric.isnumeric():
                save_participant(matric)    

def choose_club_report_activity(report_activity_btn_id):
    activity = driver.find_element(By.ID,report_activity_btn_id)
    activity.click()
    time.sleep(1)                

def run_flow(username, password,attendance, page ,report_activity_btn_id):
    try:
        driver.get('https://portal5.uum.edu.my/SAMS/AktivitiHEP/projek/list_projekstud.aspx')
        time.sleep(1) 
        login(username, password)
        
        # choose page 
        pages = driver.find_elements(By.XPATH,'//*[@id="ContentPlaceHolder1_gw1"]/tbody/tr[12]/td/table/tbody/tr/child::*')
        time.sleep(0.05)
        selected_page = pages[page - 1]
        selected_page.click()
        
        choose_club_report_activity(report_activity_btn_id)
        
        # click add button
        add_participant = driver.find_element(By.ID,'ContentPlaceHolder1_btn_ajk0')
        add_participant.click()
        
        run_attandance(attendance)
        
        # close matric modal
        close_modal = driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_btnCancel3"]')
        close_modal.click()
        
        # save the report form
        save_form = driver.find_element(By.XPATH,'//*[@id="ContentPlaceHolder1_Button1"]')
        save_form.click()
        driver.switch_to.alert.accept()
        driver.close()
    except Exception as e:
        print(e)

