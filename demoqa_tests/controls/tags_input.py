from selene.core.entity import Element
from typing import Optional

from selene import have
from selene.core.entity import SeleneElement
from selene.support.shared import browser

'''
def add(element: SeleneElement, /, *, from_: str, to: Optional[str] = None):
    element.type(from_)
    browser.all('.subjects-auto-complete__control').element_by(have.text(to or from_)).click()
'''

class TagsInput:
    def __init__(self, element: Element):
        self.element = element

    def add(self, from_: str, /, *, autocomplete: Optional[str] = None):
        self.element.type(from_)
        browser.all(
            '.subjects-auto-complete__option'
        ).element_by(have.text(autocomplete or from_)).click()
