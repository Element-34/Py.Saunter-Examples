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
from harpy.har import Har
import pytest
import StringIO
import saunter.web_element
import types

class CheckTextTypes(SaunterTestCase):    
    @pytest.marks('saunter', 'text', 'goldfish')
    def test_collar_style(self):
        s = ShirtPage(self.driver)
        s.open()
        # nothing in there at first
        assert s.top_search_text == ''
        s.top_search_text = "buckets"
        r = s.push_the_search_button()
        assert s.top_search_text == 'buckets'
        assert type(s.top_search_text) == types.StringType
        assert s.top_search_unicode == 'buckets'
        assert type(s.top_search_unicode) == types.UnicodeType