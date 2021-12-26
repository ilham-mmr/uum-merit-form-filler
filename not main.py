from selenium import webdriver
import time
from dotenv import load_dotenv
import os
import csv

load_dotenv(override=True)
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
print(username)
print(password)

        
# web = webdriver.Chrome(executable_path='D:/Development/chromedriver_win32/chromedriver.exe')
# web.get('https://portal5.uum.edu.my/SAMS/AktivitiHEP/projek/proj_laporan.aspx')

# time.sleep(2)
# def login(username, password) :
#     username_field = web.find_element_by_xpath('//*[@id="title"]/span/input[1]')
#     username_field.send_keys(username)

#     password_field = web.find_element_by_xpath('//*[@id="title"]/span/input[2]')
#     password_field.send_keys(password)

#     submit = web.find_element_by_xpath('//*[@id="login"]')
#     submit.click()

# login(username,password)

# web.get('https://portal5.uum.edu.my/SAMS/AktivitiHEP/projek/list_projekstud.aspx')
# time.sleep(3)

# activity = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_gw1_ImageButton20_4"]')
# activity.click()
# time.sleep(2)

# # first open add button
# add_participant = web.find_element_by_id('ContentPlaceHolder1_btn_ajk0')
# add_participant.click()

# def save_participant(matric):
#     matric_field = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_txtstud2"]')
#     matric_field.send_keys(matric)
#     save_btn = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_Button6"]')
#     save_btn.click()
#     time.sleep(1)
    

# with open('attandance.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         matric = row[0]
#         if matric.isnumeric():
#             save_participant(matric)

# close_modal = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_btnCancel3"]')
# close_modal.click()

# save_form = web.find_element_by_xpath('//*[@id="ContentPlaceHolder1_Button1"]')
# save_form.click()
# web.close()