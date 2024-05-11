from time import sleep
from typing import Callable
from selenium import webdriver
from selenium.webdriver.common.by import By

# ----------------------------
email: str = "a2@a2.com"
password: str = "a2"

# email form id = "formBasicEmail"
# password form id = "formBasicPassword"

login_url: str = "http://localhost:5173/login"
chrome_driver = webdriver.Chrome()
chromium_driver = webdriver.Edge()

# -------------
def run_test(test_function: Callable):
    test_function()
# -------------


def login(browser) -> None:
    
    browser.get(login_url)
    email_form = browser.find_element(By.ID, "formBasicEmail")
    pass_form = browser.find_element(By.ID, "formBasicPassword")
    login_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Login')]")

    email_form.send_keys(email)
    pass_form.send_keys(password)

    login_button.click()

def home_tests(*browsers) -> None:
    try:
        for browser in browsers:
            
            login(browser)

            sleep(2)

            genre_button = browser.find_element(By.XPATH, "//*[contains(text(), 'Genre')]")

            if (genre_button.is_displayed()):
                print(f"{browser.name}: {genre_button.text} button is visible")

            sleep(3)

    except Exception as e:
        print(e)

    finally:
        chrome_driver.quit()

# ---------------------------

run_test(lambda: login_tests(chrome_driver, chromium_driver))
