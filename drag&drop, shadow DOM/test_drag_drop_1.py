import selenium
import time
from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium.webdriver.common.by import By

def test_01_dragdrop():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/drag_and_drop")

    actions = ActionChains(driver)
    from_element = driver.find_element(By.ID, "column-a")
    to_element =  driver.find_element(By.ID, "column-b")
    # actions.click_and_hold(from_element).move_to_element(to_element).release().perform() #Best Approach and works in most of the browsers
    actions.drag_and_drop(from_element, to_element).perform()
    time.sleep(5)
    driver.quit()