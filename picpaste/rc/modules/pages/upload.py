from saunter.po.remotecontrol.page import Page
from saunter.po.remotecontrol.select import Select
import os.path
from pages.preview import Preview

locators = {
    'upload': 'css=input[name="upload"]',
    'button': 'css=input[type="submit"]',
    'storetime': 'css=select[name="storetime"]',
    'obscure_filename': 'css=select[name="addprivacy"]',
    'accept_rules': 'css=select[name="rules"]',
}

class StoreTime(Select):
    def __init__(self):
        self.locator = locators["storetime"]

class ObscureFilename(Select):
    def __init__(self):
        self.locator = locators["obscure_filename"]

class AcceptRules(Select):
    def __init__(self):
        self.locator = locators["accept_rules"]

class Upload(Page):
    storetime = StoreTime()
    obscure_filename = ObscureFilename()
    accept_rules = AcceptRules()

    def __init__(self):
        super(type(self), self).__init__()

    def open(self):
        self.selenium.open(self.config.get('Selenium', 'base_url'))
        return self

    def wait_until_loaded(self):
        self.wait_for_element_available(locators['upload'])
        return self

    def upload(self, image, storetime="30 Minutes", obscure_filename="basic", accept_rules="Yes"):
        path_to_image = "%s/files/%s" % (self.config.get('YourCompany', 'file_server_base'), image)

        self.selenium.attach_file(locators['upload'], path_to_image)

        self.storetime = "label=%s" % storetime
        self.obscure_filename = "label=%s" % obscure_filename
        self.accept_rules = "label=%s" % accept_rules

        self.selenium.click(locators['button'])

        p = Preview().wait_until_loaded()
        return p