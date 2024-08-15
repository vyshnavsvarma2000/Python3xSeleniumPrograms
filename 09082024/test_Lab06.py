import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com")
    driver.refresh()
    driver.back()
    driver.forward()
    print(driver.page_source)
    time.sleep(10)
    driver.quit()
    #close() -> close will close the current window, Session id will not be null
    #quit() -> it closes every window, and deletes the session , sothat session id is null

