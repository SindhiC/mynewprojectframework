import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from testCases.test_base import BaseTest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class TestLoginDDT002(BaseTest):
    path = ".//TestData/LoginData.xlsx"
    logger =  LogGen.loggen()
    Login_Page_Title = "Swag Labs"
    @pytest.mark.regression
    def test_login(self):
        self.logger.info("**********TestLoginDDT002**********")
        self.logger.info("*********Verify Login Test*********")
        self.loginPage = LoginPage(self.driver)
        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("Number of rows in a excel:", self.rows)
        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1',r,1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r,2)
            #self.exp = XLUtils.readData(self.path, 'Sheet1', r,3)
            self.loginPage.do_login(self.user, self.password)
            title = self.driver.title
            if title == self.Login_Page_Title:
                assert True
                self.logger.info("*********Login Test Passed*********")
            else:
                self.driver.save_screenshot('.\\Screenshots\\test_login.png')
                self.logger.error("*********login Test Failed*********")
                assert False
