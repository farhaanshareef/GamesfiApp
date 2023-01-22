import time

import pytest
from selenium import webdriver
from pageObjects.SignupPage import SignupPage
from Configurations.Config import testdata
from Utilities.CustomLogger import LogGen
from Testcases.test_base import BaseTest

class Test_Signup(BaseTest):
    baseURL= testdata.app_url
    email= testdata.user_email
    password= testdata.user_password
    referal_code= testdata.referal

    logger= LogGen.loggen()

    def test_signup(self):
        self.logger.info("***Setting up driver***")
        #self.driver= setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.logger.info("*** Checking up page title ***")

        self.lp= SignupPage(self.driver)
        self.lp.clickMainSignup()
        self.lp.enterEmail(self.email)
        self.lp.enterPassword(self.password)
        self.lp.enterRefercode(self.referal_code)
        self.lp.clickCheckbox()
        self.lp.clickSignup()
        time.sleep(2)
        self.logger.info("*** Closing up the driver ***")