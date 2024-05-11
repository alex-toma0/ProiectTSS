import time
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

    sleep(2)

def home_tests(*browsers) -> None:
    for browser in browsers:
        try:

            # Check Navigation - login - profile page - back to home page
            login(browser)
            profile = browser.find_element(By.XPATH, "//a[contains(text(), 'Profile')]")
            profile.click()
            time.sleep(2)

            home = browser.find_element(By.XPATH, "//a[contains(text(), 'Streaming App')]")
            home.click()
            sleep(2)

            genre_button = browser.find_element(By.XPATH, "//*[contains(text(), 'Genre')]")

            if (genre_button.is_displayed()):
                print(f"{browser.name}: {genre_button.text} button is visible")

            sleep(2)

        except Exception as e:
            print(f"Encountered error in {browser.name}: {e}")

        finally:
            browser.quit()

# ---------------------------

run_test(lambda: home_tests(chromium_driver, chrome_driver))
