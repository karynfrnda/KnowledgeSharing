import pytest

# from database.service import DBService
from base.base_driver import BaseDriver
from ._fixtures.composition import *
from ._fixtures.auth import *
from ._fixtures.option import *
from ._fixtures.param import *
import pdb

@pytest.fixture(scope="class")
def setup(request, logger, browser, domain, service_account, store):
    # pdb.set_trace()
    print(f"def: setup conftest")
    print(f"browser: {browser}")
    print(f"domain: {domain}")
    logger

    # setup driver
    base = BaseDriver(browser, domain, fullscreen=True)
    # print("instance variable: ", base.__dict__)
    print("instance variable1: ", base.__dict__.keys())

    # setup service
    # service = DBService(domain)
    # service.start()

    # set requests
    request.cls.base = base
    request.cls.sa = service_account
    request.cls.store = store
    # request.cls.service = service
    print("before YIELD")
    yield
    print("after YIELD")

    # service.end()
    base.exit()
