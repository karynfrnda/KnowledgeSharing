from .. import Page, StateInterface as SI
from .locator import TopmenuLocator
from utils.explicit_wait import explicit

class TopmenuPage(Page):
    """Topmenu Page action methods"""

    def __init__(self, base, usecase=None):
        super().__init__(base)
        self.lr = TopmenuLocator(base)
        

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
    def simpleTransition(self, simpleParam):
        return self.state.simpleTransition()

    # endregion

    """
    Method: Specifics
    """
    # region
    def signout(self):
        explicit(lambda: self.bd.mkd.clicking(self.lr.TOP_RIGHT_PROFILE()))
        explicit(lambda: self.bd.mkd.clicking(self.lr.SIGNOUT()))
    # endregion
