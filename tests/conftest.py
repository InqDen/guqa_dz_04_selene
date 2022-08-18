from selene.support.shared import browser
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''
@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_height = 1000
    browser.config.window_width = 1300
    browser.config.base_url = "https://demoqa.com/"
    browser.config.hold_browser_open = False #держу для проверок работоспособности
'''

'''
@pytest.fixture(scope='function', autouse=True)
def browser_management():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
'''
options = Options()
selenoid_capabilities = {
    "browserName": "chrome",
    "browserVersion": "100.0",
    "selenoid:options": {
        "enableVNC": True,
        "enableVideo": True
    }
}
options.capabilities.update(selenoid_capabilities)

driver = webdriver.Remote(
    command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
    options=options)

browser.config.driver = driver
