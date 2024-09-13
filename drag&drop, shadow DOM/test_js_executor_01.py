import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_JS_01():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
    button = driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
    # button.click()

    # Javascript executor
    # Use the Javascript code to click on this button also
    js_ex = driver.execute_script("arguments[0].click()",button)
    js_ex = driver.execute_script("arguments[0].click()",button)


    time.sleep(5)
    driver.quit()


