import pytest
from selenium import webdriver
from selene.support.shared import browser




@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_height = 1000
    browser.config.window_width = 1300
    browser.config.base_url = "https://demoqa.com/"
    browser.config.hold_browser_open = False #держу для проверок работоспособности

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "99.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    driver = webdriver.Remote(
        command_executor="https://user1:1234@selenoid.autotests.cloud/wd/hub",
        desired_capabilities=capabilities)
    browser.config.driver = driver

