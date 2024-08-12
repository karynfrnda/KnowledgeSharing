from .. import Locator


class TopmenuLocator(Locator):
    """Topmenu page locator class"""

    def __init__(self, base) -> None:
        super().__init__(base)
        self.setup()

    def setup(self):
        # flags
        self.TOP_RIGHT_PROFILE = lambda loc="//div[@class='d-flex']": self.bd.wd.clickable(self.by.xpath, loc)
        self.SIGNOUT = lambda loc="//button[normalize-space()='Sign Out' or normalize-space()='サインオフ']": self.bd.wd.clickable(self.by.xpath, loc)
