from time import sleep
from selenium.webdriver.common.by import By
from SeleniumTests.tests.auth.login import login


def back_to_home_test(*browsers) -> None:

    print("Button navigation test started")

    for browser in browsers:
        try:
            # Check Navigation - login - profile page - back to home page
            browser = browser()
            sleep(2)
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
            print(f"Encountered error in {browser.name}: {type(e).__name__}")
        finally:
            print(browser.name + " Navigation test finished\n-------")
            browser.quit()
