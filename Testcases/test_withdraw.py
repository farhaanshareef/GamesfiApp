import pytest
from Configurations.Config import testdata
from Utilities.CustomLogger import LogGen
from Testcases.test_base import BaseTest
from pageObjects.WithdrawPage import WithdrawPage
from pageObjects.LoginPage import LoginPage

class Test_withdraw(BaseTest):

    baseURL= testdata.app_url
    email= testdata.user_email
    password= testdata.user_password
    withdraw_user_email= "farhan@yopmail.com"

    logger= LogGen.loggen()

    def test_withdraw(self):
        self.logger.info("***Setting up driver***")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.Login = LoginPage(self.driver)
        self.Login.clickMainlogin()
        self.Login.enterEmail(self.email)
        self.Login.enterPassword(self.password)
        self.Login.clickLoginbtn()

        self.wp= WithdrawPage(self.driver)
        self.wp.clickmenuwithdrawbutton()
        self.wp.clicksubmenuwithdrawbtn()
        self.wp.selectgame()
        self.driver.execute_script("window.scrollBy(0,500)")
        self.wp.clickmaxbutton()
        self.wp.selectpayout()
        self.wp.enterEmail(self.withdraw_user_email)
        self.wp.clickcashout()