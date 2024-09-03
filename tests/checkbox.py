from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = "C:\\Users\\USER\\chromedriver\\win64-128.0.6613.85\\chromedriver-win64\\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.get("file:///C:/Users/USER/PycharmProjects/Selenium/checkbox_example.html")
driver.maximize_window()

checkbox = driver.find_element(By.CSS_SELECTOR, "#checkboxes > div > input:nth-child(4)")

if not checkbox.is_selected():
    checkbox.click()
    print("Checkbox selected.")
    time.sleep(5)

if checkbox.is_selected():
    checkbox.click()
    print("Checkbox unselected.")
    time.sleep(5)

driver.quit()

