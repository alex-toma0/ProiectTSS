import time
from time import sleep
from typing import Callable
from selenium.webdriver.common.by import By
from SeleniumTests.config import chromium_driver, chrome_driver
from SeleniumTests.tests.auth.login import login

# -------------
def run_test(test_function: Callable):
    test_function()
# -------------

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
