import time
from time import sleep
from typing import Callable
from selenium.webdriver.common.by import By
from SeleniumTests.tests.auth.login import login
from SeleniumTests.config import name


# -------------
def run_test(test_function: Callable):
    test_function()
# -------------


def profile_test(*browsers) -> None:

    print("Profile test started")
    for browser in browsers:
        try:
            browser = browser()
            sleep(2)
            login(browser)
            profile = browser.find_element(By.XPATH, "//a[contains(text(), 'Profile')]")
            profile.click()
            sleep(2)

            print(browser.name + ":")
            try:
                user_pfp = browser.find_element(By.XPATH, '//*[@id="root"]/div[2]/div/div[1]/img')
                if (user_pfp.is_visible()):
                    print(f"User pfp is visible")
                else:
                    print("User pfp not visible")
            except Exception:
                print("Couldn't locate user pfp")

            try:
                username = browser.find_element(By.XPATH, f"//*[contains(text(), {name})]")
                if (username.is_displayed()):
                    print("Username label is visible")
                else:
                    print("Username label not visible")
            except Exception:
                print("Couldn't locate username label")

            try:
                upload_button = browser.find_element(By.XPATH, "//a[contains(text(), 'Upload song')]")
                if (upload_button.is_displayed()):
                    print("User upload button is visible")
                else:
                    print("User upload button not visible")
            except Exception:
                print("Couldn't locate user upload button")


        except Exception as e:
            print(f"Encountered error in {browser.name}: {type(e).__name__}")
        finally:
            print(browser.name + " Profile test finished\n--------")
            browser.quit()
# ---------------------------
