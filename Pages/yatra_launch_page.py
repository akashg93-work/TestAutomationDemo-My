import logging
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Base.base_driver import BaseDriver
from Pages.search_flights_result_page import SearchFlightResults
from Utilities.utils import Utils


class LaunchPage(BaseDriver):

    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        #self.wait = wait
        #Locators

    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id = 'BE_flight_arrival_city']"
    SELECT_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    GOING_TO_RESULT_LIST = "//div[@class='viewport']//div[1]/li"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"
    SEARCH_BUTTON = "//input[@value='Search Flight']"

    def getDepartFromField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.DEPART_FROM_FIELD)

    def getGoingToField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_FIELD)

    def getGoingToResults(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.GOING_TO_RESULT_LIST)

    def getGetDepartureDateField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SELECT_DATE_FIELD)

    def getAllDatesField(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.ALL_DATES)

    def getSearchButton(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.SEARCH_BUTTON)



    def enterDepartFromLocation(self, departlocation):
        self.getDepartFromField().click()
        self.getDepartFromField().send_keys(departlocation)
        self.getDepartFromField().send_keys(Keys.ENTER)



    def enterGoingToLocation(self, goingtolocation):
        self.getGoingToField().click()
        self.log.info("Clicked on Going To")
        time.sleep(2)
        self.getGoingToField.send_keys(goingtolocation)
        self.log.info("Typed Text into Going To Field Successfully")
        time.sleep(2)
        search_results = self.getGoingToResults()
        for results in search_results:
            if goingtolocation in results.text:
                results.click()
                break

    def enterDepartureDate(self, departuredate):
        self.getGetDepartureDateField().click()
        all_dates = self.getAllDatesField().find_element(By.XPATH, self.ALL_DATES)
        for date in all_dates:
            if date.get_attribute("data-date") == departuredate:
                date.click()
                break

    def clickSearchFlightButton(self):
        self.getSearchButton().click()
        time.sleep(4)

    def searchFlights(self, departlocation, goingtolocation, departuredate):
        self.enterDepartFromLocation(departlocation)
        self.enterGoingToLocation(goingtolocation)
        self.enterDepartureDate(departuredate)
        self.clickSearchFlightButton()
        search_flights_result = SearchFlightResults(self.driver)
        return search_flights_result

    """    

            #search_results = self.wait.until(
             #   EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div/li")))

            search_results = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@class='viewport']//div/li")

            for results in search_results:

                if goingtolocation in results.text:
                    results.click()
                    break


        def selectdate(self, departuredate):
            self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_date']"))).click()
            #all_dates = self.wait.until(
            #    EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']"))) \
            #   .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")

            all_dates = self.wait_until_element_is_clickable(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']").find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']").click()




            for date in all_dates:
                if date.get_attribute("data-date") == departuredate:
                    date.click()
                    break

        def clicksearch(self):
            self.driver.find_element(By.XPATH, "//input[@value='Search Flight']").click()
            time.sleep(4)
            """
