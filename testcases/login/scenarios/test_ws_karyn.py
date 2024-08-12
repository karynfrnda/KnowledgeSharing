import pytest

from utils.wrapper import Wrapper
from . import TestLogin
import pdb
import time as t

@pytest.mark.dev
@pytest.mark.usefixtures("admin")
@pytest.mark.usefixtures("usecase1")
class TestLogin01(TestLogin):
    def __init__(self, methodName: str = "runTest"):
        # pdb.set_trace()
        print(f"class - TestLogin01")
        super().__init__(methodName)

    # @pytest.mark.dev
    @Wrapper.result_receiving
    @Wrapper.unpagshe(*("WS_Karyn", "_SN_WS_Karyn_Scenario_001_Data"))
    def test_scenario001(self, *args):
        """Test Scenario: 1-1"""

        print(f"lang: {args[0]}")
        print(f"abc1: {args[3]}")
        print(f"abc2: {args[4]}")

        # changeLanguage (1-1)
        t.sleep(5)
        self.soft_assert(
            self.assertIsNone,
            self.p.changeLanguage(lang=args[0]),
        )

        self.assert_all()

    @pytest.mark.dev
    @Wrapper.result_receiving
    @Wrapper.unpagshe(*("WS_Karyn", "_SN_WS_Karyn_Scenario_002_Data"))
    def test_scenario002(self, *args):
        """Test Scenario: 2-1"""

        # changeLanguage (1-1)
        print("changeLanguage")
        self.soft_assert(
            self.assertFalse,
            self.p.changeLanguage(lang=args[0]),
        )

        # clickLogin (1-2)
        print("clickLogin")
        self.soft_assert(
            self.assertIsNone,
            self.p.clickLogin(
                lang=args[5],
                username=args[6] if args[6] else '',
                password=args[7] if args[7] else '',
                login_btn=args[8],
            ),
        )

        # errorDisplayed (2-1)   
        pdb.set_trace()
        print("errorDisplayed(transition)\n")
        self.soft_assert(
            self.assertTrue,
            self.p.errorDisplayed(
                lang=args[5],
                username=args[6], 
                password=args[7],
            ),
        )

        self.assert_all()

    # @pytest.mark.dev
    @Wrapper.result_receiving
    @Wrapper.unpagshe(*("WS_Karyn", "_SN_WS_Karyn_Scenario_003_Data"))
    def test_scenario003(self, *args):
        """Test Scenario: 3-1"""

        # changeLanguage (1-1)
        self.soft_assert(
            self.assertFalse,
            self.p.changeLanguage(lang=args[0])
        )

        # clickLogin (1-2)
        print("clickLogin")
        self.soft_assert(
            self.assertIsNone,
            self.p.clickLogin(
                lang=args[5],
                username=args[6] if args[6] else '',
                password=args[7] if args[7] else '',
                login_btn=args[8],
            ),
        )

        # successDisplayed (2-3)
        pdb.set_trace()
        print("successDisplayed(transition)\n")
        self.soft_assert(
            self.assertTrue,
            self.p.successDisplayed(),
        )        

        # tearDown
        self.tmp.signout()

        self.assert_all()
