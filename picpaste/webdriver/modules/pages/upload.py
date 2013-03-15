from saunter.po.webdriver.page import Page
from selenium.webdriver.support.wait import WebDriverWait
from saunter.po.webdriver.select import Select2
import os.path
from pages.preview import Preview

locators = {
    'upload': 'css=input[name="upload"]',
    'button': 'css=input[type="submit"]',
    'storetime': 'css=select[name="storetime"]',
    'obscure_filename': 'css=select[name="addprivacy"]',
    'accept_rules': 'css=select[name="rules"]',
}

class StoreTime(Select2):
    def __init__(self, driver):
        self.locator = locators["storetime"]
        self.driver = driver

class ObscureFilename(Select2):
    def __init__(self, driver):
        self.locator = locators["obscure_filename"]
        self.driver = driver

class AcceptRules(Select2):
    def __init__(self, driver):
        self.locator = locators["accept_rules"]
        self.driver = driver

class Upload(Page):
    def __init__(self, driver):
        super(type(self), self).__init__(driver)
        self.driver = driver
        self.storetime = StoreTime(driver)
        self.obscure_filename = ObscureFilename(driver)
        self.accept_rules = AcceptRules(driver)

    def open(self):
        self.driver.get(self.config.get('Selenium', 'base_url'))
        return self

    def wait_until_loaded(self):
        self.short_wait.until(lambda driver: driver.find_element_by_locator(locators['upload']))
        return self

    def upload(self, image, storetime="30 Minutes", obscure_filename="basic", accept_rules="Yes"):
        path_to_image = os.path.join(self.config.get('Saunter', 'base'), 'support', 'files', image)

        u = self.driver.find_element_by_locator(locators['upload'])
        u.send_keys(path_to_image)

        self.storetime.selected = "text=%s" % storetime
        self.obscure_filename.selected = "text=%s" % obscure_filename
        self.accept_rules.selected = "text=%s" % accept_rules

        button = self.driver.find_element_by_locator(locators['button'])
        button.click()

        p = Preview(self.driver).wait_until_loaded()
        return p