import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from testCases.test_base import BaseTest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestLogin001(BaseTest):
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    logger =  LogGen.loggen()
    Login_Page_Title = "Swag Labs"
    @pytest.mark.sanity
    def test_login_page_title(self):
        self.logger.info("*************TestLogin001************")
        self.logger.info("*********Verifying Home Page Title*********")
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_login_page_title(self.Login_Page_Title)
        if title == self.Login_Page_Title:
            assert True
         #   self.driver.close()
            self.logger.info("*********Home Page Title Passed*********")
            print(title)
        else:
            self.driver.save_screenshot('.\\Screenshots\\test_login_page_title.png')
         #   self.driver.close()
            self.logger.error("*********Home Page Title Failed*********")
            assert False

    @pytest.mark.regression
    def test_login(self):
        self.logger.info("*********Verify Login Test*********")
        self.loginPage = LoginPage(self.driver)
        self.loginPage.do_login(self.username, self.password)
        title = self.driver.title
        if title == self.Login_Page_Title:
            assert True
            self.logger.info("*********Login Test Passed*********")
        else:
            self.driver.save_screenshot('.\\Screenshots\\test_login.png')
            self.logger.error("*********login Test Failed*********")
            assert False
