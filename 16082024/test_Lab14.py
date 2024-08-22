import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.positive
def test_vwo_login_invalid():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    make_app = driver.find_element(By.CSS_SELECTOR, "#btn-make-appointment")
    make_app.click()
    WebDriverWait(driver=driver, timeout=10).until(
        EC.url_contains("profile.php#login")
    )

    username = driver.find_element(By.CSS_SELECTOR, "#txt-username")
    password = driver.find_element(By.CSS_SELECTOR, "#txt-password")
    username.send_keys("John Doe")
    password.send_keys("ThisIsNotAPassword")