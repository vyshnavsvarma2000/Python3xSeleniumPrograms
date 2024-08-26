import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with


def test_practice():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()

    years_of_experience_element = driver.find_element(By.XPATH, "//span[text()='Years of Experience']")
    radio_button_of_3 = driver.find_element(locate_with(By.ID,"exp-2").to_right_of(years_of_experience_element))
    radio_button_of_3.click()
    time.sleep(10)
    driver.quit()