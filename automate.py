import time
import webbrowser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

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
  

def openMeet(url):
    # Open meet
    time.sleep(5)
    webbrowser.open_new(url)
    pyautogui.press("enter")
    time.sleep(5)
    
    
    print("opening meet")
    
def turnOffMicCam():
    # turn off Microphone
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'd')
    # turn off camera
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'e')
    
    print('Turing off mic and camera')
    
def joinNow():
    
    # Join meet
    time.sleep(1)
    pyautogui.leftClick(1410, 700)
    time.sleep(1)
    
    print("join meet")
    
def leaveMeet():
    # Leave meet
    time.sleep(2)
    pyautogui.leftClick(x=1187, y=950)    
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
opt.add_argument("--user-data-dir=C:/Users/Jayvan andel/AppData/Local/Google/Chrome/User Data/")
opt.add_argument('--profile-directory=Profile 1')
opt.add_experimental_option('excludeSwitches', ['enable-logging'])

try:   
    s = Service(r"C:/Users/Jayvan andel/AppData/Roaming/chromedriver_win32/chromedriver.exe")
    driver = webdriver.Chrome(options=opt, service=s)
except(Exception) as e:
    print("Close other chrome windows and try again")
    

    


while True:
    schedule.run_pending()
    time.sleep(1)


