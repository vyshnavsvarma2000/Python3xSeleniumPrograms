import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from allure_commons.types import AttachmentType

@pytest.mark.smoke
@allure.title("Verify the Handling of SVG- Flipkart")
@allure.description("Verify the handling of svg element in the flipkart.com website to search for a product")
def test_flipkart():
    driver = webdriver.Chrome()
    driver.get("https://flipkart.com")
    driver.maximize_window()
    # search_input = driver.find_element(By.NAME, "q")
    search_input = driver.find_element(By.XPATH, "//input[@class='Pke_EE']")
    search_input.send_keys("AC")
    svg_list = driver.find_elements(By.XPATH, "//*[local-name()='svg']")
    svg_list[0].click()
    time.sleep(5)
    allure.attach(driver.get_screenshot_as_png(), name="svg_element_flipkart", attachment_type=AttachmentType.PNG)
    driver.quit()



