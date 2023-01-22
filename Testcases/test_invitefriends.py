import time

import pytest
from Configurations.Config import testdata
from Utilities.CustomLogger import LogGen
from Testcases.test_base import BaseTest
from pageObjects.InvitePage import InvitePage
from pageObjects.WithdrawPage import WithdrawPage
from pageObjects.LoginPage import LoginPage

class Test_invite(BaseTest):

    baseURL= testdata.app_url
    email= testdata.user_email
    password= testdata.user_password

    logger= LogGen.loggen()

    def test_invite(self):
        self.logger.info("***Setting up driver***")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.Login = LoginPage(self.driver)
        self.Login.clickMainlogin()
        self.Login.enterEmail(self.email)
        self.Login.enterPassword(self.password)
        self.Login.clickLoginbtn()

        self.invite = InvitePage(self.driver)
        self.invite.clickmenubutton()
        self.invite.clickselectinvite()
        self.invite.clickcopybutton()
        time.sleep(2)
        self.invite.clickhistorytab()
        self.driver.execute_script("window.scrollBy(0,200)")
