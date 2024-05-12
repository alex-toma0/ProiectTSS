from selenium import webdriver

name: str = "a2"
email: str = "a2@a2.com"
password: str = "a2"

email_id: str = "formBasicEmail"
pass_id: str = "formBasicPassword"

login_url: str = "http://localhost:5173/login"

# lambdas so the drivers don't get initialized every time they're imported 
chrome_driver = lambda: webdriver.Chrome()
edge_driver = lambda: webdriver.Edge()

