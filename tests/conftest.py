import os
import pytest
from selenium import webdriver
from selene.support.shared import browser



@pytest.fixture(scope='function', autouse=True) # scope='function', autouse=True
def browser_management():
    browser.config.window_height = 1000
    browser.config.window_width = 1300

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "99.0",
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
