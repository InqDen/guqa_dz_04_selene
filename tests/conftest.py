import os
import pytest
from selenium import webdriver
from selene.support.shared import browser
from utils import attach



def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='99.0'
    )


@pytest.fixture(scope='function', autouse=True)  # scope='function', autouse=True
def browser_management(request):
    browser.config.window_height = 1000
    browser.config.window_width = 1300
    browser_version = request.config.getoption('--browser_version')
    capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities)

    browser.config.driver = driver
    yield browser
    attach.add_log(browser)
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
    browser.quit()

