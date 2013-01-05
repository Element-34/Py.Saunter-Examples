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

from saunter.testcase.webdriver import SaunterTestCase

from pages.shirts import ShirtPage
from pages.advanced_search.motors import Motors
import pytest

class CheckSearchCategories(SaunterTestCase):    
    @pytest.marks('deep', 'ebay', 'select', 'single')
    def test_single_get(self):
        s = ShirtPage(self.driver)
        s.open()
        assert(s.current_search_category.selected == "Clothing, Shoes & Accessories")

    @pytest.marks('deep', 'ebay', 'select', 'single', 'bacon')
    def test_single_set_by_value(self):
        s = ShirtPage(self.driver)
        s.open()
        s.current_search_category.selected = "value=550"
        print(s.current_search_category.options)
        assert(s.current_search_category.selected == "Art")

    @pytest.marks('deep', 'ebay', 'select', 'single')
    def test_single_set_by_index(self):
        s = ShirtPage(self.driver)
        s.open()
        s.current_search_category.selected = "index=2" # indexed from 1
        assert(s.current_search_category.selected == "Art")

    @pytest.marks('deep', 'ebay', 'select', 'single')
    def test_single_set_by_text(self):
        s = ShirtPage(self.driver)
        s.open()
        s.current_search_category.selected = "text=Art"
        assert(s.current_search_category.selected == "Art")
