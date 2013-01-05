# Copyright 2011 Element 34
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tailored.page import Page

from saunter.po.webdriver.text import Text
from saunter.po.webdriver.text import Unicode
from saunter.po.webdriver.select import Select2
from saunter.po import string_timeout, timeout_seconds
from saunter.exceptions import ElementVisiblityTimeout
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper
from saunter.po.webdriver.attribute import Attribute

locators = {
    "top search": 'id=gh-ac',
    "top search button": 'id=gh-btn',
}

class TopSearchText(Text):
    def __init__(self):
        self.locator = locators['top search']

class TopSearchUnicode(Unicode):
    def __init__(self):
        self.locator = locators['top search']

class ResultsPage(Page):
    top_search_text = TopSearchText()
    top_search_unicode = TopSearchUnicode()
    
    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config
        
    def wait_until_loaded(self):
        def waiter(driver):
            if len(driver.find_elements_by_locator('css=.rsittlref')) == 48:
                return True
        self.wait.until(waiter)
        return self
        
    def validate(self):
        return self