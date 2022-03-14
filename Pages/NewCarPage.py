from Pages.BasePage import BasePage


class NewCarPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def selectHyundai(self):
        self.click("HyundaiCar_XPATH")

    def selectToyota(self):
        self.click("ToyotaCar_XPATH")

    def selectBMW(self):
        self.click("BMWCar_XPATH")

    def selectHonda(self):
        self.click("HondaCar_XPATH")