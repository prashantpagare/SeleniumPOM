from Utilities import configReader


class CarBase:

    def __init__(self, driver):
        self.driver = driver

    def getCarTitle(self):
        return self.driver.find_element_by_xpath(configReader.readConfig("locators", "CarTitle_XPATH")).text

    def getCarNamesAndPrices(self):
        carNames = self.driver.find_elements_by_xpath(configReader.readConfig("locators", "CarNames_XPATH"))
        carPrices = self.driver.find_elements_by_xpath(configReader.readConfig("locators", "CarPrices_XPATH"))

        for i in range(1,len(carPrices)):
            print((carNames[i].text + "Prices are :" + carPrices[i].text).encode('utf8'))


