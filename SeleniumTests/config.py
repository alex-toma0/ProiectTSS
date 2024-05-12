from selenium import webdriver

email: str = "a2@a2.com"
password: str = "a2"

email_id: str = "formBasicEmail"
pass_id: str = "formBasicPassword"

login_url: str = "http://localhost:5173/login"
chrome_driver = webdriver.Chrome()
chromium_driver = webdriver.Edge()
