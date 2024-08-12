from .. import Locator


class LoginLocator(Locator):
    """Login page locator class"""

    def __init__(self, base) -> None:
        super().__init__(base)
        self.setup()

    def setup(self):
        # FLAG
        self.ENG_FLAG_BUTTON = lambda loc="(//label[@role='button'])[2]": self.bd.wd.clickable(self.by.xpath, loc)
        self.JPN_FLAG_BUTTON = lambda loc="//label[1]//div[1]//div[1]": self.bd.wd.clickable(self.by.xpath, loc)

        # LOGIN FIELDS
        self.ENG_TXT_USERNAME = lambda loc="//input[@placeholder='Enter username']": self.bd.wd.clickable(self.by.xpath, loc)
        self.ENG_TXT_PASSWORD = lambda loc="//input[@id='userpassword']": self.bd.wd.clickable(self.by.xpath, loc)
        self.JAP_TXT_USERNAME = lambda loc="//input[@placeholder='ユーザ名を入力']": self.bd.wd.clickable(self.by.xpath, loc)
        self.JAP_TXT_PASSWORD = lambda loc="//input[@id='userpassword']": self.bd.wd.clickable(self.by.xpath, loc) 
        self.BTN_LOGIN = lambda loc="//button[@type='submit']": self.bd.wd.clickable(self.by.xpath, loc)

        # ERROR MESSAGE
        self.ENG_WARN_MSG_USERNAME = lambda loc="//div[normalize-space()='Please enter the username']": self.bd.wd.visible(self.by.xpath, loc)
        self.ENG_WARN_MSG_PASSWORD = lambda loc="//div[normalize-space()='Please enter the password']": self.bd.wd.visible(self.by.xpath, loc)
        self.JAP_WARN_MSG_USERNAME = lambda loc="//div[normalize-space()='適切なユーザ名を入力してください']": self.bd.wd.visible(self.by.xpath, loc)
        self.JAP_WARN_MSG_PASSWORD = lambda loc="//div[normalize-space()='適切なパスワードを入力してください']": self.bd.wd.visible(self.by.xpath, loc)
        self.WARN_MSG_USERNAME_PASSWORD = lambda loc="//div[@role='alert']": self.bd.wd.visible(self.by.xpath, loc)

        self.BBUI_LABEL = lambda loc="//a[normalize-space()='Beluga Box']": self.bd.wd.visible(self.by.xpath, loc)