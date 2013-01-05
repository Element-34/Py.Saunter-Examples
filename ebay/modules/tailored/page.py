from saunter.po.webdriver.page import Page as SaunterPage
from saunter.po import timeout_seconds
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
import time

locators = {
    "throbber": 'id=v4-p180_throb'
}

class Page(SaunterPage):
    def __init__(self, driver):
        super(type(self), self).__init__(driver)

    def wait_for_trobber_sync(self):
        w = WebDriverWait(self.driver, self.config.getint('Selenium', 'timeout'))
        w.until(lambda x: x.find_element_by_id(locators["throbber"][3:]))

