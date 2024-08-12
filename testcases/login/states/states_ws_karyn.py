from ..interface import LoginInterface
import pdb

#1
class LoginInitState(LoginInterface): # Representate STATE on state diagram 
    def __init__(self, base, contextPage) -> None:
        print("class - LoginInitState")
        super().__init__(base, contextPage)

    def changeLanguage(self):  # Representate TRANSITION on state diagram
        """Required Process"""

        print("lang:", self.param["lang"])

        if self.param["lang"] == "english":
            self.bd.mkd.clicking(self.p.lr.ENG_FLAG_BUTTON())
        elif self.param["lang"] == "japanese":
            self.bd.mkd.clicking(self.p.lr.JPN_FLAG_BUTTON())

        """Transition"""
        self.p.changeState(LoginInitState(self.bd, self.p))

    def clickLogin(self):
        """Required Process"""
        print(f"username: {self.param['username']}")
        print(f"password: {self.param['password']}")
        print(f"login_btn: {self.param['login_btn']}")

        if self.param["lang"] == "english":
            self.bd.fd.insert_to_textbox(self.p.lr.ENG_TXT_USERNAME(), input=self.param["username"])
            self.bd.fd.insert_to_textbox(self.p.lr.ENG_TXT_PASSWORD(), input=self.param["password"], byEnter= not self.param["login_btn"])
        else:
            self.bd.fd.insert_to_textbox(self.p.lr.JAP_TXT_USERNAME(), input=self.param["username"])
            self.bd.fd.insert_to_textbox(self.p.lr.JAP_TXT_PASSWORD(), input=self.param["password"], byEnter= not self.param["login_btn"])

        if (self.param["login_btn"]):
            print("login button CLICKED!")
            self.bd.mkd.clicking(self.p.lr.BTN_LOGIN())

        """Transition"""
        self.p.changeState(LoginProcessState(self.bd, self.p))

# 2
class LoginProcessState(LoginInterface):
    def __init__(self, base, contextPage) -> None:
        pdb.set_trace()
        super().__init__(base, contextPage)

    def errorDisplayed(self):
        validFlag = False
        
        """Required Process"""
        if (self.param["username"] and self.param["password"]): # both not empty but wrong username/password
            print(f"username pass invalid")
            if (self.param["lang"] == "english" or self.param["lang"] == "japanese"):
                validFlag = (True if self.p.lr.WARN_MSG_USERNAME_PASSWORD() != None else False)
        
        if (not self.param["username"]): # username empty
            print(f"username empty!")
            if (self.param["lang"] == "english"):
                validFlag = (True if self.p.lr.ENG_WARN_MSG_USERNAME() != None else False)
            else:
                validFlag = (True if self.p.lr.JAP_WARN_MSG_USERNAME() != None else False)
        
        if (not self.param["password"]): # password empty
            print(f"password empty!")
            if (self.param["lang"] == "english"):
                validFlag = (True if self.p.lr.ENG_WARN_MSG_PASSWORD() != None else False)
            else:
                validFlag = (True if self.p.lr.JAP_WARN_MSG_PASSWORD() != None else False)

        """Transition"""
        self.p.changeState(LoginInitState(self.bd, self.p))
        print("error validFlag: ", validFlag)
        return validFlag

    def successDisplayed(self):
        """Required Process"""
        succ_login = True if self.p.lr.BBUI_LABEL() else False
        
        """Transition"""
        self.p.changeState(HomePageState(self.bd, self.p))
        
        return succ_login        

#3
class HomePageState(LoginInterface):
    def __init__(self, base, contextPage) -> None:
        super().__init__(base, contextPage)