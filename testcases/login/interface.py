from .. import StateInterface

from abc import ABC
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .page import LoginPage


class LoginInterface(StateInterface, ABC):
    def __init__(self, base, contextPage: "LoginPage") -> None:
        super().__init__(base)
        self.p = contextPage

    def changeLanguage(self, *args, **kwargs):
        pass
    
    def clickLogin(self, *args, **kwargs):
        pass

    def errorDisplayed(self, *args, **kwargs):
        pass

    def successDisplayed(self, *args, **kwargs):
        pass    