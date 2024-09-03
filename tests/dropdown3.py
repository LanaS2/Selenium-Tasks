from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver_path = "C:\\Users\\USER\\chromedriver\\win64-128.0.6613.85\\chromedriver-win64\\chromedriver.exe"
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)

driver.get("file:///C:/Users/USER/PycharmProjects/Selenium/drop_down_example.html")
driver.maximize_window()


x = driver.find_element(By.ID, 'age-range-select')
drop = Select(x)
drop.select_by_value("21-40")


time.sleep(10)
driver.quit()
