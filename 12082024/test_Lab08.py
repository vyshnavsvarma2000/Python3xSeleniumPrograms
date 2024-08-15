import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import allure

@pytest.mark.positive
@allure.title("VWO Invalid Login Page - test_mini_project_2")
@allure.description(
    "Verify that with Invalid Email, Password. Error message came")
def test_mini_project_2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    assert driver.current_url == "https://app.vwo.com/#/login"

    # id -> name -> classname -> link/partial -> tagname -> css selector -> xpath.
    # Find the email, password and enter the invalid details.
    # <input
    # type="email"
    # class="text-input W(100%)"
    # name="username"
    #id="login-username"
    # data-qa="hocewoqisi"
    # >
    email_web_element = driver.find_element(By.NAME,"username")
    email_web_element.send_keys("admin@admin.com")
    # <input
    # type="password"
    # class="text-input W(700%)"
    # data-qa="jobodapuxe"
    # pramod="dutta"> // custom attribute - []
    # id -> name -> className -> link/partial ( anchor) -> css Selector -> Xpath

    password_web_element = driver.find_element(By.CSS_SELECTOR,"[data-qa='jobodapuxe']")
    password_web_element.send_keys("admin123")
    # <button type="submit" id="js-login-btn" class="btn btn--positive btn--inverted W(100%) H(48px) Fz(16px)" onclick="login.login(event)" data-qa="sibequkica">
    # <span class="icon loader hidden" data-qa="zuyezasugu"></span>
    # <span data-qa="ezazsuguuy">Sign in</span>
    # </button>
    submit_web_element = driver.find_element(By.ID,"js-login-btn")
    submit_web_element.click()
    time.sleep(3)
    # Webdriver to stop for the element instead of sleep() which tells Python interpretor to stop
    error_message_web_element = driver.find_element(By.ID, "js-notification-box-msg")
    assert error_message_web_element.text == "Your email, password, IP address or location did not match"
    time.sleep(5)
    driver.quit()
