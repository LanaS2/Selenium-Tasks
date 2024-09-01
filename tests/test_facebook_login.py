import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    driver_path = "C:\\Users\\USER\\chromedriver\\win64-128.0.6613.85\\chromedriver-win64\\chromedriver.exe"
    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service)
    return driver

def load_data():
    file_path = r'C:\Users\USER\PycharmProjects\Selenium\FacebookLoginTask.xlsx'
    df = pd.read_excel(file_path)

    print("Excel Sheet Loaded:")
    print(df)

    if 'Actual Result' not in df.columns:
        df['Actual Result'] = ""
    if 'Status' not in df.columns:
        df['Status'] = ""

    return df

def test_facebook_login(driver, data):
    for index, row in data.iterrows():
        email = row['Email']
        password = row['Password']
        expected_result = row['Expected Result']
        driver.get("https://www.facebook.com")
        driver.maximize_window()

        try:
            email_field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, 'email'))
            )
            password_field = driver.find_element(By.ID, 'pass')
            login_button = driver.find_element(By.NAME, 'login')

            email_field.clear()
            password_field.clear()

            if email != 'empty':
                email_field.send_keys(email)
            if password != 'empty':
                password_field.send_keys(password)

            login_button.click()

            WebDriverWait(driver, 10).until(EC.url_changes("https://www.facebook.com"))

            current_url = driver.current_url
            if "login_attempt" in current_url:
                actual_result = "Login Failure"
            elif "https://www.facebook.com/" in current_url:
                actual_result = "Login Success"
            else:
                actual_result = "Unknown Result"

        except Exception as e:
            actual_result = "Error"
            print(f"Error during login: {e}")

        status = "Pass" if actual_result == expected_result else "Fail"
        data.at[index, 'Actual Result'] = actual_result
        data.at[index, 'Status'] = status

    print("Updated Data:")
    print(data)

    file_path = r'C:\Users\USER\PycharmProjects\Selenium\FacebookLoginTask.xlsx'
    data.to_excel(file_path, index=False)
    print(f"Data saved to {file_path}")
    if not all(data['Status'] == "Pass"):
        raise AssertionError("Some tests failed")

def main():
    driver = setup_driver()
    data = load_data()
    try:
        test_facebook_login(driver, data)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()









