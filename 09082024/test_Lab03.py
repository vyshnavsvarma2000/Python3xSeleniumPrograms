import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():

    # Options Class - What is the class?
    # customize the behavior of the browser during automated testing.
    # Chrome -> headless or UI -> headless mode - no ui
    # disable gpu, add extension, maximize, set windows, 100 other options that you can do
    # before starting the Browser

    #Create an instance of chrome Options
    chrome_options = Options()
    # chrome_options.add_argument("--headless")
    # chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://app.vwo.com")
    time.sleep(10)

