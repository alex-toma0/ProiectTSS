from selenium import webdriver

name: str = "a2"
email: str = "a2@a2.com"
password: str = "a2"

email_id: str = "formBasicEmail"
pass_id: str = "formBasicPassword"
name_id: str = "formBasicName"
confirm_pass_id: str = "formConfirmPassword"

register_email: str = "testMail@test.com"
register_name: str = "testName"
register_pass: str = "testPass"

login_url: str = "http://localhost:5173/login"
register_url: str = "http://localhost:5173/register"

# lambdas so the drivers don't get initialized every time they're imported
chrome_driver = lambda: webdriver.Chrome()
edge_driver = lambda: webdriver.Edge()

title_form_id: str = "formSongTitle"
img_form_id: str = "formImagePath"
genre_form_id: str = "formGenre"
file_form_id: str = "formFile"

song_title: str = "Sample"
song_image: str = "https://raw.githubusercontent.com/alex-toma0/images/main/pop-cover.jpg"
song_genre: str = "Pop"

# Requires absolute path
file_sample: str = "E:\Pycharm\Projects\pythonProject3\SeleniumTests\sample.ogg"


