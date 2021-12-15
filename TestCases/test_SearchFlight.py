import time

import pytest
import softest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from Pages.yatra_launch_page import LaunchPage
from Pages.search_flights_result_page import SearchFlightResults
from Utilities.utils import Utils
from ddt import  ddt, data, unpack, file_data


@pytest.mark.usefixtures("setup")
@ddt

class TestSearchAndVerify(softest.TestCase):
    log = Utils.custom_logger()

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = LaunchPage(self.driver)
        self.ut = Utils()

    #@data(("New Delhi", "JFK", "24/12/2021", "1 Stop"), ("BOM", "JFK", "24/12/2021", "1 Stop"))
    #@unpack
    #@file_data(".\\TestData\\TestData.json")
    #@file_data(".\\TestData\\Test_Yanl.yaml")
    #@data(*Utils.read_data_from_excel("D:\\Learning\\TestFrameworkDemo\\TestData\\Test_Data.xlsx", "Sheet1"))
    #@unpack
    @data(*Utils.read_data_from_csv("D:\\Learning\\TestFrameworkDemo\\TestData\\td_data.csv"))
    @unpack
    def test_search_flight_1_stop(self, goingfrom, goingto, date, stop):

        #Launching Webbrowser
        #Providing Going From Location
        #lp = LaunchPage(self.driver)
        search_flight_result = self.lp.searchFlights(goingfrom, goingto, date)

        #To handle dynamic scroll
        self.lp.page_scroll()

        #Select the filter for 1 stop results
        search_flight_result.filter_flights_by_stop(stop)

        #Verify that filter result show only flights with 1 stop
        allstop1 = search_flight_result.get_search_flight_results()
        self.log.info(len(allstop1))

        #ut = Utils()
        self.ut.assertlistitemsText(allstop1, "1 Stop")










