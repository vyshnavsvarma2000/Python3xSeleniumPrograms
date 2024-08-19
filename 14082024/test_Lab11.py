import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import allure

@pytest.mark.positive
def test_mini_project_4():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    # make_appointment_button = driver.find_element(By.XPATH, "//a[@id='btn-make-appointment']")
    # make_appointment_button = driver.find_element(By.XPATH, "//a[@href='./profile.php#login']")
    # make_appointment_button = driver.find_element(By.XPATH, "//a[text() = 'Make Appointment' and contains(@id, 'btn-make-appointment')]")
    make_appointment_button = driver.find_element(By.CSS_SELECTOR, "#btn-make-appointment")
    make_appointment_button.click()
    time.sleep(5)
    driver.close()