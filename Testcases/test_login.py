import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Configurations.Config import testdata
from Utilities.CustomLogger import LogGen
from Testcases.test_base import BaseTest
import pytest_dependency

class Test_Login(BaseTest):
    baseURL= testdata.app_url
    email= testdata.user_email
    password= testdata.user_password

    logger= LogGen.loggen()

    @pytest.mark.dependency(name="login")
    def test_login(self):
        self.logger.info("***Setting up driver***")
        #self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        page_title= self.driver.title
        print(page_title)
        self.logger.info("*** Checking up page title ***")

        if page_title=="Gamesfi":
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+ "login.png")
            assert False
        self.lp= LoginPage(self.driver)
        self.lp.clickMainlogin()
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.logger.info("*** clicking on login button ***")
        self.lp.clickLoginbtn()
        self.logger.info("*** Closing up the driver ***")