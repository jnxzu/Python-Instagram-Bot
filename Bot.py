from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self, username, password):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        username_input = driver.find_element_by_xpath("//input[@name='username']")
        pw_input = driver.find_element_by_xpath("//input[@name='password']")
        username_input.send_keys(username)
        pw_input.send_keys(password)
        pw_input.send_keys(Keys.RETURN)
        time.sleep(2)

    def close(self):
        self.driver.close()

    def like(self, hashtag, count):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(2)
        first_pic = driver.find_element_by_tag_name("a")
        first_pic.find_element_by_xpath("..").click()
        i = 0
        while i < count:
            time.sleep(2)
            try:
                driver.find_element_by_xpath("//span[@aria-label='Nie lubię']/..")
                print("Photo already liked.")
                time.sleep(2)
            except Exception:
                driver.find_element_by_xpath(
                    "/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button").click()
                i += 1
                print(f"Liked {i} out of {count} photos.")
                time.sleep(18)
            driver.find_element_by_link_text("Dalej").click()
        self.close()
