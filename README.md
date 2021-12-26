## About UUM Merit Form Filler

## HOW TO USE
- have python installed
- open terminal
- then run this in your terminal ```pip install -r requirements.txt```
- add your attendance.csv which can be converted from excel file with the following format ```MATRIC NO,NAME```
- create .env file and add your credentials ``` USERNAME='your_uum_username' PASSWORD='your_uum_password' ```
- next, you only need to configure the main.py file. choose which project report activity you want to choose. replace the ContentPlaceHolder1_gw1_ImageButton20_4 with your own report_activity_btn_id. in order to find the id of element, you have to inspect element your page 
```
    run_flow(username,password,'attendance.csv','ContentPlaceHolder1_gw1_ImageButton20_4')

```
- finally, run your code with ```python main.py```