from selenium import webdriver
from google.oauth2.service_account import Credentials
import gspread
from humanfriendly import parse_size
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

with open (r'C:\\Users\\Lenovo\\Desktop\\code\\tiktoka-data-mcn\\modular-tube-412013-666981a759e4.json') as f:
    credentials = json.load(f)
def dataTikTok(urls):
    likes=[]
    comments=[]
    saves=[]
    shares=[]

    gc = gspread.service_account_from_dict(credentials)
    sht2 = gc.open_by_url('https://docs.google.com/spreadsheets/d/1zZFqgrN6A4JNIlftQgpbyMHBZFWsU7LpL_BBrwQxu6E/edit?usp=sharing')
    worksheet = sht2.get_worksheet(0)

    for url in urls:
        path=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        driver = webdriver.ChromeOptions()
        driver.binary_location=path
        driver.add_argument("--headless")
        driver2=webdriver.Chrome(options=driver)
        driver2.get(url)
        elements = driver2.find_elements(By.TAG_NAME,'strong')
        # print("elements[0].text",elements[0].text)
        # print("elements[1].text",elements[1].text)
        # print("elements[2].text",elements[2].text)
        # print("elements[3].text",elements[3].text)
        # print("elements[4].text",elements[4].text)
        if str(parse_size(elements[1].text)).isdigit():
            likes.append(int(parse_size(elements[1].text)))
        else: 
            likes.append(0)
        
        if str(parse_size(elements[2].text)).isdigit():
            comments.append(int(parse_size(elements[2].text)))
        else: 
            comments.append(0)

        if str(parse_size(elements[3].text)).isdigit():
            saves.append(int(parse_size(elements[3].text)))
        else: 
            saves.append(0)

        if elements[4].text == "Share":
            shares.append(0)
        elif str(parse_size(elements[4].text)).isdigit():
            shares.append(int(parse_size(elements[4].text)))
        else: 
            shares.append(0)

    for index,like in enumerate(likes, start=6):
        worksheet.update(f'C{index}', [[int(f'{like}')]]) #ตัว C คือ คอลัม / start = เริ่มต้นลงข้อมูลที่ Ex. แถว 6 ... เอาไว้แก้นะจ๊ะ     
    for index,comment in enumerate(comments, start=6):
        worksheet.update(f'D{index}', [[(f'{comment}')]])
    for index,save in enumerate(saves, start=6):
        worksheet.update(f'E{index}', [[int(f'{save}')]])
    for index,share in enumerate(shares, start=6):
        worksheet.update(f'F{index}', [[int(f'{share}')]])
        

    # worksheet.update('A1:B2', [[1, 2], [3, 4]])
    # worksheet.update('D1',[["E"]])
