from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import keyboard

# Initialize the Chrome driver
driver = webdriver.Chrome()
driver.get("https://onlineorientation.uga.edu/")

# Add the authentication cookie
auth_cookie = {
    'name': 'yourAuthCookie',
    'value':'ENTER COOKIE HERE',
    'domain': 'onlineorientation.uga.edu',

}

driver.add_cookie(auth_cookie)
driver.refresh()

commandOne = """
try {
    document.getElementById('arrowRight').classList.remove('disabled');
} catch (e) {}
"""


while True:
    if keyboard.is_pressed('s'):
        driver.execute_script(commandOne)
        
    if keyboard.is_pressed('ctrl+shift+f'):
        break
    
    sleep(0.01)

driver.quit()
