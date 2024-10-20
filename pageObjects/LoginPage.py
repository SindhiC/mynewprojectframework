from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By

from pageObjects.BasePage import BasePage
class LoginPage(BasePage):
    """By Locators - OR"""
    baseURL = ReadConfig.getApplicationURL()
    username = (By.ID, "user-name")
    Password = (By.ID, "password")
    Login_Button = (By.ID, "login-button")
    # Open_Menu = (By.XPATH, "//button[normalize-space()='Open Menu']")
    # Logout_Button = (By.LINK_TEXT, "Logout")

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(self.baseURL)

    """Page Actions for Login Page"""
    """this is used to get the page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """this is used to login to the app"""
    def do_login(self, username, password):
        self.do_clear(self.username)
        self.do_send_keys(self.username, username)
        self.do_clear(self.Password)
        self.do_send_keys(self.Password, password)
        self.do_click(self.Login_Button)
      #  self.do_click(self.Logout_Button)




