import time

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.smoke
@allure.title("Verify the Handling of SVG element ")
@allure.description("Verify the Handling of SVG element in the amcharts SVG Map")
def test_svgelements():
    driver = webdriver.Chrome()
    driver.get("https://www.amcharts.com/svg-maps/?map=india")
    driver.maximize_window()
    states = driver.find_elements(By.XPATH, "//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for state in states:
        print(state.get_attribute("aria-label"))
        if "Tripura" in state.get_attribute("aria-label"):
            state.click()
            break
    time.sleep(10)
    allure.attach(driver.get_screenshot_as_png(), name="svg_elements", attachment_type=AttachmentType.PNG)
    driver.quit()