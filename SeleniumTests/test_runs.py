from typing import Callable
from SeleniumTests.tests.navigation.home import back_to_home_test
from SeleniumTests.tests.navigation.profile import profile_test
from config import chrome_driver, edge_driver


def run_test(test_function: Callable):
    test_function()

run_test(lambda: back_to_home_test(chrome_driver))
run_test(lambda: profile_test(chrome_driver, edge_driver))
