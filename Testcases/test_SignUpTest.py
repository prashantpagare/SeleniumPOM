import pytest
from Pages.RegistraionPage import RegistrationPage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_SignUp(BaseTest):

    @pytest.mark.parametrize("name, phone, email, country, city, username, password",
                             dataProvider.get_userData("Sheet1"))
    def test_doSignUp(self, name, phone, email, country, city, username, password):
        log.logger.info("TestCase Started")
        regPage = RegistrationPage(self.driver)
        regPage.fillForm(name, phone, email, country, city, username, password)
        log.logger.info("TestCase Executed Successfully")
