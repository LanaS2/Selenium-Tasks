import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


@pytest.fixture
def driver():
    driver_path = "C:\\Users\\USER\\chromedriver\\win64-128.0.6613.85\\chromedriver-win64\\chromedriver.exe"
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    driver.get("file:///C:/Users/USER/PycharmProjects/Selenium/checkbox_example.html")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_check_and_uncheck_checkboxes(driver):
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

    for checkbox in checkboxes:
        if not checkbox.is_selected():
            checkbox.click()

    time.sleep(3)

    def unselect_checkbox(index):
        if index < len(checkboxes) and checkboxes[index].is_selected():
            checkboxes[index].click()
            time.sleep(2)

    unselect_checkbox(1)
    unselect_checkbox(3)
    time.sleep(3)

