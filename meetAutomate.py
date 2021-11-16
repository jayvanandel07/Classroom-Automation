from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import webbrowser
import time

pyautogui.PAUSE = 0.5  
  
def Glogin(mail_address, password):
    # Login Page
    driver.get(
        'https://accounts.google.com/ServiceLogin?hl=en&passive=true&continue=https://www.google.com/&ec=GAZAAQ')
  
    # input Gmail
    driver.find_element_by_id("identifierId").send_keys(mail_address)
    driver.find_element_by_id("identifierNext").click()
    driver.implicitly_wait(10)
  
    # input Password
    driver.find_element_by_xpath(
        '//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
    driver.implicitly_wait(10)
    driver.find_element_by_id("passwordNext").click()
    driver.implicitly_wait(10)
  
    # go to google home page
    driver.get('https://google.com/')
    driver.implicitly_wait(100)
  
  
def turnOffMicCam():
    # turn off Microphone
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'd')
    # turn off camera
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'e')
    
    
  
  
def joinNow():
    # Join meet
    print(1)
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element(
        '//div[@class="XCoPyb"]/div[@class="uArJ5e UQuaGc Y5sE8d uyXBBb xKiqt"]/span[@class="l4V7wb Fxmcue"]').click()
    print(1)
  
  
def AskToJoin():
    # Ask to Join meet
    time.sleep(5)
    driver.implicitly_wait(2000)
    driver.find_element_by_css_selector(
        'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    # Ask to join and join now buttons have same xpaths
  
  


# create chrome instamce
opt = Options()
opt.add_argument('--disable-blink-features=AutomationControlled')
opt.add_argument('--start-maximized')
opt.add_argument("--user-data-dir=C:/Users/Jayvan andel/AppData/Local/Google/Chrome/User Data/")
opt.add_argument('--profile-directory=Profile 1')

opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 0,
    "profile.default_content_setting_values.notifications": 1
})
driver = webdriver.Chrome(options=opt, executable_path=r"C:/Users/Jayvan andel/AppData/Roaming/chromedriver_win32/chromedriver.exe")

  
# go to google meet
driver.get('https://meet.google.com/')

# meetLogin()

turnOffMicCam()
# AskToJoin()
joinNow()