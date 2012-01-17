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

import pytest

class EbayExample(SaunterTestCase):
    @pytest.marks('shallow', 'ebay', 'shirts')
    def test_collar_style(self):
        s = ShirtPage()
        s.go_to_mens_dress_shirts()
        s.change_collar_style("Banded (Collarless)")
        assert(s.is_collar_selected("Banded (Collarless)"))

    @pytest.marks('deep', 'ebay', 'meta')
    def test_meta(self):
        s = ShirtPage()
        s.go_to_mens_dress_shirts()
        metas = s.get_meta_elements()
        assert(len(metas) == 7)
        
        keywords = s.get_meta_element("keywords")
        assert(keywords.get_attribute("Content") == "Dress Shirts")

        description = s.get_meta_element("description")
        assert(description.get_attribute("Content") == "Shop eBay Fashion for the most dynamic selection of affordable, new  Dress Shirts Items. Find the best deals on new and used fashion.  Learn more about eBay Buyer Protection.")
