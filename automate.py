import time
import webbrowser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By 

import pyautogui
from datetime import date,datetime
import calendar
import schedule
from meetLink import LINKS,TIME_TABLE


pyautogui.PAUSE = 0.5



def today():
  my_date = date.today()
  return calendar.day_name[my_date.weekday()].upper()

def current_time():
    # Get current time 
  Now = datetime.now().time().strftime("%H:%M:%S")
  
  return Now
  
  
def findClass(period):
    # Find class and return the url
    print(today())
    print(current_time())
    print(period+1,":",TIME_TABLE[today()][period])
    return LINKS[TIME_TABLE[today()][period]]
  
def Glogin(mail_address, password):
    # Login Page
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
  
    # input Gmail
    driver.find_element(By.ID,"identifierId").send_keys(mail_address)
    driver.find_element(By.ID,"identifierNext").click()
    driver.implicitly_wait(10)
  
    # input Password
    driver.find_element(By.XPATH,
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element(By.ID,"passwordNext").click()
    driver.implicitly_wait(10)
  



def openMeet(url):
    # Open meet
    time.sleep(5)
    driver.get(url) #selenium
    # webbrowser.open_new(url)   #webbrowser.open
    pyautogui.press("enter")
    time.sleep(5)
    
    
    print("opening meet")


                      

def turnOffMicCam():
    # turn off Microphone
    time.sleep(2)
    driver.find_element(By.XPATH,
        "//div[@class='ZB88ed']"
    ).click()
    
    # turn off camera
    time.sleep(2)
    driver.find_element(By.XPATH,
        "//div[@class='GOH7Zb']"
    ).click()
    
    print('Turing off mic and camera')
    
def joinNow():
    
    # Join meet
    time.sleep(1)
    driver.find_element(By.XPATH,
        "//div[@class='uArJ5e UQuaGc Y5sE8d uyXBBb xKiqt']").click() #selenium
    # pyautogui.leftClick(1410, 700) #autogui
    time.sleep(1)
    
    print("join meet")
    
def leaveMeet():
    # Leave meet
    time.sleep(2)
    driver.find_element(By.XPATH,  #selenium
        "//button[@class='VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ tWDL4c jh0Tpd Gt6sbf QQrMi ftJPW']").click()
    
    # pyautogui.leftClick(x=1187, y=950)    #autogui
    time.sleep(1)

    print("leaving meet")
    

  
def job(p):
    # Run
    openMeet(findClass(p))
    turnOffMicCam()
    joinNow()
    
print("Classroom Bot Online!")

schedule.every().day.at("09:33:00").do(job,0)
schedule.every().day.at("10:26:30").do(leaveMeet)

schedule.every().day.at("10:28:00").do(job,1)
schedule.every().day.at("11:21:30").do(leaveMeet)

schedule.every().day.at("13:28:00").do(job,2)
schedule.every().day.at("14:21:30").do(leaveMeet)

schedule.every().day.at("14:23:00").do(job,3)
schedule.every().day.at("15:16:30").do(leaveMeet)



# create chrome instamce
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_argument('--disable-web-security')
opt.add_argument('--allow-running-insecure-content')
opt.add_argument('--user-data-dir')
#This code causes complications when a chrome window is already open:
# opt.add_argument("--user-data-dir=C:/Users/Jayvan andel/AppData/Local/Google/Chrome/User Data/")
# opt.add_argument('--profile-directory=Profile 1')

opt.add_experimental_option('excludeSwitches', ['enable-logging'])
# Pass the argument 1 to allow and 2 to block (allow access to mic, camera, location, notifications)
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
  })

# try:   
s = Service(r"C:/Users/Jayvan andel/AppData/Roaming/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(options=opt, service=s)
# except(Exception) as e:
#     print("Close other chrome windows and try again")

mail_address="Your mail ID"
password="PASSWORD HERE"

try:
    Glogin(mail_address, password)
except (Exception) as e:
    print(e)
    print("Gmail login failed: Run setup file First!")





while True:
    schedule.run_pending()
    time.sleep(1)


