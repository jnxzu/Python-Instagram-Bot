from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Bot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        username_input = driver.find_element_by_xpath("//input[@name='username']")
        pw_input = driver.find_element_by_xpath("//input[@name='password']")
        username_input.send_keys(self.username)
        pw_input.send_keys(self.password)
        pw_input.send_keys(Keys.RETURN)

    def close(self):
        self.driver.close()
