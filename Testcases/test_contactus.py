import time

import pytest
from Configurations.Config import testdata
from Utilities.CustomLogger import LogGen
from Testcases.test_base import BaseTest
from pageObjects.ContactusPage import ContactusPage
from pageObjects.WithdrawPage import WithdrawPage
from pageObjects.LoginPage import LoginPage

class Test_contact(BaseTest):

    baseURL= testdata.app_url
    name= "test"
    email= testdata.user_email
    message= "testing data"

    logger= LogGen.loggen()

    def test_contact(self):
        self.logger.info("***Setting up driver***")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.cu= ContactusPage(self.driver)
        self.cu.clickcontactus()
        self.driver.execute_script("window.scrollBy(0,1500)")
        time.sleep(2)
        self.cu.entername(self.name)
        self.cu.enteremail(self.email)
        self.cu.entermessage(self.message)
        self.cu.clicksubmit()
        time.sleep(2)