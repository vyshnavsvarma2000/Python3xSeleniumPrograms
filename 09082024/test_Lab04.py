import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_open_vwologin():

    chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    chrome_options.add_extension("E:\The TESTING ACADEMY\WEB_AUTOMATION\Python3xSeleniumPrograms\AdBlock-—-block-ads-across-the-web-Chrome-Web-Store.crx")
    # You have to start the Chrome with an extension
    # You have to start the Chrome with this extension
    driver = webdriver.Chrome(chrome_options)
    driver.get("https://youtube.com")
    driver.maximize_window()
    time.sleep(10)