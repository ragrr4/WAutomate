
import os
import keyboard
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 

# Replace below path with the absolute path 
# to chromedriver in your computer 
SCRIPT_PATH = os.path.dirname(os.path.realpath(__file__))
driver_path = os.path.join(SCRIPT_PATH, "chromedriver.exe")
driver = webdriver.Chrome(driver_path)
driver.get("https://web.whatsapp.com/") 
wait = WebDriverWait(driver, 600) 

# Replace 'Friend's Name' with the name of your friend 
# or the name of a group 
target = "Christian Roomie"

# Replace the below string with your own message 
string = "Message sent using Python!!!"

x_arg = "//span[contains(@title,'" + target + "')]"
chat_title = wait.until(
    EC.presence_of_element_located((By.XPATH, x_arg))
)
print("item:", str(chat_title))
chat_title.click()
inp_xpath = "//div[@contenteditable='true'][@data-tab='1'][@spellcheck='true']"
input_box = wait.until(
    EC.presence_of_element_located((By.XPATH, inp_xpath))
)
for i in range(100):
    input_box.click()
    keyboard.write(string + "\n")
    time.sleep(1) 
