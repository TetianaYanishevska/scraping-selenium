from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
import time
import config
from decorators import social_login_required


class SocialNetworkScraper:
    BASE_URL = f"http://{config.SOCIAL_NETWORK_HOST}:{config.SOCIAL_NETWORK_PORT}"
    REGISTER_URL = f"{BASE_URL}/auth/register"
    LOGIN_URL = f"{BASE_URL}/auth/login"
    BLOG_URL = f"{BASE_URL}/user/blog"

    def __init__(self, driver=None):
        self.driver = driver or self.create_driver()
        self.is_logged_in = False

    def create_driver(self):
        try:
            options = Options()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH, options=options)
            return self.driver
        except Exception as e:
            print(e.args)

    def social_network_register(self):
        self.driver.get(self.REGISTER_URL)

        username_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username_elem.send_keys(config.SOCIAL_NETWORK_LOGIN)

        email_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='email']")
        email_elem.send_keys(config.SOCIAL_NETWORK_EMAIL)

        password_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)

        confirm_password_elem = self.driver.find_element(By.XPATH,
                                                         "//div[@class='form-group']/input[@id='confirm_password']")
        confirm_password_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)
        time.sleep(2)
        confirm_password_elem.send_keys(keys.Keys.ENTER)

    def social_network_login(self):
        self.driver.get(self.LOGIN_URL)

        username_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username_elem.send_keys(config.SOCIAL_NETWORK_LOGIN)

        password_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)
        time.sleep(2)
        password_elem.send_keys(keys.Keys.ENTER)
        self.is_logged_in = True

    @social_login_required
    def social_network_add_post(self, title, content):
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
        time.sleep(2)

    def social_network_like_post(self):
        self.driver.get(self.BLOG_URL)
        like_elems = self.driver.find_elements(By.XPATH, "//div[@class='btn-group']/a[contains(@href, '/like')]")
        if like_elems:
            like_elems[0].click()
        time.sleep(2)

    @social_login_required
    def social_network_logout(self):
        self.driver.get(self.BLOG_URL)
        logout_elem = self.driver.find_element(By.XPATH, "//a[contains(@href, 'logout')]")
        logout_elem.click()
        time.sleep(2)
