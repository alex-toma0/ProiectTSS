from SeleniumTests.config import login_url, email_id, pass_id, email, password
from selenium.webdriver.common.by import By

def login(browser) -> bool:

    try:
        browser.get(login_url)
        email_form = browser.find_element(By.ID, email_id)
        pass_form = browser.find_element(By.ID, pass_id)
        login_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Login')]")

        email_form.send_keys(email)
        pass_form.send_keys(password)

        login_button.click()
        genre_button = browser.find_element(By.XPATH, "//*[contains(text(), 'Genre')]")

        if (genre_button.is_displayed()):
            return True
        return False
    except Exception as e:
        print(f"Encountered error in {browser.name}: {e}")
