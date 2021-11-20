
import time
import webbrowser
import pyautogui
from datetime import date,datetime
import calendar
import schedule
from setup.meetLink import LINKS,TIME_TABLE
from setup.coordinates import COORDINATES

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
    
def joinNow(X=1412, Y=616):
    # Join meet
    time.sleep(1)
    pyautogui.leftClick(x=X, y=Y)
    time.sleep(1)
    
    print("join meet")
    
def leaveMeet(X=1187, Y=950):
    # Leave meet
    time.sleep(2)
    pyautogui.leftClick(x=X, y=Y)    
    time.sleep(1)

    print("leaving meet")
    

  
def job(p):
    # Run
    openMeet(findClass(p))
    turnOffMicCam()
    joinNow(COORDINATES[0][0],COORDINATES[0][1])
    
def leave():
    leaveMeet(COORDINATES[1][0],COORDINATES[1][1])
    

def taskComplete():
    print("Task Complete!")
    time.sleep(10)
    quit()
    
print("Classroom Bot Online!")


schedule.every().day.at("09:33:00").do(job,0) # 9:33:00 joining time
schedule.every().day.at("10:26:00").do(leave) # 10:26:00 leaving time

schedule.every().day.at("10:28:00").do(job,1)
schedule.every().day.at("11:21:00").do(leave)

schedule.every().day.at("13:28:00").do(job,2)
schedule.every().day.at("14:21:00").do(leave)

schedule.every().day.at("14:23:00").do(job,3)
schedule.every().day.at("15:16:00").do(leave)
schedule.every().day.at("15:25:00").do(taskComplete)


while True:
    schedule.run_pending()
    time.sleep(1)


