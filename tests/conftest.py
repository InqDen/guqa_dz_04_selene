from selene.support.shared import browser
import pytest


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_height = 1000
    browser.config.window_width = 1300
    browser.config.base_url = "https://demoqa.com/"
    browser.config.hold_browser_open = False
