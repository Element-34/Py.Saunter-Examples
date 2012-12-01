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
from saunter.po.webdriver.select import Select2
from saunter.po import string_timeout, timeout_seconds
from saunter.exceptions import ElementVisiblityTimeout
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper
from saunter.po.webdriver.attribute import Attribute

locators = {
    "collar style": 'css=a[title="REPLACE"] > div:first-child',
    "current search category": 'id=gh-cat',
    "result count": 'id=v4-p308',
}

class CurrentSearchCategory(Select2):
    def __init__(self, driver):
        self.locator = locators["current search category"]
        self.driver = driver

class ShirtPage(Page):
    result_count_class = Attribute(locators["result count"], "class")
    
    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config
        self.current_search_category = CurrentSearchCategory(self.driver)
        
    def go_to_mens_dress_shirts(self):
        self.driver.get("%s/mens-clothing/Dress-Shirts/57991" % self.config.get("Selenium", "base_url"))
        
    def change_collar_style(self, style):
        self.driver.find_element_by_locator(locators["collar style"].replace("REPLACE", style)).click()
        self.wait_for_trobber_sync()
        
    def is_collar_selected(self, style):
        if self.driver.is_element_present("%s .sl-deSel" % locators["collar style"].replace("REPLACE", style)):
            return False
        return True
        
    def get_meta_elements(self):
        return self.driver.find_elements_by_locator("tag=meta")
        
    def get_meta_element(self, name):
        return self.driver.find_element_by_locator('css=meta[name="%s"]' % name)