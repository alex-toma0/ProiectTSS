from SeleniumTests.config import login_url, email_id, pass_id
from selenium.webdriver.common.by import By
from time import sleep

def login(browser, email: str, password: str) -> None:

    browser.get(login_url)
    email_form = browser.find_element(By.ID, email_id)
    pass_form = browser.find_element(By.ID, pass_id)
    login_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Login')]")

    email_form.send_keys(email)
    pass_form.send_keys(password)

    login_button.click()

    sleep(2)
