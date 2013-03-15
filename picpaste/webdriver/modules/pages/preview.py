from saunter.po.webdriver.page import Page
from selenium.webdriver.support.wait import WebDriverWait
from saunter.po.webdriver.select import Select2
import os.path

locators = {
    'image': 'css=.picture img[src^="/extpics"]:not([alt="new"])',
}

class Preview(Page):
    def __init__(self, driver):
        super(type(self), self).__init__(driver)
        self.driver = driver

    def wait_until_loaded(self):
        self.short_wait.until(lambda driver: driver.find_element_by_locator(locators['image']))
        return self