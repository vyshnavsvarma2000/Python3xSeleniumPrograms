# Actions and Windows, and Iframe.
import time

from selenium.webdriver.common.action_chains import ActionChains, ActionBuilder
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton


def test_2_actions():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    # click - Normal Driver, will find the element and click on it. release it.
    # click and Hold -> click and Hold, we will not release it.
    atag = driver.find_element(By.ID, "click")
    atag.click()
    time.sleep(3)

    # Actions Builders - Mouse interactions

    action_builders = ActionBuilder(driver)
    action_builders.pointer_action.pointer_up(MouseButton.BACK)
    action_builders.perform()

    time.sleep(10)
    driver.quit()
