import webbrowser
from time import sleep
from selenium.webdriver.common.by import By
from SeleniumTests.tests.auth.login import login
from SeleniumTests.config import register_url, \
    register_name, register_email, register_pass, email_id, pass_id, name_id, confirm_pass_id
from datetime import datetime
def register_test(*browsers) -> None:

    print("Register test started")

    for browser in browsers:
        try:
            browser = browser()
            browser.get(register_url)

            email_form = browser.find_element(By.ID, email_id)
            display_name_form = browser.find_element(By.ID, name_id)
            pass_form = browser.find_element(By.ID, pass_id)
            confirm_pass_form = browser.find_element(By.ID, confirm_pass_id)
            create_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Create account')]")

            # Avoid "user already exists" error
            new_email = "".join((str(datetime.now().strftime("%Y%m%d%H%M%S")) + register_email).split())
            # print(new_email)
            email_form.send_keys(new_email)
            display_name_form.send_keys(register_name)
            pass_form.send_keys(register_pass)
            confirm_pass_form.send_keys(register_pass)
            create_button.click()

            sleep(2)
            login(browser, new_email, register_pass)
            sleep(2)
            if browser.find_element(By.XPATH, "//*[contains(text(), 'Genre')]"):
                print(f"Register and login processes successful")
            sleep(2)

        except Exception as e:
            print(f"Encountered error in {browser.name}: {type(e).__name__}")
        finally:
            print(browser.name + " Register test finished\n-------")
            browser.quit()

