from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

base_url = "https://flyxo"

class BasePage:

    def __init__(self, browser, url, time=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(time)

    def open(self):
        self.browser.get(self.url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator),
                                                       message=f"Can't find elements by locator {locator}")

    def switch_to_new_window(self, time=10):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
        WebDriverWait(self.browser, time).until(EC.number_of_windows_to_be(2))

    def close_new_window_and_switch_to_previous_window(self):
        self.browser.close()
        previous_window = self.browser.window_handles[0]
        self.browser.switch_to.window(previous_window)

    def element_displayed(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_disappeared(self, how, what, time=10):
        try:
            WebDriverWait(self.browser, time, 1).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True