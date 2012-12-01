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
from saunter.po.webdriver.multi_select import MultiSelect
from saunter.po import string_timeout, timeout_seconds
from saunter.exceptions import ElementVisiblityTimeout
from saunter.ConfigWrapper import ConfigWrapper as cfg_wrapper

locators = {
    "fisc": "id=fisc",
}

class FISC(MultiSelect):
    def __init__(self):
        self.locator = locators["fisc"]

class Motors(Page):
    fisc = FISC()
    
    def __init__(self, driver):
        self.driver = driver
        self.config = cfg_wrapper().config
        
    def open(self):
        self.driver.get("http://www.ebay.com/sch/ebayadvsearch/?_sofindtype=21&_kw=ebayadvsearch&_since=15&_sop=12&_ipg=50")
        return self
        
    def wait_until_loaded(self, style):
        pass
