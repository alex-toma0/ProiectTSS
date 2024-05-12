from typing import Callable
from SeleniumTests.tests.navigation.home import back_to_home_test
from SeleniumTests.tests.navigation.profile import profile_test
from SeleniumTests.tests.auth.register import register_test
from SeleniumTests.tests.functional.playback import playback
from SeleniumTests.tests.functional.upload import upload
from config import chrome_driver, edge_driver


def run_test(test_function: Callable):
    test_function()

run_test(lambda: back_to_home_test(chrome_driver))
run_test(lambda: profile_test(chrome_driver, edge_driver))
run_test(lambda: register_test(chrome_driver))
run_test(lambda: playback(chrome_driver))
run_test(lambda: upload(chrome_driver))
