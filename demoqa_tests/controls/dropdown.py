from selene import have
from selene.core import command
from selene.core.entity import SeleneElement
from selene.support.shared import browser


def select(element: SeleneElement, /, *, option: str):
    element.perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select-][id*=-option]').element_by(have.exact_text(option)).click()


def autocomlete(element: SeleneElement, /, *, option: str):
    element.type(option).press_enter()
