import time

import pytest
from Configurations.Config import testdata
from Utilities.CustomLogger import LogGen
from Testcases.test_base import BaseTest
from pageObjects.ChangePasswordPage import ChangePasswordPage
from pageObjects.InvitePage import InvitePage
from pageObjects.WithdrawPage import WithdrawPage
from pageObjects.LoginPage import LoginPage

class Test_changepass(BaseTest):

    baseURL= testdata.app_url
    email= testdata.user_email
    password= testdata.user_password

    old_password= "12345"
    new_password= "12345"
    confirm_password= "12345"

    logger= LogGen.loggen()

    def test_changepass(self):
        self.logger.info("***Setting up driver***")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.Login = LoginPage(self.driver)
        self.Login.clickMainlogin()
        self.Login.enterEmail(self.email)
        self.Login.enterPassword(self.password)
        self.Login.clickLoginbtn()

        self.cp= ChangePasswordPage(self.driver)
        self.cp.clickmenubutton()
        self.cp.clickChangepassword()
        self.cp.enteroldpassword(self.old_password)
        self.cp.enternewpassword(self.new_password)
        self.cp.enterconfirmpassword(self.confirm_password)
        self.cp.clicksavebtn()
        time.sleep(2)

