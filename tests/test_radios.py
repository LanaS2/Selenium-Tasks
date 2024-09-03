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
    yield driver
    driver.quit()

def test_radio_button_selection(driver):
    driver.get("file:///C:/Users/USER/PycharmProjects/Selenium/radios_example.html")
    driver.maximize_window()

    radio_button = driver.find_element(By.CSS_SELECTOR, "#radios > div > input:nth-child(7)")
    if not radio_button.is_selected():
        radio_button.click()

    time.sleep(5)
