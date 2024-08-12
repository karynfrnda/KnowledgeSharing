import pytest
import softest

from ..page import LoginPage
from testcases.topmenu.page import TopmenuPage 


@pytest.mark.order(1)
@pytest.mark.usefixtures("setup")
class TestLogin(softest.TestCase):
    """Test cases for Login page"""

    @pytest.fixture(autouse=True)
    # def class_setup(self, auth, request):
    def class_setup(self, request):
        print(f"def: class_setup")
        self.p = LoginPage(self.base, request.cls.usecase)
        self.tmp = TopmenuPage(self.base)