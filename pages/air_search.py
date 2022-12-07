from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from .base_page import BasePage
from .locators import SearchLocators
import pytest_check as check


class AirSearch(BasePage):

    def air_search(self):
        where_from = self.find_element(SearchLocators.WHERE_FROM)
        where_to = self.find_element(SearchLocators.WHERE_TO)

        where_from.click()
        self.browser.execute_script("window.scrollBy(0, 100);")
        self.find_element(SearchLocators.LIST_NEARBY).click()
        check.equal("Zvartnots Intl", where_from.get_attribute("value"))

        where_to.send_keys("Lisbon")
        self.find_element(SearchLocators.LIST_TO).click()
        check.equal("Humberto Delgado", where_to.get_attribute("value"))

        self.find_element(SearchLocators.BUTTON_SEARCH).click()
        WebDriverWait(self.browser, 10).until(EC.url_changes(self.browser.current_url))
        check.is_in("search", self.browser.current_url)

        self.find_element(SearchLocators.AIR_CLASS_HEAVY).click()
        check.equal("Heavy", self.find_element(SearchLocators.SELECTED_CLASS).text)
