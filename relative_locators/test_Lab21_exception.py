import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.common.exceptions import *


def test_expcetion():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        search_input = driver.find_element(By.XPATH, "//textarea[@id='APjFqbw']")
        search_input.send_keys("thetestingacademy")
    except NoSuchElementException as nse:
        print(f"No such element found {nse}")
    time.sleep(5)

    driver.quit()