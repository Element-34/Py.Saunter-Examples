from saunter.testcase.webdriver import SaunterTestCase
import pytest
from pages.upload import Upload

class CheckFileUpload(SaunterTestCase):
    def setup_method(self, method):
        super(CheckFileUpload, self).setup_method(method)
        self.u = Upload(self.driver).open().wait_until_loaded()

    def teardown_method(self, method):
        super(CheckFileUpload, self).teardown_method(method)

    @pytest.mark.adam
    def test_local_upload(self):
        preview = self.u.upload('english_muffin.jpg')
        self.take_named_screenshot('potato')

    # @pytest.mark.banana
    # def test_banana(self):
    #     self.driver.get("http://www.adobe.com/software/flash/about/")
    #     import time
    #     time.sleep(100000)