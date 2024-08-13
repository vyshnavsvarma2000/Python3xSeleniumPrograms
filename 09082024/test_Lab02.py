import time

from selenium import webdriver

def test_open_vwologin():
    driver = webdriver.Chrome()
    # Code -> HTTP Request - POST
    # POST request | Create the Session
    # Session is created - Unique ID - 16 digit ID
    # 62c075633fd0b0727c5c3f6eae5665ab

    #driver = webdriver.Edge()
    #driver = webdriver.Firefox()

    # Code -> HTTP Request -. ChromeDriver-> Chrome (SessionID)
    print(driver.session_id) # 1d5d37c4eb934aef8053d28fc69862d6
    driver.get("https://app.vwo.com")
    print(driver.title)
    assert driver.title == "Login - VWO"
    #time.sleep(10) # Python Int - to stop for the 10 seconds