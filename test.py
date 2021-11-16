from datetime import datetime
import schedule
import time
def current_time():
  now = datetime.now().time().strftime("%H:%M:%S") # time object

  print("now =", now)
  print("type(now) =", type(now))
  
  return now

def job():
    print("I'm working...")

if ("15:10:00"<current_time()<"15:30:00"):
  schedule.every().day.at(current_time()).do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

  
  