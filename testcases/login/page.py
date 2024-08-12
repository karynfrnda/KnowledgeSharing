from .. import Page, StateInterface as SI
from .states import *
from .locator import LoginLocator
from .interface import LoginInterface


class LoginPage(Page):
    """Login Page action methods"""

    def __init__(self, base, usecase=None):
        print("class - LoginPagee")
        super().__init__(base)
        self.initState: LoginInterface = self.setInitState(usecase)
        self.state = self.initState
        self.lr = LoginLocator(base)

    def setInitState(self, usecase):
        dict = {
            1: LoginInitState(self.bd, self),
        }
        return dict[usecase]

    """
    Method: Abstracts
    """

    # region
    def changeState(self, newState):
        self.state = newState

    def resetState(self):
        self.state = self.initState

    # endregion

    """
    Method: Interfaces
    """

    # region ==> is a Python feature to freely collapsing code, ended with endregion
    @SI.updateParam
    def changeLanguage(self, lang): # merepresentasikan UI nya(hardware)
        return self.state.changeLanguage()
    
    @SI.updateParam
    def clickLogin(self, lang, username, password, login_btn): # merepresentasikan UI nya (hardware)
        return self.state.clickLogin() # nama transition method yang mau kita panggil  

    @SI.updateParam
    def errorDisplayed(self, lang, username, password): # merepresentasikan UI nya (hardware)
        return self.state.errorDisplayed() # nama transition method yang mau kita panggil    
    
    @SI.updateParam
    def successDisplayed(self): # merepresentasikan UI nya(hardware)
        return self.state.successDisplayed() # nama transition method yang mau kita panggil    
    
    # endregion

    """
    Method: Specifics
    """
    # region
    # endregion
