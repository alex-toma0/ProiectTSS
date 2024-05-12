from datetime import datetime
from time import sleep
from selenium.webdriver.common.by import By
from SeleniumTests.tests.auth.login import login
from SeleniumTests.config import email, password, title_form_id, img_form_id, genre_form_id, file_form_id, \
    song_title, song_image, song_genre, file_sample


def upload(*browsers) -> None:

    print("Button navigation test started")

    for browser in browsers:
        try:
            browser = browser()
            sleep(2)
            login(browser, email, password)
            profile = browser.find_element(By.XPATH, "//a[contains(text(), 'Profile')]")
            profile.click()
            sleep(2)
            upload_page = browser.find_element(By.XPATH, "//a[contains(text(), 'Upload song')]")
            upload_page.click()

            title_form = browser.find_element(By.ID, title_form_id)
            img_form = browser.find_element(By.ID, img_form_id)
            genre_form = browser.find_element(By.ID, genre_form_id)
            file_form = browser.find_element(By.ID, file_form_id)

            new_title = "".join((str(datetime.now().strftime("%Y%m%d%H%M%S")) + song_title).split())
            title_form.send_keys(new_title)
            img_form.send_keys(song_image)
            genre_form.send_keys(song_genre)
            file_form.send_keys(file_sample)

            upload_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Upload song')]")
            upload_button.click()
            sleep(2)

            alert = browser.switch_to.alert
            alert.dismiss()
            browser.switch_to.default_content()

            home = browser.find_element(By.XPATH, "//a[contains(text(), 'Streaming App')]")
            home.click()
            sleep(5)

            last_song = browser.find_elements(By.CLASS_NAME, "card-title.h5")[-1].text
            # print(last_song)

            if (last_song == new_title):
                print(f"Song {new_title} uploaded successfully")
            else:
                print(f"Song upload failed")

        except Exception as e:
            print(f"Encountered error in {browser.name}: {e}")
        finally:
            print(browser.name + " Upload test finished\n--------")
            browser.quit()
