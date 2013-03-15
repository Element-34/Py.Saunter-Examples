from saunter.testcase.webdriver import SaunterTestCase
import pytest
from pages.upload import Upload

class CheckFileUpload(SaunterTestCase):
    def setup_method(self, method):
        super(type(self), self).setup_method(method)
        self.u = Upload(self.driver).open().wait_until_loaded()

    def teardown_method(self, method):
        super(type(self), self).teardown_method(method)

    @pytest.mark.adam
    def test_local_upload(self):
        preview = self.u.upload('english_muffin.jpg')
