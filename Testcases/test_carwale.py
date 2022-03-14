import time
import pytest

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from Testcases.BaseTest import BaseTest
from Utilities import dataProvider
import logging
from Utilities.LogUtil import Logger

log = Logger(__name__, logging.INFO)


class Test_Carwale(BaseTest):

    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.logger.info("***** Inside New Car Test *****")
        home = HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(5)

    @pytest.mark.skip
    @pytest.mark.parametrize("carBrand,carTitle", dataProvider.get_userData("Sheet2"))
    def test_selectCar(self, carBrand, carTitle):
        log.logger.info("***** Inside Select New Car Test *****")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        if carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print("Car Title: " + title)
            assert title == carTitle, "Not Matching not on the Matching car page"
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print("Car Title: " + title)
            assert title == carTitle, "Not Matching not on the Matching car page"
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print("Car Title: " + title)
            assert title == carTitle, "Not Matching not on the Matching car page"
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print("Car Title: " + title)
            assert title == carTitle, "Not Matching not on the Matching car page"

    @pytest.mark.parametrize("carBrand,carTitle", dataProvider.get_userData("Sheet2"))
    def test_printCarNamesAndPrices(self, carBrand, carTitle):
        log.logger.info("***** Print Car Names and Prices Test *****")
        home = HomePage(self.driver)
        car = CarBase(self.driver)

        if carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = car.getCarTitle()
            print(("Car Title: " + title).encode('utf8'))
            assert title == carTitle, "Not Matching not on the Matching car page"
            car.getCarNamesAndPrices()
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = car.getCarTitle()
            print(("Car Title: " + title).encode('utf8'))
            assert title == carTitle, "Not Matching not on the Matching car page"
            car.getCarNamesAndPrices()
        elif carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = car.getCarTitle()
            print(("Car Title: " + title).encode('utf8'))
            assert title == carTitle, "Not Matching not on the Matching car page"
            car.getCarNamesAndPrices()
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = car.getCarTitle()
            print(("Car Title: " + title).encode('utf8'))
            assert title == carTitle, "Not Matching not on the Matching car page"
            car.getCarNamesAndPrices()
