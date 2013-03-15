from saunter.po.remotecontrol.page import Page
from saunter.po.remotecontrol.select import Select
import os.path

locators = {
    'image': 'css=.picture img[src^="/extpics"]:not([alt="new"])',
}

class Preview(Page):
    def __init__(self):
        super(type(self), self).__init__()

    def wait_until_loaded(self):
        self.wait_for_element_available(locators['image'])
        return self