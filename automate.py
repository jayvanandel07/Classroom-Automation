import time
import webbrowser
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
  now = datetime.now().time()
  return now
  
  
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
    
    time.sleep(5)
    pyautogui.leftClick(x=1311, y=413)
    
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
    pyautogui.leftClick(x=1412, y=616)
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
schedule.every().day.at("10:25:00").do(leaveMeet)

schedule.every().day.at("10:28:00").do(job,1)
schedule.every().day.at("11:20:00").do(leaveMeet)

schedule.every().day.at("13:28:00").do(job,2)
schedule.every().day.at("14:20:00").do(leaveMeet)

schedule.every().day.at("14:23:00").do(job,3)
schedule.every().day.at("15:15:00").do(leaveMeet)

  

while True:
    schedule.run_pending()
    time.sleep(1)


