from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time

import config


class SocialNetworkScraper:
    BASE_URL = f"http://{config.SOCIAL_NETWORK_HOST}:{config.SOCIAL_NETWORK_PORT}"
    LOGIN_URL = f"{BASE_URL}/auth/login"
    BLOG_URL = f"{BASE_URL}/user/blog"

    def __init__(self):
        self.driver = None

    def create_driver(self):
        try:
            self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
            return self.driver
        except Exception as e:
            print(e.args)

    def social_network_login(self):
        driver = self.create_driver()
        driver.get(self.LOGIN_URL)

        username_elem = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username_elem.send_keys(config.SOCIAL_NETWORK_LOGIN)

        password_elem = driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)
        password_elem.send_keys(keys.Keys.ENTER)

        return driver

    def social_network_add_post(self, title, content, login_required=True):
        if login_required:
            self.driver = self.social_network_login()

        self.driver.get(self.BLOG_URL)
        time.sleep(1)

        title_elem = self.driver.find_element(By.ID, 'title')
        title_elem.send_keys(title)
        time.sleep(1)

        content_elem = self.driver.find_element(By.ID, 'content')
        content_elem.send_keys(content)
        time.sleep(1)

        create_post_elem = self.driver.find_element(By.XPATH, "//form/button[@type='submit']")
        create_post_elem.click()
        time.sleep(1)
