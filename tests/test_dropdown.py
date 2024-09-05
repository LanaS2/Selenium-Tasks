import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

# List of browsers
browsers = ["chrome", "edge"]

@pytest.mark.parametrize("browser", browsers)
def test_dropdown_and_menu(browser):
    if browser == "chrome":
        driver_path = "C:\\Users\\USER\\chromedriver\\win64-128.0.6613.85\\chromedriver-win64\\chromedriver.exe"
        service = ChromeService(executable_path=driver_path)
        driver = webdriver.Chrome(service=service)
    elif browser == "edge":
        driver_path = "C:\\Users\\USER\\OneDrive\\Desktop\\QA\\edgedriver_win64\\msedgedriver.exe"
        service = EdgeService(executable_path=driver_path)
        driver = webdriver.Edge(service=service)

    driver.get("file:///C:/Users/USER/PycharmProjects/Selenium/drop_down_example.html")
    driver.maximize_window()

    x = driver.find_element(By.ID, 'age-range-select')
    drop = Select(x)
    drop.select_by_value("61-80")

    y = driver.find_element(By.ID, 'dropdownMenuButton')
    y.click()
    option = driver.find_element(By.XPATH, "//a[text()='Cart']")
    option.click()

    time.sleep(5)
    driver.quit()
#above is sequantiol
#this will be in parallel
##import pytest
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.edge.service import Service as EdgeService
#from selenium.webdriver.support.ui import Select
#from selenium.webdriver.common.by import By
#import time

#@pytest.fixture(params=["chrome", "edge"])
#def driver(request):
#    if request.param == "chrome":
#        driver_path = "C:\\Users\\USER\\chromedriver\\win64-128.0.6613.85\\chromedriver-win64\\chromedriver.exe"
#        service = ChromeService(executable_path=driver_path)
#        driver = webdriver.Chrome(service=service)
#    elif request.param == "edge":
#        driver_path = "C:\\Users\\USER\\OneDrive\\Desktop\\QA\\edgedriver_win64\\msedgedriver.exe"
#        service = EdgeService(executable_path=driver_path)
#        driver = webdriver.Edge(service=service)

#    driver.get("file:///C:/Users/USER/PycharmProjects/Selenium/drop_down_example.html")
#    driver.maximize_window()
#    yield driver
#    driver.quit()

#def test_dropdown_and_menu(driver):
#    x = driver.find_element(By.ID, 'age-range-select')
#    drop = Select(x)
#    drop.select_by_value("61-80")

#    y = driver.find_element(By.ID, 'dropdownMenuButton')
#    y.click()
#    option = driver.find_element(By.XPATH, "//a[text()='Cart']")
#    option.click()

#    time.sleep(5)



