from time import sleep
from selenium.webdriver.common.by import By
from SeleniumTests.config import email, password
from SeleniumTests.tests.auth.login import login

def playback(*browsers) -> None:

    print("Playback test started")
    for browser in browsers:
        try:
            browser = browser()
            login(browser, email, password)

            # Get the first song
            song_cards = browser.find_element(By.CLASS_NAME, 'card-title.h5')
            # print(song_cards.text)

            # Play the first song
            song = browser.find_element(By.XPATH, "//button[contains(text(), 'Play')]")
            song.click()

            sleep(3)
            currently_playing = browser.find_element(By.XPATH, "//span[@class='title']")

            if song_cards.text == currently_playing.text:
                print(f"Song {currently_playing.text} queued correctly")
            else:
                print(f"Song {currently_playing.text} was not queued")
        except Exception as e:
            print(f"Encountered error in {browser.name}: {type(e).__name__}")


