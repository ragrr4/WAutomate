import keyboard
from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By

class WActions:

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.driver.get(WHATSAPP_URL) 
        self.wait = WebDriverWait(self.driver, 600) 

    def write_chat(self, msg):
        # Enter char is included
        input_box = self.wait.until(
            EC.presence_of_element_located((By.XPATH, XPATH_CHAT_INPUT))
        )
        input_box.click()
        keyboard.write(msg + "\n")
    
    def new_chat(self):
        new_chat = self.wait.until(
            EC.presence_of_element_located((By.XPATH, XPATH_NEW_CHAT))
        )
        new_chat.click()

    def search(self, keyword):
        # keyword should be at least 3 char long
        keyboard.write(keyboard)

    def search_select(self, keyword):
        # keyword should be at least 3 char long
        keyboard.write(keyboard + "\n")

    def select_elem(self, elem_no = 1):
        element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, XPATH_ELEMENT.format(elem_no)))
        )
        element.click()

    def open_chat(self):
        chat_title = self.wait.until(
            EC.presence_of_element_located(
                (By.XPATH, XPATH_EXISTING_CHAT.format(target))
            )
        )
        chat_title.click()

