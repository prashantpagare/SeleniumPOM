from Pages.BasePage import BasePage
from Pages.NewCarPage import NewCarPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def gotoNewCars(self):
        self.moveTo("newCar_XPATH")
        self.click("findNewCars_XPATH")
        return NewCarPage(self.driver)

    def gotoCompareCars(self):
        pass

    def gotoUsedCars(self):
        pass