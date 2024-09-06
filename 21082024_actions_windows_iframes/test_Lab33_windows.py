# Actions and Windows, and Iframe.
import time

from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import os


def test_022_windows():
    load_dotenv()
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/windows")
    driver.maximize_window()
    parent_window = driver.current_window_handle #Gives the parent window #1
    link = driver.find_element(By.LINK_TEXT, "Click Here")
    link.click()
    window_handles = driver.window_handles #2 total windows are there

    for handle in window_handles:
        driver.switch_to.window(handle) #Go to the child window
        if "New Window" in driver.page_source:
            print("Test case passed")
            break

    time.sleep(5)
    driver.quit()