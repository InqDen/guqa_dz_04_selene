from typing import Optional

from selene import have
from selene.core.entity import SeleneElement
from selene.support.shared import browser


def add(element: SeleneElement, /, *, from_: str, to: Optional[str] = None):
    element.type(from_)
    browser.all('.subjects-auto-complete__control').element_by(have.text(to or from_)).click()